/**
 * md_to_yaml.mjs — Sync cv.md (English master) into cv.en.yaml.
 *
 * Source of truth: cv.md (symlinked from career-ops).
 * Target: cv.en.yaml (RenderCV format).
 *
 * OVERWRITE from cv.md:
 *   cv.headline
 *   cv.location, cv.email, cv.phone (only when present in md)
 *   cv.sections.Summary
 *   cv.sections.Experience[*].highlights (preserve company/position/dates by token-match)
 *   cv.sections.Skills (full replace, with Languages tail)
 *
 * PRESERVE in cv.en.yaml:
 *   cv.name, cv.photo, cv.social_networks
 *   cv.sections.Education (entirely)
 *   cv.sections.Projects (entirely)
 *   design, settings, locale
 *
 * cv.yaml (Spanish) is NEVER touched.
 *
 * Crash-safe: if cv.md is missing -> exit 0 without changes.
 * Fail-loud: if Summary or Experience parses empty -> exit 1 without writing.
 *
 * The script can also be imported (`parseMd`, `mergeIntoYaml`) for testing.
 */

import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';

// ---- Pure parsing functions (exported for tests) ------------------------

const DASH_RE = /[—–\-]/; // em-dash, en-dash, hyphen
const DASH_RE_GLOBAL = /\s*[—–\-]\s*/;

