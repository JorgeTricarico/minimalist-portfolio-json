import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { readFileSync, writeFileSync, mkdtempSync, rmSync, existsSync, copyFileSync } from 'node:fs';
import { join, resolve, dirname } from 'node:path';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';

import {
  splitSections,
  parsePreamble,
  parseSummary,
  parseExperience,
  parseDateRange,
  parseSkills,
  parseLanguages,
  parseMd,
  companyToken,
  matchExperience,
  mergeDoc,
  dumpYaml,
  run,
} from './md_to_yaml.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const FIX = join(__dirname, '__fixtures__');
const STD_MD = readFileSync(join(FIX, 'cv.standard.md'), 'utf8');
const STD_YAML_TEXT = readFileSync(join(FIX, 'cv.en.yaml'), 'utf8');

let tmp;
beforeEach(() => {
  tmp = mkdtempSync(join(tmpdir(), 'md2yaml-'));
});
afterEach(() => {
  rmSync(tmp, { recursive: true, force: true });
});

const silentLog = { warn() {}, error() {}, log() {} };

function setupFiles({ md = STD_MD, yamlText = STD_YAML_TEXT, esText = 'spanish: untouched\n' } = {}) {
  const cvMd = join(tmp, 'cv.md');
  const cvYaml = join(tmp, 'cv.en.yaml');
  const esYaml = join(tmp, 'cv.yaml');
  writeFileSync(cvMd, md);
  writeFileSync(cvYaml, yamlText);
  writeFileSync(esYaml, esText);
  return { cvMd, cvYaml, esYaml };
}

// ---- Parser unit tests --------------------------------------------------

describe('parseDateRange', () => {
  it('handles em-dash with Present', () => {
    expect(parseDateRange('2026 — Present')).toEqual({ start_date: '2026-01', end_date: 'present' });
  });
  it('handles en-dash with year', () => {
    expect(parseDateRange('2023 – 2024')).toEqual({ start_date: '2023-01', end_date: '2024-12' });
  });
  it('handles plain hyphen', () => {
    expect(parseDateRange('2020 - 2022')).toEqual({ start_date: '2020-01', end_date: '2022-12' });
  });
  it('strips trailing meta after middle dot', () => {
    expect(parseDateRange('2023 – Present · 3 years')).toEqual({ start_date: '2023-01', end_date: 'present' });
  });
  it('returns empty on garbage', () => {
    expect(parseDateRange('not a date')).toEqual({ start_date: '', end_date: '' });
  });
});

describe('parsePreamble', () => {
  it('extracts name, headline and contact bullets', () => {
    const lines = [
      '# Jorge Tricarico',
      '',
      '**AI-Driven QA Engineer**',
      '',
      '- Location: Buenos Aires, AR',
      '- Email: jorge@example.com',
      '- Phone: +54 9 11 50479769',
    ];
    const out = parsePreamble(lines);
    expect(out.name).toBe('Jorge Tricarico');
    expect(out.headline).toBe('AI-Driven QA Engineer');
    expect(out.contact.location).toBe('Buenos Aires, AR');
    expect(out.contact.email).toBe('jorge@example.com');
    expect(out.contact.phone).toBe('+54 9 11 50479769');
  });
  it('tolerates missing phone', () => {
    const out = parsePreamble(['# Jorge', '**Headline**', '- Email: a@b.com']);
    expect(out.contact.phone).toBeUndefined();
    expect(out.contact.email).toBe('a@b.com');
  });
});

describe('parseSummary', () => {
  it('splits by blank lines', () => {
    const out = parseSummary(['', 'First paragraph.', '', 'Second paragraph.', '']);
    expect(out).toEqual(['First paragraph.', 'Second paragraph.']);
  });
  it('returns empty for blank input', () => {
    expect(parseSummary(['', '   ', ''])).toEqual([]);
  });
});

