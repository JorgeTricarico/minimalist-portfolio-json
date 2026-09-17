// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Jorge Tricarico",
  title: "Jorge Tricarico - CV",
  footer: context { [#emph[Jorge Tricarico -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Last updated in Sept 2026] ],
  locale-catalog-language: "en",
  text-direction: ltr,
  page-size: "a4",
  page-top-margin: 1.0cm,
  page-bottom-margin: 1.0cm,
  page-left-margin: 1.2cm,
  page-right-margin: 1.2cm,
  page-show-footer: false,
  page-show-top-note: false,
  colors-body: rgb(0, 0, 0),
  colors-name: rgb(0, 79, 144),
  colors-headline: rgb(0, 79, 144),
  colors-connections: rgb(0, 79, 144),
  colors-section-titles: rgb(0, 79, 144),
  colors-links: rgb(0, 79, 144),
  colors-footer: rgb(128, 128, 128),
  colors-top-note: rgb(128, 128, 128),
  typography-line-spacing: 0.6em,
  typography-alignment: "justified",
  typography-date-and-location-column-alignment: right,
  typography-font-family-body: "Source Sans 3",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "Source Sans 3",
  typography-font-size-body: 9pt,
  typography-font-size-name: 24pt,
  typography-font-size-headline: 10pt,
  typography-font-size-connections: 9pt,
  typography-font-size-section-titles: 1.2em,
  typography-small-caps-name: false,
  typography-small-caps-headline: false,
  typography-small-caps-connections: false,
  typography-small-caps-section-titles: true,
  typography-bold-name: true,
  typography-bold-headline: false,
  typography-bold-connections: false,
  typography-bold-section-titles: true,
  links-underline: false,
  links-show-external-link-icon: false,
  header-alignment: center,
  header-photo-width: 3.5cm,
  header-space-below-name: 0.2cm,
  header-space-below-headline: 0.2cm,
  header-space-below-connections: 0.25cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.5cm,
  section-titles-type: "with_partial_line",
  section-titles-line-thickness: 0.5pt,
  section-titles-space-above: 0.3cm,
  section-titles-space-below: 0.15cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.2em,
  sections-space-between-regular-entries: 0.4em,
  entries-date-and-location-width: 3.8cm,
  entries-side-space: 0.2cm,
  entries-space-between-columns: 0.1cm,
  entries-allow-page-break: false,
  entries-short-second-row: true,
  entries-degree-width: 0cm,
  entries-summary-space-left: 0cm,
  entries-summary-space-above: 0cm,
  entries-highlights-bullet:  "•" ,
  entries-highlights-nested-bullet:  "•" ,
  entries-highlights-space-left: 0.15cm,
  entries-highlights-space-above: 0cm,
  entries-highlights-space-between-items: 0cm,
  entries-highlights-space-between-bullet-and-text: 0.5em,
  date: datetime(
    year: 2026,
    month: 9,
    day: 16,
  ),
)


#grid(
  columns: (auto, 1fr),
  column-gutter: 0cm,
  align: horizon + left,
  [#pad(left: 0.4cm, right: 0.4cm, image("perfil_rounded.png", width: 3.5cm))
],
  [
= Jorge Tricarico

  #headline([AI-Driven QA Engineer])

#connections(
  [#connection-with-icon("location-dot")[Buenos Aires, AR]],
  [#link("mailto:jorge.tricarico@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[jorge.tricarico\@gmail.com]]],
  [#link("tel:+54-9-11-5047-9769", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[011 15-5047-9769]]],
  [#link("https://linkedin.com/in/jorge-tricarico", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[jorge-tricarico]]],
  [#link("https://github.com/JorgeTricarico", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[JorgeTricarico]]],
)
  ]
)


== Summary

QA Engineer and AI Specialist focused on product creation and software reliability. I have a full-stack technical profile that I leverage through the advanced use of LLMs and agentic tools. I specialize in test automation in dynamic environments, compensating for resource limitations through innovative architectures and optimizing value delivery with full technical autonomy.

== Experience

#regular-entry(
  [
    #strong[OneVisa - Dubai (UAE) \/ Spain], (Part-time) Senior Principal QA Engineer (AI & Reliability)

    - Sole QA engineer in high-growth startup: designed and implemented the end-to-end testing and reliability strategy from scratch.

    - Deployed autonomous QA Agent to production (Claude Code) for E2E testing and continuous product evolution without operational overhead.

    - Implemented self-diagnostic pipelines and DORA metrics, scaling technical coverage with minimal headcount.

  ],
  [
    Feb 2026 – Aug 2026

    

    7 months

  ],
)

#regular-entry(
  [
    #strong[Tata Consultancy Service - Banco Galicia], SSR QA Automation Engineer

    - QA Automation (App, Web & API) in Tools & Data Tribe & AI Ambassador (AI Hub): Mobile App automation (Android\/iOS) using AI agents via the new KrakenQA project in VS Code, and Web\/API testing with Tricentis TOSCA.

    - Promoted to SSR following progression in Onboarding and technical testing in Retail Transfers on the critical mobile banking app.

    - Co-creator of CobroTron & FullTron: pioneered filtered-DOM auto-debugging pattern, POM suite generation, and unattended ALM sync.

  ],
  [
    Apr 2023 – present

    

    3 years 6 months

  ],
)

#regular-entry(
  [
    #strong[Ada School - Colombia], Python Instructor (Data & FullStack BootCamp)

    - Advanced technical mentorship in Python focused on code quality, software architecture, and development best practices for international profiles.

  ],
  [
    Sept 2023 – Oct 2024

    

    1 year 2 months

  ],
)

== Education

#education-entry(
  [
    #strong[National University of Hurlingham]

    #emph[University Technician] in Artificial Intelligence

  ],
  [
    Jan 2024 – present

  ],
)

#education-entry(
  [
    #strong[Teacher Training Institute N°109]

    #emph[Secondary Education Professor] in Economics and Management

    - Last year pending

  ],
  [
    Mar 2019 – Dec 2023

  ],
)

== Skills

#strong[AI & Agents:] Claude Code, Gemini, DeepSeek, Scikit-learn, GitHub Copilot, Cursor, Antigravity, Engram, Prompt Engineering, OpenAI, Anthropic, Pandas, NumPy

#strong[Testing & QA:] Tricentis Tosca, Playwright, Cypress, Selenium, Appium, Pytest, k6 (Performance), Postman, Bruno

#strong[Dev & Ops:] Python, TypeScript, JavaScript, Java, Node.js, FastAPI, Flask, AWS, Docker, Jenkins, Linux, Bash, CI\/CD

#strong[Observability & Data:] Grafana, Kibana, SQL, NoSQL, Matplotlib, Seaborn, Trace\/Log Analysis, GitHub Actions

#strong[Languages:] Spanish, English

== Projects

#regular-entry(
  [
    #strong[Zenco.arg (In Prod)]

    - React 18 · Node.js · AI WhatsApp Bot · Gemini AI

  ],
  [
  ],
)

#regular-entry(
  [
    #strong[El Industrial (In Prod)]

    - Python · Vanilla JS · API REST · Telegram Bot · IA Reporting

  ],
  [
  ],
)

#regular-entry(
  [
    #strong[Portfolio CV (Live)]

    - JSON Resume · Astro · RenderCV (ATS Friendly) · i18n · Advanced Dark Mode

  ],
  [
  ],
)
