import { test, expect } from '@playwright/test';

test('Saucedemo E2E flow generated via codegen', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.getByPlaceholder('Username').click();
  await page.getByPlaceholder('Username').fill('standard_user');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('secret_sauce');
  await page.getByRole('button', { name: 'Login' }).click();

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
