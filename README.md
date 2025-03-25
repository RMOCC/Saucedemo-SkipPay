1. Automatizace uživatelské cesty Python/Selenium ✅


2. Implementace do CI/CD pipeline ✅


3. Analýza chyb a jejich dopadu
                              Title: API endpoint /checkout vrací 500 Internal Server Error při finalizaci objednávky
                                 Type: Bug
                                 Priority: High
                                 Reported by: Automation Tester
                                 Environment: https://www.saucedemo.com/api/checkout
                                 Description: Během automatizovaného E2E testu byla detekována chyba na API endpointu /checkout. Server vrací chybový kód 500 Internal Server Error při pokusu o dokončení objednávky. Testovací scénář "Complete Purchase Flow" selhal v kroku "Submit checkout".
                                 Steps to Reproduce (simulace): Přihlášení jako standard_user, Přidání zboží do košíku, Přechod na checkout, Odeslání POST requestu na /api/checkout, Server vrátí: HTTP/1.1 500 Internal Server Error
                                 Test Failure Message (Log): Expected status 200 but received 500, POST /api/checkout, Response: Internal Server Error
                                 Příloha: Logy z testu, Screenshot chyby (případně přiložit .har z manualni verze testu)


5. Kritické cesty a jejich pokrytí ✅

      Přihlášení do aplikace - Uživatel se bez úspěšného přihlášení nedostane k funkcím aplikace.
                               Chyby při přihlášení mohou způsobit frustraci nebo znemožnit nákup.
                             - Ověřit správné přihlášení pomocí platných přihlašovacích údajů.
                               Otestovat chybové stavy (např. nesprávné heslo, neexistující uživatel).
                               Ověřit, že po úspěšném přihlášení je uživatel přesměrován na správnou stránku.
                               Simulovat nečekané chování (např. pomalé načítání stránky, výpadek serveru).
      E2E Přidání produktu do košíku a dokončení objednávky
                             - Jde o hlavní obchodní funkci e-shopu.
                               Chyby mohou způsobit ztrátu zákazníků a příjmů
                             - Ověřit, že uživatel může přidat produkt do košíku a že je správně zobrazen.
                               Simulovat přidání více produktů a zkontrolovat celkovou cenu.
                               Otestovat proces dokončení objednávky (vyplnění formuláře, platba).
                               Simulovat různé chybové scénáře (např. vyprodáno, pomalá odezva serveru).
      Odhlášení uživatele    - Odhlášení je důležité pro bezpečnost uživatele ( delete session )
                               Chyba může vést k nechtěnému sdílení účtu s jinými uživateli ( treba u sdileneho PC )
                             - Ověřit, že fce pro odhlášení funguje správně.
                               Zkontrolovat, zda po odhlášení není možné přistupovat k chráněným stránkám.
                               Simulovat různé scénáře (např. rychlé přepínání mezi účty).


7. Mentoring úkol  ✅          

                              1. Základní knihovny
                              Používej tyto knihovny: from selenium import webdriver
                                                      from selenium.webdriver.common.by import By
                                                      from selenium.webdriver.support.ui import WebDriverWait
                                                      from selenium.webdriver.support import expected_conditions as EC
                                                      from webdriver_manager.chrome import ChromeDriverManager

                                                      webdriver_manager` ti **automaticky stáhne správný ChromeDriver

                              2. Správné vyhledávání prvků (příklad z našeho PageObject)
                                                      Vždy používej By.ID, By.CLASS_NAME, By.CSS_SELECTOR:

                                                      self.driver.find_element(By.ID, "user-name").send_keys("standard_user")

                                                      Nepoužívej složité XPATH, když máš ID nebo data-test!


                              3. Používej `WebDriverWait` — zamezí chybám načtení
                                                      Správně čekáme na prvek v našem testu:
                                                      self.wait.until(EC.element_to_be_clickable(self.saucedemo_page.login_button.locator)).click()
                                                      Čekáme na **kliknutelnost** — nepadne ti to na "element not found"

                              4. `driver.quit()` na konci testu 
                                                      V našem testu máme clean-up:
                                                      def teardown(self):
                                                      logging.info("Tearing down browser")
                                                      self.browser.quit()

                                                      Tím se zavře prohlížeč— nezůstane ti viset proces

                              5. Používej Page Object Model (POM) 
                                                      Příklad naší `SaucedemoPage`:
                                                      class SaucedemoPage:
                                                          def __init__(self, driver):
                                                          self.driver = driver

                                                      @property
                                                          def login_button(self):
                                                                return self.driver.find_element(By.ID, "login-button")

                                                      Test je přehledný — test volá:
                                                      self.saucedemo_page.login_button.click()


                              6. Automatické stahování driveru            
                                                      V našem `drivers.py`:
                                                      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

                                                       Nehraješ si ručně s chromedriverem** — řeší `webdriver_manager`

                              7.Nejčastější chyby juniorů (naše skripty se jim vyhýbají!)**
                                                      Chybí `driver.quit()`  
                                                      Chybí `WebDriverWait` → "element not found"  
                                                      Používají absolutní XPATH  
                                                      Vše v jednom scripťáku bez struktury

  
                              "Začni jednoduše, přidej složitost až postupně."  
                              "Vždy přemýšlej, jestli test simuluje reálného uživatele."


9. Dokumentace k spusteni testu Python & Playwright  ✅

                              Jak spustit testovací scénář:

                               Přihlas se do GitHub repozitáře
                               Klikni na záložku "Actions"
                               Vyber workflow "Python and Playwright Tests"
                               Klikni na "Run workflow"
                               Vyber branch (většinou main) a potvrď
                               Sleduj běh pipeline v job logu
                               Výsledek uvidíš v Actions logu


10. CI/CD konfigurace      ✅
                               
   

11. Playwright automatizace  ✅

   
# skippay
