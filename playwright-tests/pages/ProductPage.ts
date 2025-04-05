import { Page } from '@playwright/test';

export class ProductPage {
  constructor(private page: Page) {}

  async isVisible() {
    await this.page.getByText('Products').isVisible();
  }

  async goToJacket() {
    await this.page.locator('[data-test="item-5-title-link"]').click();
  }

  async addToCart() {
    await this.page.getByRole('button', { name: 'Add to cart' }).click();
  }

  async openCart() {
    await this.page.locator('.shopping_cart_link').click();
  }
}
