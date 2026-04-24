import fs from 'fs';
import yaml from 'js-yaml';
import path from 'path';
import { fileURLToPath } from 'url';
import { z } from 'zod';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Export for testing
export const cvSchema = z.object({
  basics: z.object({
    name: z.string().min(1),
    label: z.string(),
    image: z.string(),
    email: z.string(),
    phone: z.string(),
    url: z.string(),
    summary: z.string(),
    location: z.object({
      address: z.string(),
      postalCode: z.string(),
      city: z.string(),
      countryCode: z.string(),
      region: z.string()
    }),
    profiles: z.array(z.object({
      network: z.string(),
      username: z.string(),
      url: z.string()
    }))
  }),
  work: z.array(z.object({
    name: z.string(),
    position: z.string(),
    url: z.string(),
    startDate: z.string(),
    endDate: z.string().nullable(),
    summary: z.string(),
    highlights: z.array(z.string())
  })),
  volunteer: z.array(z.any()).optional(),
  education: z.array(z.object({
    institution: z.string(),
    url: z.string(),
    area: z.string(),
    studyType: z.string(),
    startDate: z.string(),
    endDate: z.string().nullable(),
    score: z.string(),
    courses: z.array(z.string())
  })),
  awards: z.array(z.any()).optional(),
  certificates: z.array(z.object({
    name: z.string(),
    date: z.string(),
    issuer: z.string(),
    url: z.string()
  })).optional(),
  publications: z.array(z.any()).optional(),
  skills: z.array(z.object({
    name: z.string(),
    level: z.string(),
    keywords: z.array(z.string())
  })),
  languages: z.array(z.object({
    language: z.string(),
    fluency: z.string()
  })).optional(),
  interests: z.array(z.any()).optional(),
  references: z.array(z.any()).optional(),
  projects: z.array(z.object({
    name: z.string(),
    isActive: z.boolean().optional(),
    description: z.string(),
    highlights: z.array(z.string()),
    url: z.string(),
    github: z.string().optional()
  })).optional()
}).passthrough();

export const applySmartBolding = (text, keywords) => {
  if (!text || !keywords || keywords.length === 0) return text;
  let boldedText = text;
  keywords.forEach(keyword => {
    const regex = new RegExp(`\\b(${keyword})\\b`, 'gi');
    boldedText = boldedText.replace(regex, '<strong>$1</strong>');
  });
  return boldedText;
}

export const getSection = (sections, possibleNames) => {
  if (!sections) return null;
  for (const name of possibleNames) {
    if (sections[name]) return sections[name];
  }
  return null;
}

export const mapYamlToJson = (data) => {
  if (!data || !data.cv) {
    throw new Error('El archivo cv.yaml o la data carece de formato RenderCV.');
  }

  const cv = data.cv;
  const settings = data.settings || {};
  const boldKeywords = settings.bold_keywords || [];

  const resumeText = getSection(cv.sections, ['Resumen', 'Summary', 'About']);
  const experienceData = getSection(cv.sections, ['Experiencia', 'Experience', 'Trabajo']) || [];
  const educationData = getSection(cv.sections, ['Educación', 'Educacion', 'Education']) || [];
  const certificatesData = getSection(cv.sections, ['Certificados', 'Certificates']) || [];
  const skillsData = getSection(cv.sections, ['Habilidades', 'Skills']) || [];

  const formattedSummary = resumeText ? applySmartBolding(resumeText[0], boldKeywords) : "";

  const jsonResume = {
    basics: {
      name: cv.name || "",
      label: cv.headline || cv.label || "AI-Driven QA Engineer",
      image: "/perfil.jpg",
      email: cv.email || "",
      phone: cv.phone || "",
      url: cv.website || "",
      summary: formattedSummary,
      location: {
        address: "",
        postalCode: "1684",
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
    work: experienceData.map(w => ({
      name: w.company,
      position: w.position,
      url: "",
      startDate: w.start_date === "present" || !w.start_date ? "" : (w.start_date + "-01"),
      endDate: w.end_date === "present" || !w.end_date ? null : (w.end_date + "-01"),
      summary: "",
      highlights: (w.highlights || []).map(h => applySmartBolding(h, boldKeywords))
    })),
    volunteer: [],
    education: educationData.map(e => ({
      institution: e.institution,
      url: "",
      area: e.area,
      studyType: e.degree || "",
      startDate: e.start_date === "present" || !e.start_date ? "" : (e.start_date + "-01"),
      endDate: e.end_date === "present" || !e.end_date ? null : (e.end_date + "-01"),
      score: "",
      courses: e.highlights || []
    })),
    awards: [],
    certificates: certificatesData.map(c => ({
      name: c.name,
      date: "",
      issuer: c.issuer,
      url: ""
    })),
    publications: [],
    skills: skillsData.map(s => {
      const keywords = typeof s.details === 'string' ? s.details.split(',').map(k => k.trim()) : [];
      return {
        name: s.label,
        level: "N/A",
        keywords: keywords
      };
    }),
    languages: [
      { language: "Español", fluency: "Nativo" },
      { language: "Inglés", fluency: "Intermedio" }
    ],
    interests: [],
    references: [],
    projects: [
      {
        name: "Portfolio CV Automático",
        isActive: true,
        description: "Desarrollo de este propio CV utilizando JSON Resume y Astro, con despliegue automatizado.",
        highlights: ["JSON Resume", "Astro", "ATS Friendly"],
        url: "https://github.com/JorgeTricarico",
        github: "https://github.com/JorgeTricarico"
      }
    ]
  };

  // Validate schema. This will throw a detailed error if invalid
  return cvSchema.parse(jsonResume);
}

// Execution 
if (import.meta.url.startsWith('file:') && process.argv[1] === fileURLToPath(import.meta.url)) {
  const yamlPath = path.resolve(__dirname, '../cv.yaml');
  const jsonPath = path.resolve(__dirname, '../cv.json');

  try {
    const fileContents = fs.readFileSync(yamlPath, 'utf8');
    const data = yaml.load(fileContents);

    // Map with schema validation
    const jsonResume = mapYamlToJson(data);

    fs.writeFileSync(jsonPath, JSON.stringify(jsonResume, null, 2), 'utf8');
    console.log('✅ cv.json ha sido validado y generado exitosamente desde cv.yaml');
  } catch (e) {
    if (e instanceof z.ZodError) {
      console.error("❌ Error de Validación de Zod en el esquema del CV generado:");
      console.error(JSON.stringify(e.errors, null, 2));
      process.exit(1);
    } else {
      console.error("❌ Error convirtiendo YAML a JSON:", e.message);
      process.exit(1);
    }
  }
}
