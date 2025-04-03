import { test, expect, Page } from '@playwright/test';
import * as dotenv from 'dotenv';
dotenv.config();


async function loginToSaucedemo(page) {
  const username = process.env.SAUCE_USERNAME;
  const password = process.env.SAUCE_PASSWORD;

  if (!username || !password) {
    throw new Error('Chybí SAUCE_USERNAME nebo SAUCE_PASSWORD v .env souboru');
  }

  await page.goto('https://www.saucedemo.com/');
  await page.getByPlaceholder('Username').fill(username);
  await page.getByPlaceholder('Password').fill(password);
  await page.getByRole('button', { name: 'Login' }).click();

 // await handleRandomPopup(page);


  /* Zkusit zavřít případný pop-up po přihlášení
  await handleRandomPopup(page);
  */
}

test('Saucedemo E2E flow', async ({ page }) => {
  await loginToSaucedemo(page);

  await page.getByText('Products').isVisible();

  // Navigate to Sauce Labs Fleece Jacket
  await page.locator('[data-test="item-5-title-link"]').click();

  // Add to cart
  await page.getByRole('button', { name: 'Add to cart' }).click();

  // Go to cart
  await page.locator('.shopping_cart_link').click();
  await page.getByRole('heading', { name: 'Your Cart' }).isVisible();
  await expect(page.getByText('Sauce Labs Fleece Jacket')).toBeVisible();

  // Checkout
  await page.getByRole('button', { name: 'Checkout' }).click();

  // Fill out checkout info
  await page.getByPlaceholder('First Name').fill('Jan');
  await page.getByPlaceholder('Last Name').fill('Novak');
  await page.getByPlaceholder('Zip/Postal Code').fill('10400');
  await page.getByRole('button', { name: 'Continue' }).click();

  // Overview and finish
  await page.getByText('Checkout: Overview').isVisible();
  await expect(page.getByText('Sauce Labs Fleece Jacket')).toBeVisible();

  // Logout
  await page.getByRole('button', { name: 'Open Menu' }).click();
  await page.getByRole('link', { name: 'Logout' }).click();
  await expect(page.getByRole('button', { name: 'Login' })).toBeVisible();
});

// Simulace funkce na zavření pop-upu – tu si přizpůsob podle potřeby
  async function handleRandomPopup(page: Page) {
  // Pokud existuje nějaký pop-up, tady ho můžeš zkusit zavřít
  // await page.locator('selector-na-popup-close-button').click({ timeout: 1000 }).catch(() => {});
}
