import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { ProductPage } from '../pages/ProductPage';
import { CheckoutPage } from '../pages/CheckoutPage';
import { Menu } from '../pages/Menu';

test('Saucedemo E2E flow (POM)', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const productPage = new ProductPage(page);
  const checkoutPage = new CheckoutPage(page);
  const menu = new Menu(page);

  await loginPage.goto();
  await loginPage.login(process.env.SAUCE_USERNAME!, process.env.SAUCE_PASSWORD!);

  await productPage.isVisible();
  await productPage.goToJacket();
  await productPage.addToCart();
  await productPage.openCart();
  await expect(page.getByText('Sauce Labs Fleece Jacket')).toBeVisible();

  await page.getByRole('button', { name: 'Checkout' }).click();
  await checkoutPage.checkoutInfo('Jan', 'Novak', '10400');
  await checkoutPage.finish();

  await menu.logout();
  await expect(page.getByRole('button', { name: 'Login' })).toBeVisible();
});
