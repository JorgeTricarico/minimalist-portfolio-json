import fs from 'fs';
import path from 'path';
import https from 'https';

const keywords = [
  "Claude Code", "Gemini", "DeepSeek", "GitHub Copilot", "Cursor", "Antigravity", 
  "Engram", "Prompt Engineering", "OpenAI", "Anthropic", "Scikit-learn", "Pandas", 
  "NumPy", "Playwright", "Cypress", "Selenium", "Appium", "Pytest", "k6", "Performance", 
  "Postman", "Bruno", "Python", "TypeScript", "JavaScript", "Java", "Node.js", 
  "FastAPI", "Flask", "AWS", "Docker", "Jenkins", "Linux", "Bash", "CI/CD", 
  "Grafana", "Kibana", "SQL", "NoSQL", "Matplotlib", "Seaborn", 
  "Análisis de Traces/Logs", "GitHub Actions", "Español", "Inglés"
];

const ICONS_DIR = path.resolve('public/icons');

const logos = {
  "javascript": "logos:javascript",
  "typescript": "logos:typescript-icon",
  "postgresql": "logos:postgresql",
  "mongodb": "logos:mongodb-icon",
  "python": "logos:python",
  "java": "logos:java",
  "js": "logos:javascript",
  "ts": "logos:typescript-icon",
  "node": "logos:nodejs-icon",
  "fastapi": "logos:fastapi-icon",
  "flask": "logos:flask",
  "pandas": "logos:pandas-icon",
  "numpy": "logos:numpy",
  "matplotlib": "logos:matplotlib-icon",
  "seaborn": "logos:seaborn-icon",
  "aws": "logos:aws",
  "amazon": "logos:aws",
  "azure": "logos:microsoft-azure",
  "docker": "logos:docker-icon",
  "jenkins": "logos:jenkins",
  "github actions": "logos:github-actions",
  "postman": "logos:postman-icon",
  "selenium": "logos:selenium",
  "playwright": "logos:playwright",
  "cypress": "logos:cypress-icon",
  "mysql": "logos:mysql-icon",
  "openai": "logos:openai-icon",
  "chatgpt": "logos:openai-icon",
  "langchain": "logos:langchain-icon",
  "hugging": "logos:hugging-face-icon",
};

const simple = {
  "playwright": "playwright",
  "cypress": "cypress",
  "appium": "appium",
  "pytest": "pytest",
  "bruno": "bruno",
  "k6": "k6",
  "anthropic": "anthropic",
  "claude": "anthropic",
  "deepseek": "deepseek",
  "copilot": "githubcopilot",
  "cursor": "cursor",
  "linux": "linux",
  "bash": "gnubash",
  "supabase": "supabase",
  "scikit": "scikitlearn",
  "gemini": "googlegemini",
  "nosql": "mongodb",
  "sql": "postgresql",
  "grafana": "grafana",
  "kibana": "kibana"
};

const getIconUrl = (name) => {
  const n = name.toLowerCase().trim();
  
  const foundLogo = Object.keys(logos)
    .sort((a, b) => b.length - a.length)
    .find(key => n.includes(key));
  if (foundLogo) return `https://api.iconify.design/${logos[foundLogo]}.svg`;

  const foundSimple = Object.keys(simple)
    .sort((a, b) => b.length - a.length)
    .find(key => n.includes(key));
  
  if (foundSimple) {
    const slug = simple[foundSimple];
    if (slug === 'deepseek') return `https://api.iconify.design/logos:deepseek-icon.svg`;
    if (slug === 'googlegemini' || slug === 'gemini') return `https://api.iconify.design/simple-icons:googlegemini.svg?color=%231A73E8`;
    if (slug === 'scikitlearn') return `https://api.iconify.design/simple-icons:scikitlearn.svg?color=%23F89939`;
    if (slug === 'anthropic' || slug === 'claude') return `https://api.iconify.design/simple-icons:anthropic.svg?color=%23191919`;
    return `https://cdn.simpleicons.org/${slug}`;
  }

  if (n.includes("nosql")) return "https://api.iconify.design/material-symbols:database-off-outline.svg";
  if (n.includes("sql")) return "https://api.iconify.design/material-symbols:database-outline.svg";
  if (n.includes("bot") || n.includes("agente") || n.includes("antigravity") || n.includes("cobrotron") || n.includes("fulltron")) return "https://api.iconify.design/lucide:bot.svg";
  if (n.includes("engram")) return "https://api.iconify.design/ph:brain-duotone.svg";
  if (n.includes("logs") || n.includes("traces") || n.includes("análisis")) return "https://api.iconify.design/lucide:file-search.svg";
  if (n.includes("idioma") || n.includes("inglés") || n.includes("español")) return "https://api.iconify.design/lucide:languages.svg";
  if (n.includes("ci/cd") || n.includes("pipeline")) return "https://api.iconify.design/lucide:infinity.svg";
  if (n.includes("performance") || n.includes("rendimiento")) return "https://api.iconify.design/lucide:gauge.svg";
  
  return "https://api.iconify.design/lucide:code-2.svg";
};

const download = (url, dest) => {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      if (response.statusCode !== 200) {
        reject(new Error(`Failed to get '${url}' (${response.statusCode})`));
        return;
      }
      const file = fs.createWriteStream(dest);
      response.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve();
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
};

async function run() {
  if (!fs.existsSync(ICONS_DIR)) {
    fs.mkdirSync(ICONS_DIR, { recursive: true });
  }

  for (const keyword of keywords) {
    const url = getIconUrl(keyword);
    const fileName = keyword.toLowerCase().replace(/[^a-z0-9]/g, '_') + '.svg';
    const filePath = path.join(ICONS_DIR, fileName);
    
    console.log(`Downloading ${keyword} from ${url}...`);
    try {
      await download(url, filePath);
      console.log(`Success: ${fileName}`);
    } catch (err) {
      console.error(`Error downloading ${keyword}: ${err.message}`);
    }
  }
}

run();
