import { Page } from '@playwright/test';

export class Menu {
  constructor(private page: Page) {}

  async logout() {
    await this.page.getByRole('button', { name: 'Open Menu' }).click();
    await this.page.getByRole('link', { name: 'Logout' }).click();
  }
}
