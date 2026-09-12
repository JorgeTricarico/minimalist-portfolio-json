import { describe, it, expect } from 'vitest';
import { getIconUrl } from './download_icons.js';

describe('getIconUrl', () => {
  it('should return the correct icon URL for logo matches', () => {
    expect(getIconUrl('JavaScript')).toBe('https://api.iconify.design/logos:javascript.svg');
    expect(getIconUrl(' TypeScript ')).toBe('https://api.iconify.design/logos:typescript-icon.svg');
    expect(getIconUrl('python')).toBe('https://api.iconify.design/logos:python.svg');
    // playwright and cypress are actually in the logos dictionary
    expect(getIconUrl('playwright')).toBe('https://api.iconify.design/logos:playwright.svg');
    expect(getIconUrl('cypress')).toBe('https://api.iconify.design/logos:cypress-icon.svg');
  });

  it('should return the correct icon URL for simple icon matches', () => {
    expect(getIconUrl('appium')).toBe('https://cdn.simpleicons.org/appium');
    expect(getIconUrl('pytest')).toBe('https://cdn.simpleicons.org/pytest');
  });

  it('should handle custom colored simple icons', () => {
    expect(getIconUrl('gemini')).toBe('https://api.iconify.design/simple-icons:googlegemini.svg?color=%231A73E8');
    expect(getIconUrl('scikit-learn')).toBe('https://api.iconify.design/simple-icons:scikitlearn.svg?color=%23F89939');
    expect(getIconUrl('claude')).toBe('https://api.iconify.design/simple-icons:anthropic.svg?color=%23191919');
    expect(getIconUrl('anthropic')).toBe('https://api.iconify.design/simple-icons:anthropic.svg?color=%23191919');
  });

  it('should handle specific deepseek case', () => {
    expect(getIconUrl('deepseek')).toBe('https://api.iconify.design/logos:deepseek-icon.svg');
  });

  it('should return fallback icons for common patterns', () => {
    // nosql matches "nosql" in simple which resolves to mongodb
    expect(getIconUrl('NoSQL DB')).toBe('https://cdn.simpleicons.org/mongodb');
    // mysql is in logos, but 'My SQL' is handled by simple SQL which is postgresql
    expect(getIconUrl('My SQL')).toBe('https://cdn.simpleicons.org/postgresql');
    expect(getIconUrl('Bot')).toBe('https://api.iconify.design/lucide:bot.svg');
    expect(getIconUrl('agente')).toBe('https://api.iconify.design/lucide:bot.svg');
    expect(getIconUrl('engram')).toBe('https://api.iconify.design/ph:brain-duotone.svg');
    expect(getIconUrl('Logs')).toBe('https://api.iconify.design/lucide:file-search.svg');
    expect(getIconUrl('Inglés')).toBe('https://api.iconify.design/lucide:languages.svg');
    expect(getIconUrl('CI/CD')).toBe('https://api.iconify.design/lucide:infinity.svg');
    expect(getIconUrl('Performance')).toBe('https://api.iconify.design/lucide:gauge.svg');
  });

  it('should return the default code icon for unmatched terms', () => {
    expect(getIconUrl('Random Skill')).toBe('https://api.iconify.design/lucide:code-2.svg');
  });
});