export function splitSections(md) {
  const sections = {};
  let current = '__preamble__';
  sections[current] = [];
  for (const line of md.split('\n')) {
    const m = line.match(/^##\s+(.+?)\s*$/);
    if (m) {
      current = m[1].trim();
      sections[current] = [];
    } else {
      sections[current].push(line);
    }
  }
  return sections;
}

export function parsePreamble(lines) {
  const out = { name: '', headline: '', contact: {} };
  for (const line of lines) {
    const h1 = line.match(/^#\s+(.+?)\s*$/);
    if (h1) { out.name = h1[1].trim(); continue; }
    const headline = line.match(/^\*\*(.+?)\*\*\s*$/);
    if (headline && !out.headline) { out.headline = headline[1].trim(); continue; }
    const kv = line.match(/^-\s+([A-Za-z][A-Za-z ]*?):\s+(.+?)\s*$/);
    if (kv) out.contact[kv[1].toLowerCase().trim()] = kv[2].trim();
  }
  return out;
}

export function parseSummary(lines) {
  const text = lines.join('\n').trim();
  if (!text) return [];
  // Split by blank lines into paragraphs
  return text.split(/\n\s*\n/).map((p) => p.trim()).filter(Boolean);
}

export function parseDateRange(s) {
  // Strip leading/trailing italic markers and whitespace
  const cleaned = s.replace(/^\*+|\*+$/g, '').trim();
  // Split on " · " to drop trailing meta ("3 years", "Part-time")
  const head = cleaned.split(/\s+[·•|]\s+/)[0].trim();
  const m = head.match(/(\d{4})\s*[—–\-]\s*(Present|present|\d{4})/);
  if (!m) return { start_date: '', end_date: '' };
  const start = `${m[1]}-01`;
  const end = /present/i.test(m[2]) ? 'present' : `${m[2]}-12`;
  return { start_date: start, end_date: end };
}

export function parseExperience(lines) {
  const entries = [];
  let cur = null;
  for (const line of lines) {
    const h3 = line.match(/^###\s+(.+?)\s*$/);
    if (h3) {
      if (cur) entries.push(cur);
      // "Position — Company" — split on first em-dash/en-dash/hyphen surrounded by spaces
      const parts = h3[1].split(DASH_RE_GLOBAL);
      const position = (parts[0] || '').trim();
      const company = parts.slice(1).join(' - ').trim();
      cur = {
        company,
        position,
        start_date: '',
        end_date: '',
        highlights: [],
      };
      continue;
    }
    if (!cur) continue;
    // Italic date line: *2026 – Present · Part-time*
    const dateLine = line.match(/^\*(.+?)\*\s*$/);
    if (dateLine && !cur.start_date) {
      const { start_date, end_date } = parseDateRange(dateLine[1]);
      if (start_date) {
        cur.start_date = start_date;
        cur.end_date = end_date;
        continue;
      }
    }
    const bullet = line.match(/^-\s+(.+?)\s*$/);
    if (bullet) cur.highlights.push(bullet[1].trim());
  }
  if (cur) entries.push(cur);
  return entries;
}

export function parseSkills(lines) {
  const entries = [];
  for (const line of lines) {
    const m = line.match(/^\*\*(.+?):\*\*\s+(.+?)\s*$/);
    if (m) entries.push({ label: m[1].trim(), details: m[2].trim() });
  }
  return entries;
}

export function parseLanguages(lines) {
  const langs = [];
  for (const line of lines) {
    const m = line.match(/^-\s+(.+?)\s*$/);
    if (m) langs.push(m[1].trim());
  }
  return langs.length ? { label: 'Languages', details: langs.join(', ') } : null;
}

export function parseMd(md) {
  const sections = splitSections(md);
  return {
    preamble: parsePreamble(sections.__preamble__ || []),
    summary: parseSummary(sections.Summary || []),
    experience: parseExperience(sections.Experience || []),
    skills: parseSkills(sections.Skills || []),
    languages: parseLanguages(sections.Languages || []),
  };
}

// ---- Matching helpers ---------------------------------------------------

/**
 * Extract the first identifying token from a company string.
 * "OneVisa (Dubai, UAE / España)" -> "onevisa"
 * "Tata Consultancy Services (Banco Galicia)" -> "tata"
 * "Ada School (Colombia)" -> "ada"
 * "Tata Consultancy Service - Banco Galicia" -> "tata"
 */
export function companyToken(company) {
  if (!company) return '';
  // Strip parentheticals and anything after a separator
  const stripped = company
    .replace(/\([^)]*\)/g, '')
    .split(DASH_RE)[0]
    .split('/')[0]
    .trim();
  const first = stripped.split(/\s+/)[0] || '';
  return first.toLowerCase();
}

export function matchExperience(prevList, parsedEntry) {
  const token = companyToken(parsedEntry.company);
  if (!token) return undefined;
  return prevList.find((p) => {
    if (!p.company) return false;
    const prevLower = p.company.toLowerCase();
    return prevLower.includes(token) || companyToken(p.company) === token;
  });
}

// ---- Merge --------------------------------------------------------------

/**
 * Merge parsed cv.md into existing yaml document.
 * Returns new doc (does NOT mutate input). Throws on invalid input.
 */
export function mergeDoc(doc, parsed) {
  if (!doc?.cv?.sections) {
    throw new Error('yaml document missing cv.sections');
  }
  const out = JSON.parse(JSON.stringify(doc)); // deep clone, simple

  // Top-level cv fields
  if (parsed.preamble.headline) out.cv.headline = parsed.preamble.headline;
  if (parsed.preamble.contact.location) out.cv.location = parsed.preamble.contact.location;
  if (parsed.preamble.contact.email) out.cv.email = parsed.preamble.contact.email;
  if (parsed.preamble.contact.phone) out.cv.phone = parsed.preamble.contact.phone;

  // Summary
  out.cv.sections.Summary = parsed.summary;

  // Experience: replace highlights only; preserve company/position/dates from yaml when matched.
  // If a parsed entry has no match, append it with parsed dates.
  // If a yaml entry has no parsed counterpart, it is REMOVED (cv.md is canonical for which roles exist).
  const prevExp = out.cv.sections.Experience || [];
  out.cv.sections.Experience = parsed.experience.map((entry) => {
    const prev = matchExperience(prevExp, entry);
    if (prev) {
      return {
        company: prev.company,
        position: prev.position,
        start_date: prev.start_date,
        end_date: prev.end_date,
        highlights: entry.highlights,
      };
    }
    return {
      company: entry.company,
      position: entry.position,
      start_date: entry.start_date,
      end_date: entry.end_date,
      highlights: entry.highlights,
    };
  });

  // Education: PRESERVE entirely — do nothing.

  // Projects: PRESERVE entirely — do nothing.

  // Skills — replace with parsed + Languages tail
  const skills = [...parsed.skills];
  if (parsed.languages) skills.push(parsed.languages);
  out.cv.sections.Skills = skills;

  return out;
}

// ---- YAML dumping (stable) ---------------------------------------------

export function dumpYaml(doc) {
  return yaml.dump(doc, {
    lineWidth: -1,
    noRefs: true,
    quotingType: '"',
    forceQuotes: true,
  });
}

// ---- Main runner --------------------------------------------------------

export function run({ cvMdPath, yamlPath, esYamlPath, log = console } = {}) {
  if (!existsSync(cvMdPath)) {
    log.warn?.(`[md_to_yaml] cv.md not found at ${cvMdPath}. Skipping.`);
    return { status: 'skipped-no-md', code: 0 };
  }

  let md;
  try {
    md = readFileSync(cvMdPath, 'utf8');
  } catch (err) {
    log.warn?.(`[md_to_yaml] failed to read cv.md: ${err.message}`);
    return { status: 'skipped-read-error', code: 0 };
  }

  let parsed;
  try {
    parsed = parseMd(md);
  } catch (err) {
    log.error?.(`[md_to_yaml] parse error: ${err.message}`);
    return { status: 'parse-error', code: 1 };
  }

  // Sanity guards: refuse to write if parsing produced empty critical sections
  if (!parsed.summary.length) {
    log.error?.('[md_to_yaml] empty Summary parsed; refusing to overwrite yaml. Check cv.md.');
    return { status: 'empty-summary', code: 1 };
  }
  if (!parsed.experience.length) {
    log.error?.('[md_to_yaml] zero Experience entries parsed; refusing to overwrite yaml. Check cv.md.');
    return { status: 'empty-experience', code: 1 };
  }

  if (!existsSync(yamlPath)) {
    log.warn?.(`[md_to_yaml] ${yamlPath} not found, skipping.`);
    return { status: 'skipped-no-yaml', code: 0 };
  }

  let doc;
  try {
    doc = yaml.load(readFileSync(yamlPath, 'utf8'));
  } catch (err) {
    log.error?.(`[md_to_yaml] failed to parse ${yamlPath}: ${err.message}`);
    return { status: 'yaml-parse-error', code: 1 };
  }

  let merged;
  try {
    merged = mergeDoc(doc, parsed);
  } catch (err) {
    log.error?.(`[md_to_yaml] merge failed: ${err.message}`);
    return { status: 'merge-error', code: 1 };
  }

  const out = dumpYaml(merged);
  const prev = existsSync(yamlPath) ? readFileSync(yamlPath, 'utf8') : '';
  if (out !== prev) {
    writeFileSync(yamlPath, out, 'utf8');
    log.log?.(`[md_to_yaml] Updated ${yamlPath.split('/').pop()}`);
  } else {
    log.log?.(`[md_to_yaml] ${yamlPath.split('/').pop()} already up-to-date.`);
  }

  if (esYamlPath && existsSync(esYamlPath)) {
    log.log?.('[md_to_yaml] cv.yaml (Spanish) NOT auto-updated. Edit manually.');
  }

  return { status: 'ok', code: 0, doc: merged };
}

// ---- CLI ---------------------------------------------------------------

const isMain = (() => {
  try {
    return resolve(process.argv[1] || '') === fileURLToPath(import.meta.url);
  } catch {
    return false;
  }
})();

if (isMain) {
  const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
  const result = run({
    cvMdPath: resolve(ROOT, 'cv.md'),
    yamlPath: resolve(ROOT, 'cv.en.yaml'),
    esYamlPath: resolve(ROOT, 'cv.yaml'),
  });
  process.exit(result.code);
}
