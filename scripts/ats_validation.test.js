import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { describe, it, expect } from 'vitest';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const pdf = require('pdf-parse');

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const WORKSPACE_DIR = path.resolve(__dirname, '..');

// Utilidad para limpiar textos y facilitar búsquedas flexibles (ignora mayúsculas, espacios adicionales y acentos)
function normalizeText(text) {
  if (!text) return '';
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // Elimina acentos
    .replace(/\s+/g, ' ')
    .trim();
}

// Lista de encabezados de sección estándar permitidos por ATS
const STANDARD_HEADERS_ES = [
  'resumen', 'summary', 'perfil', 'experiencia', 'experiencia laboral', 'experiencia profesional',
  'trabajo', 'education', 'educacion', 'formacion', 'habilidades', 'skills', 'aptitudes',
  'certificados', 'certificaciones', 'certificates', 'proyectos', 'projects', 'idiomas', 'languages'
];

const STANDARD_HEADERS_EN = [
  'summary', 'profile', 'experience', 'work experience', 'professional experience',
  'education', 'skills', 'key skills', 'competencies', 'certificates', 'certifications',
  'projects', 'languages', 'interests'
];

// Helper para parsear un PDF usando la librería pdf-parse
async function parsePdf(pdfPath) {
  if (!fs.existsSync(pdfPath)) {
    throw new Error(`El archivo PDF no existe en la ruta: ${pdfPath}`);
  }
  const dataBuffer = fs.readFileSync(pdfPath);
  // El constructor de PDFParse internamente carga el archivo si le pasamos data o url
  const parser = new pdf.PDFParse({ 
    verbosity: 0,
    data: new Uint8Array(dataBuffer)
  });
  
  const textResult = await parser.getText();
  const infoResult = await parser.getInfo({ parsePageInfo: true });
  await parser.destroy();
  
  return {
    text: textResult.text,
    info: infoResult
  };
}

describe('parsePdf Helper', () => {
  it('Debe lanzar un error si el archivo PDF no existe', async () => {
    const nonExistentPath = path.join(WORKSPACE_DIR, 'archivo_que_no_existe.pdf');
    await expect(parsePdf(nonExistentPath)).rejects.toThrow(
      `El archivo PDF no existe en la ruta: ${nonExistentPath}`
    );
  });

  it('Debe lanzar un error para archivos vacíos (sin contenido PDF válido)', async () => {
    const emptyFilePath = path.join(WORKSPACE_DIR, 'empty.pdf');
    fs.writeFileSync(emptyFilePath, '');
    await expect(parsePdf(emptyFilePath)).rejects.toThrow();
    fs.unlinkSync(emptyFilePath);
  });
});

describe('Validación de Legibilidad ATS - CV en Español', () => {
  const pdfPath = path.join(WORKSPACE_DIR, 'public', 'cv.pdf');
  const jsonPath = path.join(WORKSPACE_DIR, 'cv.json');

  let pdfData = null;
  let jsonData = null;

  it('Debe cargar exitosamente el PDF y el JSON correspondiente', async () => {
    expect(fs.existsSync(pdfPath)).toBe(true);
    expect(fs.existsSync(jsonPath)).toBe(true);

    jsonData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    pdfData = await parsePdf(pdfPath);

    expect(jsonData).toBeDefined();
    expect(pdfData.text).toBeDefined();
    expect(pdfData.text.length).toBeGreaterThan(100);
  });

  it('Debe contener los Datos Personales Críticos (Nombre, Email, Teléfono, Perfiles)', () => {
    const normalizedPdf = normalizeText(pdfData.text);

    // 1. Nombre Completo
    const name = jsonData.basics.name;
    expect(normalizedPdf).toContain(normalizeText(name));

    // 2. Email
    const email = jsonData.basics.email;
    expect(normalizedPdf).toContain(normalizeText(email));

    // 3. Teléfono (comprobando existencia de los últimos dígitos significativos)
    const phoneDigits = jsonData.basics.phone.replace(/\D/g, '').slice(-8);
    expect(normalizedPdf.replace(/\D/g, '')).toContain(phoneDigits);

    // 4. Perfiles Sociales (LinkedIn, GitHub)
    jsonData.basics.profiles.forEach(profile => {
      const username = profile.username;
      expect(normalizedPdf).toContain(normalizeText(username));
    });
  });

  it('Debe asegurar la Linealidad Secuencial y Cronológica de la Experiencia Laboral', () => {
    const normalizedPdf = normalizeText(pdfData.text);
    const workExperiences = jsonData.work || [];

    if (workExperiences.length > 1) {
      let previousIndex = -1;

      workExperiences.forEach((exp, index) => {
        const companyName = exp.name.split('-')[0].trim(); // Extraemos la parte principal del nombre de la empresa
        const normalizedCompany = normalizeText(companyName);
        const currentIndex = normalizedPdf.indexOf(normalizedCompany);

        // Verificamos que la empresa actual aparezca en el documento
        expect(currentIndex).toBeGreaterThan(-1);

        if (index > 0 && previousIndex !== -1) {
          // El trabajo más reciente (primer elemento en JSON Resume) debe aparecer antes que el trabajo más antiguo
          // Esto valida que un parser de arriba-hacia-abajo lea de forma lineal y cronológica correcta
          expect(currentIndex).toBeGreaterThan(previousIndex);
        }
        previousIndex = currentIndex;
      });
    }
  });

  it('Debe poseer Encabezados de Sección Compatibles con la Ontología ATS Estándar', () => {
    const outline = pdfData.info.outline || [];
    expect(outline.length).toBeGreaterThan(0);

    // Extraemos todos los marcadores del esquema (Bookmarks/Outline) definidos en el PDF
    const extractOutlineTitles = (items) => {
      let titles = [];
      items.forEach(item => {
        titles.push(item.title);
        if (item.items && item.items.length > 0) {
          titles = titles.concat(extractOutlineTitles(item.items));
        }
      });
      return titles;
    };

    const outlineTitles = extractOutlineTitles(outline);

    // Validar que cada cabecera de sección de primer nivel sea ATS-Friendly
    outlineTitles.forEach(title => {
      // Ignorar el propio nombre del candidato como cabecera si está en el outline
      if (normalizeText(title) === normalizeText(jsonData.basics.name)) return;

      const isFriendly = STANDARD_HEADERS_ES.some(stdHeader => 
        normalizeText(title).includes(stdHeader)
      );

      // Si no es un encabezado estándar común, lanzamos un error explícito para advertir mejores prácticas
      expect(isFriendly).toBe(true);
    });
  });

  it('Debe validar que todas las Habilidades Principales estén en el PDF', () => {
    const normalizedPdf = normalizeText(pdfData.text);
    const skills = jsonData.skills || [];

    skills.forEach(skill => {
      // Comprobar la categoría de la habilidad
      expect(normalizedPdf).toContain(normalizeText(skill.name));

      // Comprobar las palabras clave (keywords)
      skill.keywords.forEach(keyword => {
        // Hacemos una validación de presencia flexible para palabras clave compuestas o abreviadas
        expect(normalizedPdf).toContain(normalizeText(keyword));
      });
    });
  });

  it('No debe contener caracteres corruptos ni glifos rotos de fuentes', () => {
    // La presencia de múltiples caracteres nulos (\u0000) o rombos de reemplazo indica mala codificación tipográfica
    expect(pdfData.text).not.toContain('\u0000');
    expect(pdfData.text).not.toContain('\uFFFD');
  });

  it('Debe tener metadatos de creación fiables de PDF', () => {
    const creator = pdfData.info.info.Creator;
    expect(creator).toBeDefined();
    // Validamos que sea Typst o RenderCV la herramienta emisora (muy compatibles con ATS)
    expect(normalizeText(creator)).toMatch(/(typst|rendercv|latex)/);
  });
});

