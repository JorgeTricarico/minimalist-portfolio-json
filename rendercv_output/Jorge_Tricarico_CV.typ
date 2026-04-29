// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Jorge Tricarico",
  title: "Jorge Tricarico - CV",
  footer: context { [#emph[Jorge Tricarico -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Last updated in Apr 2026] ],
  locale-catalog-language: "en",
  text-direction: ltr,
  page-size: "a4",
  page-top-margin: 1.5cm,
  page-bottom-margin: 1.5cm,
  page-left-margin: 1.5cm,
  page-right-margin: 1.5cm,
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
  typography-font-size-body: 9.5pt,
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
  header-space-below-name: 0.4cm,
  header-space-below-headline: 0.4cm,
  header-space-below-connections: 0.5cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.5cm,
  section-titles-type: "with_partial_line",
  section-titles-line-thickness: 0.5pt,
  section-titles-space-above: 0.5cm,
  section-titles-space-below: 0.3cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.5em,
  sections-space-between-regular-entries: 1em,
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
    month: 4,
    day: 29,
  ),
)


#grid(
  columns: (auto, 1fr),
  column-gutter: 0cm,
  align: horizon + left,
  [#pad(left: 0.4cm, right: 0.4cm, image("perfil.jpg", width: 3.5cm))
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

QA Engineer and AI Specialist focused on product creation and software reliability. I have a full-stack technical profile that I leverage through the advanced use of LLMs and agentic tools. I specialize in leading automation in dynamic environments, compensating for resource limitations through innovative architectures and optimizing value delivery with full technical autonomy.

== Experience

#regular-entry(
  [
    #strong[OneVisa - Dubai (UAE) \/ Spain], (Part-time) Senior Principal QA Engineer (AI & Reliability)

    - Solely responsible for QA in a high-growth startup, leading the design and execution of the end-to-end automation strategy from scratch.

    - Scalability of test coverage without increasing headcount, compensating for human resource gaps by creating and orchestrating AI agents with Claude Code.

    - Implementation of iterative self-diagnostic systems in pipelines, reducing debugging times and allowing deep technical integration with the engineering team.

  ],
  [
    Feb 2026 – present

    

    3 months

  ],
)

#regular-entry(
  [
    #strong[Tata Consultancy Service - Banco Galicia], Manual QA Analyst - Automation

    - Design and development of 'CobroTron', a proprietary AI agent integrated into VSC Github Copilot, specialized in significantly accelerating automation script generation for web flows using Playwright and Python.

    - Construction of 'FullTron', the ultimate evolution of a QA agent with pioneering self-diagnosis to iterate tests autonomously. It generates complete E2E frameworks (POM) for native Apps\/React (Appium + BrowserStack), APIs, and Web; automatically uploading Pass\/Fail metrics and evidence to the ALM system.

    - Agile technical management of the testing cycle and trace\/log analysis, working closely with developers by optimizing infrastructure and queries (SQL\/NoSQL).

  ],
  [
    Apr 2023 – present

    

    3 years 1 month

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

#strong[AI & Agents:] Claude Code, Gemini, DeepSeek, GitHub Copilot, Cursor, Antigravity, Engram, Prompt Engineering, OpenAI, Anthropic, Scikit-learn, Pandas, NumPy

#strong[Testing & QA:] Playwright, Cypress, Selenium, Appium, Pytest, k6 (Performance), Postman, Bruno

#strong[Dev & Ops:] Python, TypeScript, JavaScript, Java, Node.js, FastAPI, Flask, AWS, Docker, Jenkins, Linux, Bash, CI\/CD

#strong[Observability & Data:] Grafana, Kibana, SQL, NoSQL, Matplotlib, Seaborn, Trace\/Log Analysis, GitHub Actions

#strong[Languages:] Spanish, English
