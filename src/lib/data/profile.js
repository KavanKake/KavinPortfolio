// Alt personlig innhold samlet på ett sted – endre her, så oppdateres hele siden.

export const GITHUB_USER = "KavanKake";

export const links = {
  email: "contact@kavinlokeswaran.no",
  github: `https://github.com/${GITHUB_USER}`,
  instagram: "https://instagram.com/kavinlokeswaran",
  // Legg inn riktig LinkedIn-URL her, så dukker ikonet opp automatisk:
  linkedin: "",
  site: "https://kavinlokeswaran.no"
};

// Web3Forms tilgangsnøkkel for kontaktskjemaet (https://web3forms.com).
// Nøkkelen er laget for å ligge offentlig i nettsiden – den kan bare brukes til å
// sende skjemaer til din e-post. Du kan lage en ny i Web3Forms-dashbordet ved behov.
export const WEB3FORMS_KEY = "f12fe63f-5ca8-48e0-b345-65bf4353e21a";

/** Ferdigheter gruppert slik rekrutterere skanner dem. level: 1–3 (lærer / komfortabel / sterk) */
export const skills = [
  {
    key: "frontend",
    items: [
      { name: "HTML", level: 3 },
      { name: "CSS", level: 3 },
      { name: "JavaScript", level: 3 },
      { name: "Svelte / SvelteKit", level: 2 },
      { name: "Responsivt design", level: 2 }
    ]
  },
  {
    key: "backend",
    items: [
      { name: "Node.js", level: 2 },
      { name: "Express", level: 2 },
      { name: "REST-API-er", level: 2 },
      { name: "Innlogging / sessions", level: 1 }
    ]
  },
  {
    key: "programming",
    items: [
      { name: "Python", level: 3 },
      { name: "Pygame", level: 2 },
      { name: "OOP", level: 2 }
    ]
  },
  {
    key: "tools",
    items: [
      { name: "Git & GitHub", level: 2 },
      { name: "GitHub Actions", level: 1 },
      { name: "VS Code", level: 3 }
    ]
  }
];

export const education = [
  { key: "bachelor", current: true },
  { key: "elvebakken" },
  { key: "lofsrud" },
  { key: "mortensrud" }
];
