import { Page } from '@playwright/test';

export class CheckoutPage {
  constructor(private page: Page) {}

  async checkoutInfo(first: string, last: string, zip: string) {
    await this.page.getByPlaceholder('First Name').fill(first);
    await this.page.getByPlaceholder('Last Name').fill(last);
    await this.page.getByPlaceholder('Zip/Postal Code').fill(zip);
    await this.page.getByRole('button', { name: 'Continue' }).click();
  }

  async finish() {
    await this.page.getByText('Checkout: Overview').isVisible();
  }
}
