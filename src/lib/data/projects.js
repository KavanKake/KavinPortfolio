// Håndplukkede prosjekter. Alle ANDRE offentlige repoer på GitHub hentes automatisk
// (se src/lib/github.js), så du trenger bare legge til prosjekter her hvis du vil
// fremheve dem med bilde og egen tekst.
//
// repo     – navnet på repoet på GitHub (brukes til lenke og for å unngå duplikater)
// featured – vises på forsiden
// status   – "done" | "in_progress"
// text     – { no, en } kort beskrivelse: problem → hva du gjorde → resultat

export const curatedProjects = [
  {
    id: "portfolio",
    title: "Portefølje – kavinlokeswaran.no",
    repo: "KavinPortfolio",
    live: "https://kavinlokeswaran.no",
    image: "/img/portfolio.webp",
    tech: ["SvelteKit", "JavaScript", "CSS", "GitHub API", "GitHub Actions"],
    featured: true,
    status: "done",
    text: {
      no: "Personlig nettside bygget med SvelteKit. Tospråklig (norsk/engelsk), responsiv, og henter nye offentlige GitHub-repoer automatisk – så porteføljen aldri blir utdatert.",
      en: "Personal website built with SvelteKit. Bilingual (Norwegian/English), responsive, and automatically pulls in new public GitHub repositories so it never goes stale."
    }
  },
  {
    id: "bakkasmak",
    title: "BakkaSmak",
    repo: "BakkaSmak",
    live: null,
    image: "/img/bakkasmak.webp",
    tech: ["HTML", "CSS", "JavaScript"],
    featured: true,
    status: "done",
    text: {
      no: "Nettside for en skolekantine med ukesmeny (mandag–fredag), snacks-side, «Stem her»-avstemning og om oss-side. Fokus på tydelig navigasjon og innbydende matbilder.",
      en: "Website for a school cafeteria with a weekly menu (Monday–Friday), snacks page, a “vote here” poll and an about page. Focused on clear navigation and inviting food imagery."
    }
  },
  {
    id: "multikit",
    title: "MultiKit",
    repo: "MultikitWebpage",
    live: null,
    image: "/img/multikit.webp",
    tech: ["HTML", "CSS", "JavaScript"],
    featured: true,
    status: "done",
    text: {
      no: "Landingsside for produktet MultiKit med registrering og innlogging, animert bakgrunn og en ren, konverteringsfokusert forside.",
      en: "Landing page for the MultiKit product with sign-up and login, an animated background and a clean, conversion-focused front page."
    }
  },
  {
    id: "doquire",
    title: "Doquire",
    repo: null,
    live: null,
    image: "/assets/doquire_logo.svg",
    tech: [],
    featured: true,
    status: "in_progress",
    text: {
      no: "Pågående prosjekt – mer kommer snart.",
      en: "Work in progress – more coming soon."
    }
  },
  {
    id: "vikingtokt",
    title: "Vikingtokt – Wolfheart Tribe",
    repo: "Vikingtokt",
    live: null,
    image: "/img/vikingtokt.webp",
    tech: ["HTML", "CSS", "JavaScript", "Teamarbeid"],
    featured: false,
    status: "done",
    text: {
      no: "Vikinginspirert nettside med butikk, «bli med»-side og om oss. Laget i team sammen med Henrik Luan.",
      en: "Viking-themed website with a shop, “join us” page and about page. Built as a team together with Henrik Luan."
    }
  },
  {
    id: "express",
    title: "Innlogging med Express.js",
    repo: "Express-js",
    live: null,
    image: "/img/express-login.webp",
    tech: ["Node.js", "Express", "JavaScript"],
    featured: false,
    status: "done",
    text: {
      no: "Innloggings- og registreringssystem på serversiden med Node.js og Express.",
      en: "Server-side login and sign-up system built with Node.js and Express."
    }
  },
  {
    id: "quiz",
    title: "Who Wants to Be a Millionaire",
    repo: "Quizspill",
    live: null,
    image: null,
    tech: ["Python", "Pygame"],
    featured: false,
    status: "done",
    text: {
      no: "Quizspill i Python med livlinjer (50/50, ring en venn, spør publikum), lyd og grafikk.",
      en: "Quiz game in Python with lifelines (50/50, phone a friend, ask the audience), sound and graphics."
    }
  },
  {
    id: "viking-game",
    title: "Viking game",
    repo: "Viking_game",
    live: null,
    image: null,
    tech: ["Godot", "GDScript"],
    featured: false,
    status: "done",
    text: {
      no: "2D-spill laget i Godot-motoren.",
      en: "2D game built with the Godot engine."
    }
  },
  {
    id: "rating",
    title: "Ratingsystem – fotball",
    repo: "Ratingsystem-fotball",
    live: null,
    image: null,
    tech: ["Python"],
    featured: false,
    status: "done",
    text: {
      no: "Python-program som beregner og rangerer fotballspillere/lag etter prestasjoner.",
      en: "Python program that calculates and ranks football players/teams by performance."
    }
  }
];

export const githubUrl = (repo) => (repo ? `https://github.com/KavanKake/${repo}` : null);
