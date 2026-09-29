# kavinlokeswaran.no

Personlig portefølje for Kavin Lokeswaran – IT-student og utvikler fra Oslo.
Bygget med **SvelteKit** (statisk), tospråklig (NO/EN) og publisert via GitHub Actions.

## Funksjoner

- **Besøksstatistikk med GoatCounter** (uten cookies): se https://kavin.goatcounter.com
- **Kontaktskjema via Web3Forms** (sendes i bakgrunnen med takk-/feilmelding; nøkkel i `src/lib/data/profile.js`).
- **Rekrutterer-vennlig oppsett:** tydelig hero med hvem/hva/tilgjengelighet, ferdigheter med nivå, 3–4 utvalgte prosjekter med teknologi, kode- og live-lenker, om meg, utdanning og kontakt.
- **Automatiske GitHub-prosjekter:** alle offentlige repoer på [github.com/KavanKake](https://github.com/KavanKake) hentes automatisk
  - live i nettleseren via GitHub API (nye repoer vises med en gang)
  - pluss et øyeblikksbilde (`static/data/repos.json`) som lages ved hver build og oppdateres hver natt av GitHub Actions
- Raske, optimaliserte bilder (WebP), ingen kunstig lasteskjerm, mobilvennlig og tilgjengelig (tastatur, skip-lenke, redusert bevegelse).

## Endre innhold

| Hva | Fil |
| --- | --- |
| Tekster (norsk/engelsk) | `src/lib/i18n/index.js` |
| Ferdigheter, lenker (LinkedIn m.m.), utdanning | `src/lib/data/profile.js` |
| Utvalgte prosjekter (bilde, tekst, teknologi) | `src/lib/data/projects.js` |

Nye offentlige repoer trenger du **ikke** legge inn – de dukker opp automatisk. Tips: gi repoene en beskrivelse, *topics* og eventuelt en *website*-lenke på GitHub, så vises det på kortet.

## Utvikling

```bash
npm install
npm run dev      # lokal utvikling
npm run build    # henter repoer + bygger til /build
```

## Kontakt

- E-post: contact@kavinlokeswaran.no
- GitHub: [KavanKake](https://github.com/KavanKake)
