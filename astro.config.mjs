import { defineConfig } from 'astro/config';
import path from 'path';

// Run `npm install @astrojs/sitemap` then uncomment:
// import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://jorgetricarico.com',
  // integrations: [sitemap({ i18n: { defaultLocale: 'es', locales: { es: 'es-AR', en: 'en-US' } } })],
  vite: {
    resolve: {
      alias: {
        '@cv': path.resolve('./cv.json'),
        '@': path.resolve('./src')
      }
    }
  }
});
