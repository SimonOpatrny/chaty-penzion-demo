# MEZI LESY — prémiový DEMO web pro pronájem chat

**Jde o fiktivní koncept.** Žádné skutečné ubytování zde nelze rezervovat. Adresy, reference a skutečná obsazenost nejsou uváděny.

## Spuštění
Otevřete `index.html` v moderním prohlížeči. Není třeba instalovat Node, framework ani server.

## Funkce
- Responzivní design s mobilním menu a jemnými scroll animacemi.
- Tři ilustrativní typy ubytování, karty a interaktivní výběr.
- Galerie skutečných fotografií Pexels: filtry kategorií, prohlížeč fotografií, klávesy ← → a Esc.
- Rozsáhlý demonstrační ceník (20 položek).
- Kalkulačka podle typu ubytování, počtu nocí, kapacity, domácích mazlíčků, snídaně, dřeva a pozdního odjezdu.
- Sleva 10 % při 4+ nocích ze základní ceny ubytování.
- Validovaný DEMO formulář a informační dialog. Data se nikam neodesílají.
- Sémantické HTML, atributy aria, alt texty, lazy-loading a podpora prefers-reduced-motion.

## Nahrání na GitHub Pages
1. Rozbalte ZIP a vložte **obsah složky `mezi-lesy/`** do kořene nového repozitáře na GitHubu (nebo ponechte podsložku a nastavte publikování odpovídajícím způsobem).
2. V repozitáři otevřete **Settings → Pages → Build and deployment → Deploy from a branch**.
3. Zvolte větev `main`, složku `/ (root)` a potvrďte **Save**.
4. Po publikování otevřete URL svého GitHub Pages webu. Všechny obrázky používají relativní cesty `assets/images/...`.

## Fotografie
Seznam původu jednotlivých fotografií viz `FOTO-ZDROJE.txt`. Fotografie jsou **ilustrační**, nezobrazují skutečnou realizaci žádné fiktivní chaty. Autorství fotografií náleží jejich autorům. Licence Pexels: https://www.pexels.com/license/.

## Úpravy
V `app.js` lze změnit ceny a kapacity (`houses`) i položky ceníku (`rateItems`). V `styles.css` jsou barvy v CSS proměnných na začátku souboru. Kontaktní část je záměrně pouze DEMO a nevytváří žádné rezervace.

## Instalace fotografií (nutné kvůli omezení přenosu mezi archivy)
Soubor `FOTOGRAFIE-ODKAZ.txt` obsahuje archiv 28 stažených, optimalizovaných fotografií WebP. Po stažení fotobalíčku rozbalte všech 28 souborů `.webp` do `assets/images/` a soubor `FOTO-ZDROJE.txt` do kořene projektu. Alternativně spusťte `python doplnit_fotografie.py` (vyžaduje pouze běžný Python a přístup k internetu).
**Až po tomto kroku bude web plně offline a připravený na GitHub Pages.**
