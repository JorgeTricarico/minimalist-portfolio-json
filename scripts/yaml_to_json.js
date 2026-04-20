import fs from 'fs';
import yaml from 'js-yaml';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const yamlPath = path.resolve(__dirname, '../cv.yaml');
const jsonPath = path.resolve(__dirname, '../cv.json');

try {
  // 1. Leer el YAML
  const fileContents = fs.readFileSync(yamlPath, 'utf8');
  const data = yaml.load(fileContents);
  
  if (!data || !data.cv) {
    throw new Error('El archivo cv.yaml no tiene un formato RenderCV válido.');
  }

  const cv = data.cv;
  
  // 2. Mapear a JSON Resume (estructura esperada por tu portafolio)
  const jsonResume = {
    basics: {
      name: cv.name || "",
      label: "Especialista en IA y QA",
      image: "/perfil.jpg",
      email: cv.email || "",
      phone: cv.phone || "",
      url: cv.website || "",
      summary: cv.sections?.Resumen ? cv.sections.Resumen[0] : "",
      location: {
        address: "",
        postalCode: "1684", // Se puede agregar dinámicamente si se requiere
        city: cv.location ? cv.location.split(',')[0].trim() : "",
        countryCode: cv.location ? cv.location.split(',')[1]?.trim() : "",
        region: "Buenos Aires"
      },
      profiles: (cv.social_networks || []).map(p => ({
        network: p.network,
        username: p.username,
        url: p.network.toLowerCase() === 'linkedin' 
          ? `https://www.linkedin.com/in/${p.username}/` 
          : `https://www.github.com/${p.username}`
      }))
    },
    work: (cv.sections?.Experiencia || []).map(w => ({
      name: w.company,
      position: w.position,
      url: "",
      startDate: w.start_date === "present" ? "" : (w.start_date + "-01"), // Añade día por defecto
      endDate: w.end_date === "present" ? null : (w.end_date + "-01"),
      summary: "",
      highlights: w.highlights || []
    })),
    volunteer: [],
    education: (cv.sections?.Educacion || []).map(e => ({
      institution: e.institution,
      url: "",
      area: e.area,
      studyType: e.degree,
      startDate: e.start_date === "present" ? "" : (e.start_date + "-01"),
      endDate: e.end_date === "present" ? null : (e.end_date + "-01"),
      score: "",
      courses: e.highlights || []
    })),
    awards: [],
    certificates: (cv.sections?.Certificados || []).map(c => ({
      name: c.name,
      date: "",
      issuer: c.issuer,
      url: ""
    })),
    publications: [],
    skills: (cv.sections?.Habilidades || []).map(s => {
      // Intentar dividir details en un array si es un string separado por comas
      const keywords = typeof s.details === 'string' ? s.details.split(',').map(k => k.trim()) : [];
      return {
        name: s.label,
        level: "N/A",
        keywords: keywords
      };
    }),
    languages: [
      {
        language: "Español",
        fluency: "Nativo"
      },
      {
        language: "Inglés",
        fluency: "Intermedio"
      }
    ],
    interests: [],
    references: [],
    projects: [
      {
        name: "Portfolio CV Automático",
        isActive: true,
        description: "Desarrollo de este propio CV utilizando JSON Resume y Astro, con despliegue atomatizado.",
        highlights: [
          "JSON Resume",
          "Astro",
          "ATS Friendly"
        ],
        url: "https://github.com/JorgeTricarico",
        github: "https://github.com/JorgeTricarico"
      }
    ]
  };

  // 3. Sobrescribir el cv.json
  fs.writeFileSync(jsonPath, JSON.stringify(jsonResume, null, 2), 'utf8');
  console.log('✅ cv.json ha sido generado exitosamente desde cv.yaml');

} catch (e) {
  console.error("❌ Error convirtiendo YAML a JSON:", e.message);
}
