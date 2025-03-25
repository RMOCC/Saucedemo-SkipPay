1. Automatizace uživatelské cesty Python/Selenium ✅


2. Implementace do CI/CD pipeline ✅


3. Analýza chyb a jejich dopadu


4. Kritické cesty a jejich pokrytí ✅

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


7. Mentoring úkol

8. Dokumentace k spusteni testu Python & Playwright  ✅

                              Jak spustit testovací scénář:

                               Přihlas se do GitHub repozitáře
                               Klikni na záložku "Actions"
                               Vyber workflow "Python and Playwright Tests"
                               Klikni na "Run workflow"
                               Vyber branch (většinou main) a potvrď
                               Sleduj běh pipeline v job logu
                               Výsledek uvidíš v Actions logu


9. CI/CD konfigurace      ✅
                               
   

11. Playwright automatizace  ✅

   
# skippay
