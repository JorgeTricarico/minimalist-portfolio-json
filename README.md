# 🚀 AI-Driven & Multilingual Portfolio

Este es un portafolio/CV minimalista, elegante y altamente funcional, diseñado específicamente para ingenieros de software y QA que buscan destacar su perfil técnico tanto en la web como en PDF.

**Basado en el trabajo original de [midudev](https://github.com/midudev/minimalist-portfolio-json)**, este fork ha evolucionado para incluir capacidades avanzadas de automatización e internacionalización.

---

## ✨ Características Destacadas

- 🌍 **Soporte Multilingüe (ES/EN)**: Cambio dinámico de idioma con un switch premium con Glassmorphism.
- 📄 **PDF Dual Automatizado**: Generación de currículums profesionales en ambos idiomas mediante [RenderCV](https://github.com/sina-ariyan/rendercv) y LaTeX.
- 🤖 **Perfil AI-Focused**: Optimizado para resaltar habilidades en IA, Agentes y Automatización de QA.
- 🌑 **Modo Oscuro Inteligente**: Sincronizado entre sesiones y con efectos de brillo (Glow) dinámicos.
- ⚡ **Astro + TypeScript**: Rendimiento ultrarrápido y código 100% tipado.
- ⌨️ **Keyboard Friendly**: Atajos de teclado intuitivos (`Ctrl+K`) para acciones rápidas.

---

## 🛠️ Stack Tecnológico

- **Frontend**: [Astro](https://astro.build/), [TypeScript](https://www.typescriptlang.org/), CSS Nativo.
- **Data**: YAML como fuente de verdad, convertido automáticamente a JSON Resume.
- **PDF Engine**: [RenderCV](https://rendercv.com/) (LaTeX).
- **Interacción**: [HotKeyPad](https://github.com/ssleptsov/ninja-keys) para el gestor de comandos.

---

## 🧞 Comandos y Desarrollo

A diferencia del template original, este proyecto incluye scripts de automatización personalizados:

| Comando | Acción |
| :--- | :--- |
| `npm run dev` | Lanza el servidor y sincroniza los archivos YAML/JSON automáticamente. |
| `npm run cv` | Genera los PDFs en Español e Inglés desde los archivos YAML. |
| `npm run build` | Valida tipos y genera el bundle estático para producción. |

### Cómo usar tu propio contenido
1. Edita `cv.yaml` (Español) y `cv.en.yaml` (Inglés).
2. Ejecuta `npm run cv` para actualizar los PDFs en `public/`.
3. El sitio web se actualizará automáticamente reflejando los cambios.

---

## 📝 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). 
Inspirado por [Bartosz Jarocki](https://github.com/BartoszJarocki/cv) y adaptado por [midudev](https://midu.dev).
**Mejorado y extendido por Jorge Tricarico.**