describe('parseExperience', () => {
  it('parses three entries from the standard fixture', () => {
    const sections = splitSections(STD_MD);
    const exp = parseExperience(sections.Experience);
    expect(exp.length).toBe(3);
    expect(exp[0].company).toContain('OneVisa');
    expect(exp[0].position).toContain('Senior Principal QA Engineer');
    expect(exp[0].start_date).toBe('2026-01');
    expect(exp[0].end_date).toBe('present');
    expect(exp[0].highlights.length).toBe(2);
    expect(exp[0].highlights[0]).toContain('**Sole QA**');
  });
  it('preserves bold markers and special chars in highlights', () => {
    const md = `### Foo — Bar\n*2020 – 2021*\n\n- **bold** with \`code\` and *italic* and (parens) and "quotes" — em-dash`;
    const sections = splitSections('## Experience\n' + md);
    const exp = parseExperience(sections.Experience);
    expect(exp[0].highlights[0]).toBe('**bold** with `code` and *italic* and (parens) and "quotes" — em-dash');
  });
});

describe('companyToken', () => {
  it('strips parentheticals', () => {
    expect(companyToken('OneVisa (Dubai, UAE / España)')).toBe('onevisa');
  });
  it('takes first word from multi-word company', () => {
    expect(companyToken('Tata Consultancy Services (Banco Galicia)')).toBe('tata');
  });
  it('strips after dash', () => {
    expect(companyToken('Tata Consultancy Service - Banco Galicia')).toBe('tata');
  });
  it('handles empty', () => {
    expect(companyToken('')).toBe('');
  });
});

describe('matchExperience', () => {
  const yamlExp = [
    { company: 'OneVisa - Dubai (UAE) / Spain' },
    { company: 'Tata Consultancy Service - Banco Galicia' },
    { company: 'Ada School - Colombia' },
  ];
  it('matches OneVisa via token', () => {
    expect(matchExperience(yamlExp, { company: 'OneVisa (Dubai, UAE / España)' }).company).toBe('OneVisa - Dubai (UAE) / Spain');
  });
  it('matches Tata via token', () => {
    expect(matchExperience(yamlExp, { company: 'Tata Consultancy Services (Banco Galicia)' }).company).toContain('Tata');
  });
  it('matches Ada via token', () => {
    expect(matchExperience(yamlExp, { company: 'Ada School (Colombia)' }).company).toContain('Ada');
  });
  it('returns undefined for unknown company', () => {
    expect(matchExperience(yamlExp, { company: 'Acme Corp' })).toBeUndefined();
  });
});

describe('parseSkills + parseLanguages', () => {
  it('parses bold-prefix labelled skill lines', () => {
    expect(parseSkills(['**AI:** Claude, Gemini', '**QA:** Playwright'])).toEqual([
      { label: 'AI', details: 'Claude, Gemini' },
      { label: 'QA', details: 'Playwright' },
    ]);
  });
  it('joins multiple languages', () => {
    expect(parseLanguages(['- Spanish (native)', '- English', '- French'])).toEqual({
      label: 'Languages',
      details: 'Spanish (native), English, French',
    });
  });
  it('returns null when no languages', () => {
    expect(parseLanguages([])).toBeNull();
  });
});

// ---- mergeDoc semantics -------------------------------------------------

