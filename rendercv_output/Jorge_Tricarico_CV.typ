// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.3.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Jorge Tricarico",
  title: "Jorge Tricarico - CV",
  footer: context { [#emph[Jorge Tricarico -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Última actualización Oct 2026] ],
  locale-catalog-language: "es",
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
  header-space-below-name: 0.35cm,
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
    month: 10,
    day: 6,
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

  #headline([AI Engineer | Agentic Systems & Software Architecture])

#connections(
  [#connection-with-icon("location-dot")[Buenos Aires, AR]],
  [#link("mailto:jorge.tricarico@gmail.com", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[jorge.tricarico\@gmail.com]]],
  [#link("tel:+54-9-11-5047-9769", icon: false, if-underline: false, if-color: false)[#connection-with-icon("phone")[011 15-5047-9769]]],
  [#link("https://jorge-tricarico.onrender.com/?utm_source=cv&utm_medium=pdf&utm_campaign=resume_apply", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[jorge-tricarico.onrender.com]]],
  [#link("https://linkedin.com/in/jorge-tricarico", icon: false, if-underline: false, if-color: false)[#connection-with-icon("linkedin")[jorge-tricarico]]],
  [#link("https://github.com/JorgeTricarico", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[JorgeTricarico]]],
)
  ]
)


== Resumen

AI Engineer especializado en el diseño e implementación de sistemas agénticos, automatización de procesos y arquitecturas basadas en LLMs. Combino una sólida base técnica en desarrollo y calidad de software para construir agentes de IA modulares, confiables y orientados a resolver flujos de negocio complejos en producción.

== Experiencia

#regular-entry(
  [
    #strong[Tata Consultancy Service - Banco Galicia]

    - #strong[AI Engineer (Hub de IA)] (#emph[Oct 2026 – presente])

    - Arquitectura y evolución de agentes de IA: líder institucional en adopción y ejecuciones para orquestación y automatización de flujos de negocio.

    - Integración ágil en Comercio Exterior: diseño e implementación de arquitectura modular para ComEx en menos de una semana.

    - Auditoría y gobernanza técnica de agentes de IA, evaluación de agentes y consultoría transversal a squads.

    - #strong[SSR QA Automation Engineer (Área de Calidad)] (#emph[Feb 2026 – Oct 2026])

    - QA Automation transversal: diseño y ejecución de pruebas E2E multi-plataforma (Web, APIs, Mobile y Desktop) con Tricentis TOSCA institucional.

    - Proyecto \"Kraken Mobile\": desarrollo de agente de IA para pruebas en Apps móviles (Android\/iOS) acelerando regresiones.

    - #strong[Analista QA Manual & Automation] (#emph[Abr 2023 – Feb 2026])

    - Testing técnico y aseguramiento de calidad sobre Onboarding y Transferencias en la app móvil transaccional crítica.

    - Co-creador de CobroTron y FullTron: herramientas pioneras de auto-debug por DOM filtrado y sincronización con ALM.

  ],
  [
    Abr 2023 – presente

    

    3 años 7 meses

  ],
)

#regular-entry(
  [
    #strong[OneVisa - Dubai (UAE) \/ España], (Part-time) Senior Principal QA Engineer (AI & Reliability)

    - Único responsable de QA en startup de alto crecimiento: diseño e implementación de la estrategia integral de testing y confiabilidad desde cero.

    - Implementación de Agente QA autónomo en producción (Claude Code) y pipelines con autodiagnóstico iterativo y métricas DORA.

  ],
  [
    Feb 2026 – Ago 2026

    

    7 meses

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

#strong[IA & Agentes:] Claude Code, Gemini, DeepSeek, Scikit-learn, GitHub Copilot, Cursor, Antigravity, Engram, Prompt Engineering, OpenAI, Anthropic, Pandas, NumPy

#strong[Testing & QA:] Tricentis Tosca, Playwright, Cypress, Selenium, Appium, Pytest, k6 (Performance), Postman, Bruno

#strong[Dev & Ops:] Python, TypeScript, JavaScript, Java, Node.js, FastAPI, Flask, AWS, Docker, Jenkins, Linux, Bash, CI\/CD

#strong[Observabilidad & Data:] Grafana, Kibana, SQL, NoSQL, Matplotlib, Seaborn, Análisis de Traces\/Logs, GitHub Actions

#strong[Idiomas:] Español, Inglés

== Proyectos

#regular-entry(
  [
    #strong[Zenco.arg (En Prod)]

    - React 18 · Node.js · AI WhatsApp Bot · Gemini AI

  ],
  [
  ],
)

#regular-entry(
  [
    #strong[El Industrial (En Prod)]

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
