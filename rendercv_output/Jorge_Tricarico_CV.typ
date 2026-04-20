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
    day: 20,
  ),
)


#grid(
  columns: (auto, 1fr),
  column-gutter: 0cm,
  align: horizon + left,
  [#pad(
  left: 0.4cm, 
  right: 0.4cm, 
  box(
    width: 3.5cm,
    height: 3.5cm,
    radius: 50%, 
    clip: true, 
    image("perfil.jpg", width: 100%, height: 100%, fit: "cover")
  )
)
],
  [
= Jorge Tricarico

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

Especialista en #strong[IA] y #strong[QA] con un enfoque orientado a la ingeniería de software y la creación de producto. Cuento con una sólida base técnica potenciada por el uso estratégico de modelos de lenguaje, lo que me permite abordar con autonomía tareas de desarrollo funcional y arquitectura técnica. Perfil adaptable e innovador, enfocado en optimizar la entrega de valor mediante herramientas agentic y un aprendizaje constante.

== Experiencia

#regular-entry(
  [
    #strong[#emph[#sym.ast.basic#h(0pt, weak: true) OneVisa]#sym.ast.basic - Dubai (UAE) \/ España], (Part-time) #strong[Senior] #strong[QA] Engineer (AI & Reliability)

    - Desempeño de un #strong[rol pionero y disruptivo] en el campo de la #strong[IA] #strong[Agentic], definiendo nuevos paradigmas de validación de software mediante la orquestación recursiva de agentes inteligentes.

    - Desarrollo y refinamiento constante de agentes especializados mediante #strong[#emph[#sym.ast.basic#h(0pt, weak: true) Claude Code]]#sym.ast.basic#h(0pt, weak: true) , optimizando la confiabilidad del software a través de una interacción avanzada humano-agente.

    - Implementación de sistemas de autodiagnóstico iterativos que maduran con el producto, permitiendo una colaboración técnica profunda con el equipo de ingeniería.

  ],
  [
    Feb 2026 – presente

    

    3 meses

  ],
)

#regular-entry(
  [
    #strong[Tata Consultancy Service - ]Banco Galicia#strong[#emph[#sym.ast.basic#h(0pt, weak: true) , Analista ]#sym.ast.basic#h(0pt, weak: true) QA] Manual - Automation

    - Desarrollo de un agente de #strong[IA] para VS Code Copilot enfocado en acelerar la generación de pruebas y mejorar la sincronización técnica con el equipo de desarrollo.

    - Automatización de servicios críticos (APIs, Web, Mobile) con un perfil técnico capaz de validar la lógica de negocio directamente en el código fuente.

    - Gestión técnica del ciclo de vida de pruebas, colaborando estrechamente con desarrolladores mediante análisis de logs y optimización de bases de datos SQL\/NoSQL.

  ],
  [
    Abr 2023 – presente

    

    3 años 1 mes

  ],
)

#regular-entry(
  [
    #strong[Ada School - Colombia], Profesor #strong[Python] (BootCamp Data y FullStack)

    - Mentoría técnica avanzada en #strong[Python] enfocada en la calidad del código, arquitectura de software y mejores prácticas de desarrollo para perfiles internacionales.

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

#strong[#emph[#sym.ast.basic#h(0pt, weak: true) IA]#sym.ast.basic & Agentes:] #strong[Claude Code], GitHub Copilot, Prompt Engineering, Arquitectura de Agentes, LLMs (Anthropic, OpenAI)

#strong[Core Testing:] #strong[Playwright], Selenium, Pytest, Automatización de APIs, Diagnósticos #strong[IA], OCR Validation

#strong[Lenguajes:] #strong[Python] (Avanzado), #strong[TypeScript], Java

#strong[Cloud & Infra:] Docker, Supabase, Linux\/Bash, CI\/CD, Jenkins, OpenShift

#strong[Idiomas:] Español (Nativo), Inglés (Intermedio)