describe('mergeDoc — preserve/overwrite contract', () => {
  let doc;
  let parsed;
  beforeEach(() => {
    doc = yaml.load(STD_YAML_TEXT);
    parsed = parseMd(STD_MD);
  });

  it('preserves company, position, dates from yaml; replaces only highlights', () => {
    const merged = mergeDoc(doc, parsed);
    const onevisa = merged.cv.sections.Experience[0];
    expect(onevisa.company).toBe('OneVisa - Dubai (UAE) / Spain');
    expect(onevisa.position).toBe('(Part-time) Senior Principal QA Engineer (AI & Reliability)');
    expect(onevisa.start_date).toBe('2026-02');
    expect(onevisa.end_date).toBe('present');
    expect(onevisa.highlights[0]).toContain('**Sole QA**');
    // Old highlights gone
    expect(onevisa.highlights.find((h) => h === 'OLD HIGHLIGHT 1')).toBeUndefined();
  });

  it('preserves Education entirely', () => {
    const merged = mergeDoc(doc, parsed);
    expect(merged.cv.sections.Education).toEqual(doc.cv.sections.Education);
  });

  it('preserves Projects entirely', () => {
    const merged = mergeDoc(doc, parsed);
    expect(merged.cv.sections.Projects).toEqual(doc.cv.sections.Projects);
  });

  it('preserves design, settings, locale', () => {
    const merged = mergeDoc(doc, parsed);
    expect(merged.design).toEqual(doc.design);
    expect(merged.settings).toEqual(doc.settings);
    expect(merged.locale).toEqual(doc.locale);
  });

  it('preserves cv.name, photo, social_networks', () => {
    const merged = mergeDoc(doc, parsed);
    expect(merged.cv.name).toBe('Jorge Tricarico');
    expect(merged.cv.photo).toBe('public/perfil_rounded.png');
    expect(merged.cv.social_networks).toEqual(doc.cv.social_networks);
  });

  it('overwrites headline, location, email, phone from md', () => {
    const merged = mergeDoc(doc, parsed);
    expect(merged.cv.headline).toBe('AI-Driven QA Engineer');
    expect(merged.cv.location).toBe('Buenos Aires, AR');
    expect(merged.cv.email).toBe('jorge.tricarico@gmail.com');
    expect(merged.cv.phone).toBe('+54 9 11 50479769');
  });

  it('overwrites Summary and Skills', () => {
    const merged = mergeDoc(doc, parsed);
    expect(merged.cv.sections.Summary[0]).toContain('QA engineer');
    expect(merged.cv.sections.Skills.find((s) => s.label === 'AI & Agents')).toBeTruthy();
    expect(merged.cv.sections.Skills.find((s) => s.label === 'Languages').details).toBe('Spanish (native), English');
  });

  it('does not overwrite phone if missing in md', () => {
    const mdNoPhone = STD_MD.replace(/^- Phone:.*$/m, '');
    const parsed2 = parseMd(mdNoPhone);
    const merged = mergeDoc(doc, parsed2);
    expect(merged.cv.phone).toBe('+0 000'); // preserved
  });

  it('appends new experience entry not in yaml with parsed dates', () => {
    const docMissing = yaml.load(STD_YAML_TEXT);
    docMissing.cv.sections.Experience = docMissing.cv.sections.Experience.filter(
      (e) => !/ada/i.test(e.company),
    );
    const merged = mergeDoc(docMissing, parsed);
    const ada = merged.cv.sections.Experience.find((e) => /ada/i.test(e.company));
    expect(ada).toBeTruthy();
    expect(ada.start_date).toBe('2023-01');
    expect(ada.end_date).toBe('2024-12');
  });

  it('removes experience entries that disappear from cv.md', () => {
    const mdNoAda = STD_MD.replace(/### Python Professor[\s\S]*?(?=\n## |$)/, '');
    const parsed2 = parseMd(mdNoAda);
    const merged = mergeDoc(doc, parsed2);
    expect(merged.cv.sections.Experience.find((e) => /ada/i.test(e.company))).toBeUndefined();
  });

  it('reflects experience reordering from cv.md', () => {
    // Build a reordered cv.md by hand: Tata first, then OneVisa, then Ada.
    const reorderedMd = `# Jorge Tricarico

**AI-Driven QA Engineer**

- Location: Buenos Aires, AR
- Email: jorge.tricarico@gmail.com

## Summary

Some summary.

## Experience

### QA Automation — Tata Consultancy Services (Banco Galicia)
*2023 – Present*

- Tata bullet.

### Senior Principal QA Engineer — OneVisa (Dubai)
*2026 – Present*

- OneVisa bullet.

### Python Professor — Ada School
*2023 – 2024*

- Ada bullet.

## Skills

**AI:** Claude
`;
    const parsed2 = parseMd(reorderedMd);
    const merged = mergeDoc(doc, parsed2);
    expect(/Tata/i.test(merged.cv.sections.Experience[0].company)).toBe(true);
    expect(/OneVisa/i.test(merged.cv.sections.Experience[1].company)).toBe(true);
    expect(/Ada/i.test(merged.cv.sections.Experience[2].company)).toBe(true);
  });

  it('throws when doc is missing cv.sections', () => {
    expect(() => mergeDoc({}, parsed)).toThrow();
  });
});

// ---- Idempotency --------------------------------------------------------

describe('idempotency', () => {
  it('parse → merge → dump → parse → merge → dump produces identical bytes', () => {
    const doc = yaml.load(STD_YAML_TEXT);
    const parsed = parseMd(STD_MD);
    const out1 = dumpYaml(mergeDoc(doc, parsed));
    const doc2 = yaml.load(out1);
    const out2 = dumpYaml(mergeDoc(doc2, parsed));
    expect(out2).toBe(out1);
  });

  it('run() twice on disk produces identical files', () => {
    const { cvMd, cvYaml, esYaml } = setupFiles();
    expect(run({ cvMdPath: cvMd, yamlPath: cvYaml, esYamlPath: esYaml, log: silentLog }).code).toBe(0);
    const after1 = readFileSync(cvYaml, 'utf8');
    expect(run({ cvMdPath: cvMd, yamlPath: cvYaml, esYamlPath: esYaml, log: silentLog }).code).toBe(0);
    const after2 = readFileSync(cvYaml, 'utf8');
    expect(after2).toBe(after1);
  });
});

// ---- run() integration --------------------------------------------------

describe('run() — integration', () => {
  it('exits 0 and leaves yaml unchanged when cv.md is missing', () => {
    const { cvYaml, esYaml } = setupFiles();
    rmSync(join(tmp, 'cv.md'));
    const before = readFileSync(cvYaml, 'utf8');
    const result = run({ cvMdPath: join(tmp, 'cv.md'), yamlPath: cvYaml, esYamlPath: esYaml, log: silentLog });
    expect(result.code).toBe(0);
    expect(readFileSync(cvYaml, 'utf8')).toBe(before);
  });

  it('exits 1 and leaves yaml untouched when Summary is empty', () => {
    const md = STD_MD.replace(/## Summary[\s\S]*?(?=\n## )/, '## Summary\n\n');
    const { cvMd, cvYaml, esYaml } = setupFiles({ md });
    const before = readFileSync(cvYaml, 'utf8');
    const result = run({ cvMdPath: cvMd, yamlPath: cvYaml, esYamlPath: esYaml, log: silentLog });
    expect(result.code).toBe(1);
    expect(readFileSync(cvYaml, 'utf8')).toBe(before);
  });

  it('exits 1 and leaves yaml untouched when Experience is empty', () => {
    const md = STD_MD.replace(/## Experience[\s\S]*?(?=\n## )/, '## Experience\n\n');
    const { cvMd, cvYaml, esYaml } = setupFiles({ md });
    const before = readFileSync(cvYaml, 'utf8');
    const result = run({ cvMdPath: cvMd, yamlPath: cvYaml, esYamlPath: esYaml, log: silentLog });
    expect(result.code).toBe(1);
    expect(readFileSync(cvYaml, 'utf8')).toBe(before);
  });

  it('never touches cv.yaml (Spanish)', () => {
    const { cvMd, cvYaml, esYaml } = setupFiles();
    const esBefore = readFileSync(esYaml, 'utf8');
    run({ cvMdPath: cvMd, yamlPath: cvYaml, esYamlPath: esYaml, log: silentLog });
    expect(readFileSync(esYaml, 'utf8')).toBe(esBefore);
  });

  it('handles different dash characters in dates', () => {
    const md = STD_MD
      .replace('2026 – Present', '2026 — Present') // em
      .replace('2023 – Present', '2023 - Present') // hyphen
      .replace('2023 – 2024', '2023–2024'); // en, no spaces
    const parsed = parseMd(md);
    expect(parsed.experience[0].start_date).toBe('2026-01');
    expect(parsed.experience[1].start_date).toBe('2023-01');
    expect(parsed.experience[2]).toMatchObject({ start_date: '2023-01', end_date: '2024-12' });
  });

  it('handles missing Languages section', () => {
    const md = STD_MD.replace(/## Languages[\s\S]*$/, '');
    const parsed = parseMd(md);
    expect(parsed.languages).toBeNull();
    const doc = yaml.load(STD_YAML_TEXT);
    const merged = mergeDoc(doc, parsed);
    expect(merged.cv.sections.Skills.find((s) => s.label === 'Languages')).toBeUndefined();
  });
});
