// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Jorge Tricarico",
  title: "Jorge Tricarico - CV",
  footer: context { [#emph[Jorge Tricarico -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Última actualización Abr 2026] ],
  locale-catalog-language: "es",
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
    day: 24,
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


== Resumen

Ingeniero de QA y Especialista en IA enfocado en la creación de producto y la confiabilidad del software. Cuento con un perfil técnico full-stack que potencio mediante el uso avanzado de LLMs y herramientas agenticas. Me especializo en liderar la automatización en entornos dinámicos, compensando limitaciones de recursos mediante arquitecturas innovadoras y optimizando la entrega de valor con total autonomía técnica.

== Experiencia

#regular-entry(
  [
    #strong[OneVisa - Dubai (UAE) \/ España], (Part-time) Senior Principal QA Engineer (AI & Reliability)

    - Único responsable de QA en una startup en fase de alto crecimiento, liderando el diseño y la ejecución de la estrategia integral de automatización desde cero.

    - Escalabilidad de la cobertura de pruebas sin ampliar la plantilla, compensando la falta de recursos humanos mediante la creación y orquestación de agentes de IA con Claude Code.

    - Implementación de sistemas de autodiagnóstico iterativos en los pipelines, reduciendo los tiempos de debugging y permitiendo una integración técnica profunda con el equipo de ingeniería.

  ],
  [
    Feb 2026 – presente

    

    3 meses

  ],
)

#regular-entry(
  [
    #strong[Tata Consultancy Service - Banco Galicia], Analista QA Manual - Automation

    - Diseño y desarrollo de 'CobroTron', un agente de IA propio integrado en VSC Github Copilot, especializado en acelerar fuertemente la generación de scripts de automatización para flujos web utilizando Playwright y Python.

    - Construcción de 'FullTron', la máxima evolución de agente QA con autodiagnóstico pionero para iterar tests de forma autónoma. Genera frameworks completos (POM) E2E para Apps nativas\/React (Appium + BrowserStack), APIs y Web; subiendo métricas de Pass\/Fail y evidencia de forma automática al sistema ALM.

    - Gestión técnica ágil del ciclo de pruebas y análisis de traces\/logs, colaborando cercanamente con desarrolladores mediante la optimización de infraestructura y queries (SQL\/NoSQL).

  ],
  [
    Abr 2023 – presente

    

    3 años 1 mes

  ],
)

#regular-entry(
  [
    #strong[Ada School - Colombia], Profesor Python (BootCamp Data y FullStack)

    - Mentoría técnica avanzada en Python enfocada en la calidad del código, arquitectura de software y mejores prácticas de desarrollo para perfiles internacionales.

  ],
  [
    Sep 2023 – Oct 2024

    

    1 año 2 meses

  ],
)

== Educación

#education-entry(
  [
    #strong[Universidad Nacional de Hurlingham]

    #emph[Tec. Universitaria] en Inteligencia Artificial

  ],
  [
    Ene 2024 – presente

  ],
)

#education-entry(
  [
    #strong[Instituto Superior de Formación Docente N°109]

    #emph[Prof. de Educación Secundaria] en Economía y Gestión

    - Adeudo último año

  ],
  [
    Mar 2019 – Dic 2023

  ],
)

== Habilidades

#strong[IA & Agentes:] Claude Code, Gemini, DeepSeek, GitHub Copilot, Cursor, Antigravity, Engram, Prompt Engineering, OpenAI, Anthropic

#strong[Testing & QA:] Playwright, Cypress, Selenium, Appium, Pytest, k6 (Performance), Postman, Bruno

#strong[Dev & Ops:] Python, TypeScript, JavaScript, Java, Node.js, FastAPI, AWS, Docker, Jenkins

#strong[Observabilidad & Data:] Grafana, Kibana, SQL, NoSQL, Análisis de Traces\/Logs, GitHub Actions

#strong[Idiomas:] Español, Inglés
