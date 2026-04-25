import { defineConfig } from 'astro/config';
import path from 'path';

// https://astro.build/config
export default defineConfig({
  vite: {
    resolve: {
      alias: {
        '@cv': path.resolve('./cv.json'),
        '@': path.resolve('./src')
      }
    }
  }
});
