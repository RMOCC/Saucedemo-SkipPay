import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  retries: 0,
  use: {
    headless: true,
    screenshot: 'only-on-failure', // ⬅️ Automatický screenshot při selhání
    video: 'retain-on-failure',    // ⬅️ Volitelné: zachová video při selhání
    trace: 'retain-on-failure',    // ⬅️ Volitelné: trace report
  },
});
