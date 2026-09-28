import { writable, derived } from "svelte/store";

export const locale = writable("no");

const STORAGE_KEY = "portfolio-locale";

/** Kalles én gang i layouten: lagret valg → nettleserspråk → norsk */
export function initLocale() {
  if (typeof window === "undefined") return;
  let initial = "no";
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored === "no" || stored === "en") initial = stored;
    else {
      const nav = (navigator.language || "").toLowerCase();
      initial = /^(nb|nn|no|da|sv)/.test(nav) ? "no" : "en";
    }
  } catch {
    /* ignorer */
  }
  locale.set(initial);
  locale.subscribe((value) => {
    try {
      localStorage.setItem(STORAGE_KEY, value);
    } catch {
      /* ignorer */
    }
    document.documentElement.lang = value === "no" ? "no" : "en";
  });
}

const translations = {
  no: {
    skip: "Hopp til innhold",
    nav_home: "Hjem",
    nav_projects: "Prosjekter",
    nav_skills: "Ferdigheter",
    nav_about: "Om meg",
    nav_contact: "Kontakt",
    nav_menu: "Meny",

    hero_eyebrow: "IT-student · Utvikler · Oslo",
    hero_hi: "Hei, jeg er",
    hero_title: "Jeg bygger nettsider og apper som er enkle å bruke.",
    hero_pitch:
      "IT-student ved Elvebakken VGS med fokus på webutvikling. Jeg jobber med JavaScript, Svelte, Node/Express og Python – og liker å ta et prosjekt helt fra idé til ferdig, publisert løsning.",
    hero_available: "Åpen for nye muligheter",
    hero_cta_projects: "Se prosjektene mine",
    hero_cta_contact: "Ta kontakt",
    hero_img_alt: "Portrett av Kavin Lokeswaran",

    stat_repos: "offentlige repoer",
    stat_last: "Sist aktiv på GitHub",
    stat_location: "Oslo, Norge",
    stat_languages: "Norsk & engelsk",

    skills_eyebrow: "Ferdigheter",
    skills_title: "Verktøyene jeg bruker",
    skills_lead:
      "Et ærlig bilde av hva jeg kan i dag. Alt her er brukt i ekte prosjekter du finner lenger ned og på GitHub.",
    skills_frontend: "Frontend",
    skills_backend: "Backend",
    skills_programming: "Programmering",
    skills_tools: "Verktøy og arbeidsflyt",
    level_1: "Lærer",
    level_2: "Komfortabel",
    level_3: "Sterk",

    featured_eyebrow: "Utvalgte prosjekter",
    featured_title: "Ting jeg har bygget",
    featured_lead: "Et utvalg prosjekter som viser hva jeg kan – med kode og teknologi for hvert av dem.",
    featured_all: "Alle prosjekter",

    gh_eyebrow: "Direkte fra GitHub",
    gh_title: "Siste aktivitet",
    gh_lead: "Oppdateres automatisk – nye offentlige repoer dukker opp her av seg selv.",
    gh_profile: "Se GitHub-profilen",
    gh_loading: "Henter repoer fra GitHub …",
    gh_error: "Klarte ikke å hente repoer akkurat nå.",
    gh_empty: "Ingen flere offentlige repoer ennå.",
    gh_updated: "Oppdatert",
    gh_new: "Ny",
    gh_no_desc: "Ingen beskrivelse ennå.",

    project_code: "Kode",
    project_live: "Se live",
    project_in_progress: "Under arbeid",
    project_private: "Privat repo",

    about_eyebrow: "Om meg",
    about_title: "Litt om meg",
    about_p1:
      "Jeg heter Kavin Lokeswaran og er IT-student ved Elvebakken VGS i Oslo. Jeg valgte IT fordi jeg liker å forstå hvordan teknologi fungerer – og hvordan den kan gjøre hverdagen enklere for folk.",
    about_p2:
      "Jeg lærer best ved å bygge. Derfor har jeg laget alt fra nettsider og innloggingssystemer til spill i Python og Godot, både alene og i team. Denne nettsiden er også et av prosjektene mine.",
    about_p3:
      "Når jeg ikke koder, spiller jeg fotball eller gaming. Målet mitt er å bli IT-ingeniør.",
    about_more: "Mer om meg",
    about_img_alt: "Kavin som jobber på laptop",

    values_title: "Hva du får med meg",
    value_1_t: "Lærer raskt",
    value_1_d: "Setter meg inn i nye verktøy og rammeverk på egen hånd – som SvelteKit og Express.",
    value_2_t: "Fullfører",
    value_2_d: "Tar prosjekter fra idé til publisert løsning, med kode på GitHub.",
    value_3_t: "Samarbeider",
    value_3_d: "Vant til teamprosjekter på skolen, med Git for deling og versjonskontroll.",

    edu_title: "Utdanning",
    edu_elvebakken: "Elvebakken VGS",
    edu_elvebakken_sub: "Informasjonsteknologi",
    edu_elvebakken_years: "2023 – nå",
    edu_lofsrud: "Lofsrud skole",
    edu_lofsrud_sub: "Ungdomsskole",
    edu_lofsrud_years: "2020 – 2023",
    edu_mortensrud: "Mortensrud skole",
    edu_mortensrud_sub: "Barneskole",
    edu_mortensrud_years: "2013 – 2020",
    edu_now: "Nå",

    interests_title: "Interesser",
    interest_1: "Webutvikling",
    interest_2: "Spillutvikling",
    interest_3: "Design / UI",
    interest_4: "Fotball",
    interest_5: "Gaming",

    cta_title: "Skal vi jobbe sammen?",
    cta_lead:
      "Jeg er åpen for deltidsjobb, sommerjobb, praksis og spennende prosjekter. Send meg en melding – jeg svarer raskt.",
    cta_button: "Send meg en melding",

    projects_title: "Prosjekter",
    projects_lead:
      "Håndplukkede prosjekter øverst, og alle andre offentlige repoer fra GitHub under – de hentes automatisk.",
    projects_curated: "Utvalgte prosjekter",
    projects_more: "Flere prosjekter fra GitHub",
    projects_more_lead: "Hentes automatisk fra GitHub. Nye offentlige repoer vises her uten at jeg trenger å oppdatere siden.",
    projects_filter_all: "Alle",
    projects_search: "Søk i repoer",
    projects_count: "repoer",

    contact_eyebrow: "Kontakt",
    contact_heading: "La oss snakke sammen",
    contact_intro:
      "Har du en jobb, et prosjekt eller bare et spørsmål? Fyll ut skjemaet, eller send en e-post direkte.",
    contact_direct: "Direkte",
    contact_response: "Svarer vanligvis innen 24 timer",
    contact_form_title: "Send en melding",
    contact_firstname: "Fornavn",
    contact_lastname: "Etternavn",
    contact_email: "E-post",
    contact_email_placeholder: "navn@firma.no",
    contact_topic: "Emne",
    contact_topic_placeholder: "Hva gjelder det?",
    contact_message: "Melding",
    contact_message_placeholder: "Skriv meldingen din …",
    contact_submit: "Send melding",
    contact_subject_hidden: "Ny melding fra porteføljen",
    contact_copy: "Kopier",
    contact_copied: "Kopiert!",

    footer_tagline: "IT-student og utvikler fra Oslo.",
    footer_nav: "Navigasjon",
    footer_social: "Finn meg",
    footer_back_to_top: "Til toppen",
    footer_built: "Bygget med SvelteKit",
    footer_copyright: "Kavin Lokeswaran"
  },
  en: {
    skip: "Skip to content",
    nav_home: "Home",
    nav_projects: "Projects",
    nav_skills: "Skills",
    nav_about: "About",
    nav_contact: "Contact",
    nav_menu: "Menu",

    hero_eyebrow: "IT student · Developer · Oslo",
    hero_hi: "Hi, I'm",
    hero_title: "I build websites and apps that are easy to use.",
    hero_pitch:
      "IT student at Elvebakken Upper Secondary in Oslo, focused on web development. I work with JavaScript, Svelte, Node/Express and Python – and I enjoy taking a project all the way from idea to a finished, published product.",
    hero_available: "Open to new opportunities",
    hero_cta_projects: "View my projects",
    hero_cta_contact: "Get in touch",
    hero_img_alt: "Portrait of Kavin Lokeswaran",

    stat_repos: "public repositories",
    stat_last: "Last active on GitHub",
    stat_location: "Oslo, Norway",
    stat_languages: "Norwegian & English",

    skills_eyebrow: "Skills",
    skills_title: "The tools I use",
    skills_lead:
      "An honest picture of what I can do today. Everything here has been used in real projects you can find below and on GitHub.",
    skills_frontend: "Frontend",
    skills_backend: "Backend",
    skills_programming: "Programming",
    skills_tools: "Tools & workflow",
    level_1: "Learning",
    level_2: "Comfortable",
    level_3: "Strong",

    featured_eyebrow: "Featured work",
    featured_title: "Things I've built",
    featured_lead: "A selection of projects that show what I can do – with code and tech stack for each.",
    featured_all: "All projects",

    gh_eyebrow: "Live from GitHub",
    gh_title: "Recent activity",
    gh_lead: "Updated automatically – new public repositories show up here on their own.",
    gh_profile: "View GitHub profile",
    gh_loading: "Fetching repositories from GitHub …",
    gh_error: "Couldn't load repositories right now.",
    gh_empty: "No other public repositories yet.",
    gh_updated: "Updated",
    gh_new: "New",
    gh_no_desc: "No description yet.",

    project_code: "Code",
    project_live: "Live demo",
    project_in_progress: "In progress",
    project_private: "Private repo",

    about_eyebrow: "About",
    about_title: "A bit about me",
    about_p1:
      "My name is Kavin Lokeswaran and I'm an IT student at Elvebakken Upper Secondary School in Oslo. I chose IT because I love understanding how technology works – and how it can make everyday life easier for people.",
    about_p2:
      "I learn best by building. I've made everything from websites and login systems to games in Python and Godot, both on my own and in teams. This website is one of my projects too.",
    about_p3: "When I'm not coding, I play football or games. My goal is to become an IT engineer.",
    about_more: "More about me",
    about_img_alt: "Kavin working on a laptop",

    values_title: "What you get with me",
    value_1_t: "Fast learner",
    value_1_d: "I pick up new tools and frameworks on my own – like SvelteKit and Express.",
    value_2_t: "I finish things",
    value_2_d: "I take projects from idea to a published product, with the code on GitHub.",
    value_3_t: "Team player",
    value_3_d: "Used to team projects at school, using Git for sharing and version control.",

    edu_title: "Education",
    edu_elvebakken: "Elvebakken Upper Secondary",
    edu_elvebakken_sub: "Information Technology",
    edu_elvebakken_years: "2023 – present",
    edu_lofsrud: "Lofsrud School",
    edu_lofsrud_sub: "Lower secondary",
    edu_lofsrud_years: "2020 – 2023",
    edu_mortensrud: "Mortensrud School",
    edu_mortensrud_sub: "Primary school",
    edu_mortensrud_years: "2013 – 2020",
    edu_now: "Now",

    interests_title: "Interests",
    interest_1: "Web development",
    interest_2: "Game development",
    interest_3: "Design / UI",
    interest_4: "Football",
    interest_5: "Gaming",

    cta_title: "Let's work together",
    cta_lead:
      "I'm open to part-time and summer jobs, internships and interesting projects. Send me a message – I reply quickly.",
    cta_button: "Send me a message",

    projects_title: "Projects",
    projects_lead:
      "Hand-picked projects at the top, and every other public GitHub repository below – fetched automatically.",
    projects_curated: "Featured projects",
    projects_more: "More projects from GitHub",
    projects_more_lead: "Fetched automatically from GitHub. New public repositories appear here without me updating the site.",
    projects_filter_all: "All",
    projects_search: "Search repositories",
    projects_count: "repositories",

    contact_eyebrow: "Contact",
    contact_heading: "Let's talk",
    contact_intro:
      "Have a job, a project or just a question? Fill out the form, or send an email directly.",
    contact_direct: "Direct",
    contact_response: "Usually replies within 24 hours",
    contact_form_title: "Send a message",
    contact_firstname: "First name",
    contact_lastname: "Last name",
    contact_email: "Email",
    contact_email_placeholder: "name@company.com",
    contact_topic: "Subject",
    contact_topic_placeholder: "What is it about?",
    contact_message: "Message",
    contact_message_placeholder: "Write your message …",
    contact_submit: "Send message",
    contact_subject_hidden: "New message from portfolio",
    contact_copy: "Copy",
    contact_copied: "Copied!",

    footer_tagline: "IT student and developer from Oslo.",
    footer_nav: "Navigation",
    footer_social: "Find me",
    footer_back_to_top: "Back to top",
    footer_built: "Built with SvelteKit",
    footer_copyright: "Kavin Lokeswaran"
  }
};

export const t = derived(locale, ($locale) => (key) =>
  translations[$locale]?.[key] ?? translations.no[key] ?? key
);
