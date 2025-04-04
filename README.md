1. Playwright automatizace  ✅

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





6. CI/CD konfigurace      ✅
                               
   



   
