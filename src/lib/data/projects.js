// Håndplukkede prosjekter. Bare prosjekter med OFFENTLIG repo på GitHub skal ligge her.
// Alle andre offentlige repoer hentes automatisk (se src/lib/github.js), så du trenger
// bare legge til et prosjekt her hvis du vil fremheve det med bilde og egen tekst.
//
// repo     – navnet på det offentlige repoet på GitHub (brukes til lenke og for å unngå duplikater)
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
  }
];

export const githubUrl = (repo) => (repo ? `https://github.com/KavanKake/${repo}` : null);