describe('ATS Legibility Validation - English CV', () => {
  const pdfPath = path.join(WORKSPACE_DIR, 'public', 'cv_en.pdf');
  const jsonPath = path.join(WORKSPACE_DIR, 'cv.en.json');

  let pdfData = null;
  let jsonData = null;

  it('Should load the English PDF and JSON successfully', async () => {
    expect(fs.existsSync(pdfPath)).toBe(true);
    expect(fs.existsSync(jsonPath)).toBe(true);

    jsonData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    pdfData = await parsePdf(pdfPath);

    expect(jsonData).toBeDefined();
    expect(pdfData.text).toBeDefined();
    expect(pdfData.text.length).toBeGreaterThan(100);
  });

  it('Should contain critical contact details', () => {
    const normalizedPdf = normalizeText(pdfData.text);

    // 1. Name
    expect(normalizedPdf).toContain(normalizeText(jsonData.basics.name));

    // 2. Email
    expect(normalizedPdf).toContain(normalizeText(jsonData.basics.email));

    // 3. Teléfono (comprobando los últimos dígitos significativos para evadir diferencias de prefijo internacional)
    const phoneDigits = jsonData.basics.phone.replace(/\D/g, '').slice(-8);
    expect(normalizedPdf.replace(/\D/g, '')).toContain(phoneDigits);

    // 4. Perfiles Sociales (LinkedIn, GitHub)
    jsonData.basics.profiles.forEach(profile => {
      expect(normalizedPdf).toContain(normalizeText(profile.username));
    });
  });

  it('Should maintain a sequential cronological linear flow of work experience', () => {
    const normalizedPdf = normalizeText(pdfData.text);
    const workExperiences = jsonData.work || [];

    if (workExperiences.length > 1) {
      let previousIndex = -1;

      workExperiences.forEach((exp, index) => {
        // En inglés extraemos la primera parte del nombre de la compañía
        const companyName = exp.name.split('-')[0].trim();
        const normalizedCompany = normalizeText(companyName);
        const currentIndex = normalizedPdf.indexOf(normalizedCompany);

        expect(currentIndex).toBeGreaterThan(-1);

        if (index > 0 && previousIndex !== -1) {
          expect(currentIndex).toBeGreaterThan(previousIndex);
        }
        previousIndex = currentIndex;
      });
    }
  });

  it('Should use standard ATS-friendly headers in the outline', () => {
    const outline = pdfData.info.outline || [];
    expect(outline.length).toBeGreaterThan(0);

    const extractOutlineTitles = (items) => {
      let titles = [];
      items.forEach(item => {
        titles.push(item.title);
        if (item.items && item.items.length > 0) {
          titles = titles.concat(extractOutlineTitles(item.items));
        }
      });
      return titles;
    };

    const outlineTitles = extractOutlineTitles(outline);

    outlineTitles.forEach(title => {
      if (normalizeText(title) === normalizeText(jsonData.basics.name)) return;

      const isFriendly = STANDARD_HEADERS_EN.some(stdHeader => 
        normalizeText(title).includes(stdHeader)
      );

      expect(isFriendly).toBe(true);
    });
  });

  it('Should include all key skills and keywords in the PDF', () => {
    const normalizedPdf = normalizeText(pdfData.text);
    const skills = jsonData.skills || [];

    skills.forEach(skill => {
      expect(normalizedPdf).toContain(normalizeText(skill.name));
      skill.keywords.forEach(keyword => {
        expect(normalizedPdf).toContain(normalizeText(keyword));
      });
    });
  });
});
