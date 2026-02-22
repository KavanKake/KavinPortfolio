import { writable, derived } from "svelte/store";

// Default language (used on first load if user hasn't selected)
export const locale = writable("en");

if (typeof document !== "undefined") {
  locale.subscribe((value) => {
    try {
      localStorage.setItem("portfolio-locale", value);
    } catch (_) {}
  });
}

const translations = {
  no: {
    nav_home: "Hjem",
    nav_projects: "Prosjekter",
    nav_about: "Om meg",
    nav_contact: "Kontakt",
    footer_social: "SOSIALE MEDIER",
    footer_nav: "NAVIGASJON",
    footer_home: "HJEM",
    footer_projects: "PROSJEKTER",
    footer_about: "OM MEG",
    footer_contact: "KONTAKT",
    footer_back_to_top: "← TILBAKE TIL TOPPEN →",
    footer_copyright: "COPYRIGHT (2026) KAVIN LOKESWARAN",
    home_welcome: "Hei, og velkommen til porteføljen min",
    home_projects: "Prosjekter",
    home_featured: "Her er noen utvalgte prosjekter",
    home_prev: "Forrige prosjekt",
    home_next: "Neste prosjekt",
    projects_title: "Prosjekter",
    projects_subtitle: "Prosjekter lenket til GitHub",
    projects_github: "Åpne på GitHub →",
    projects_in_progress: "Under arbeid",
    about_title: "Om meg",
    about_subtitle: "Kavin Lokeswaran – IT-student",
    about_paragraph: "Hei, jeg heter Kavin Lokeswaran. Jeg er en IT-student med stor interesse for teknologi og programmering på Elvebakken VGS i Oslo. Jeg studerer IT fordi jeg liker å forstå hvordan teknologi fungerer og hvordan den kan forbedre hverdagen. Jeg har jobbet med mange prosjekter, for eksempel denne nettsiden. Når jeg ikke jobber med IT, spiller jeg gjerne spill eller fotball. Drømmen min er å bli ingeniør innen IT.",
    about_school_mortensrud: "Mortensrud skole",
    about_school_mortensrud_years: "2013–2020",
    about_school_lofsrud: "Lofsrud skole",
    about_school_lofsrud_years: "2020–2023",
    about_school_elvebakken: "Elvebakken VGS",
    about_school_elvebakken_years: "2023 – nå",
    contact_heading: "Vil du ta kontakt?",
    contact_intro1: "Fyll ut skjemaet til høyre for å sende meg en e-post",
    contact_intro2: "Eller send e-post direkte til adressen under",
    contact_form_title: "Kontaktskjema",
    contact_name: "Navn",
    contact_firstname: "Fornavn",
    contact_lastname: "Etternavn",
    contact_email: "E-post",
    contact_email_placeholder: "Din e-post",
    contact_topic: "Emne",
    contact_topic_placeholder: "Emne",
    contact_message: "Melding",
    contact_message_placeholder: "Skriv meldingen din",
    contact_submit: "Send",
    contact_subject_hidden: "Ny melding fra porteføljen"
  },
  en: {
    nav_home: "Home",
    nav_projects: "Projects",
    nav_about: "About me",
    nav_contact: "Contact me",
    footer_social: "SOCIAL MEDIA",
    footer_nav: "NAVIGATION",
    footer_home: "HOME",
    footer_projects: "PROJECTS",
    footer_about: "ABOUT ME",
    footer_contact: "CONTACT ME",
    footer_back_to_top: "← BACK TO TOP →",
    footer_copyright: "COPYRIGHT (2026) KAVIN LOKESWARAN",
    home_welcome: "Hi, and welcome to my Portfolio",
    home_projects: "Projects",
    home_featured: "Here are some featured projects",
    home_prev: "Previous project",
    home_next: "Next project",
    projects_title: "Projects",
    projects_subtitle: "Projects linked to GitHub",
    projects_github: "Open on GitHub →",
    projects_in_progress: "In progress",
    about_title: "About me",
    about_subtitle: "Kavin Lokeswaran – IT student",
    about_paragraph: "Hello, my name is Kavin Lokeswaran. I am a passionate IT student with a strong interest in technology and programming at Elvebakken VGS in Oslo, Norway. I am currently studying IT because I enjoy understanding how technology works and how it can improve our daily lives. I have worked on many projects, including this website. When I'm not working on IT-related projects, I enjoy playing games or football. My dream is to become an IT engineer.",
    about_school_mortensrud: "Mortensrud school",
    about_school_mortensrud_years: "2013–2020",
    about_school_lofsrud: "Lofsrud school",
    about_school_lofsrud_years: "2020–2023",
    about_school_elvebakken: "Elvebakken VGS",
    about_school_elvebakken_years: "2023–2026",
    contact_heading: "Would you like to contact me?",
    contact_intro1: "Fill out the form on the right to send me an email",
    contact_intro2: "Or send an email directly to the address below",
    contact_form_title: "Contact form",
    contact_name: "Name",
    contact_firstname: "First name",
    contact_lastname: "Last name",
    contact_email: "Email",
    contact_email_placeholder: "Your email",
    contact_topic: "Topic",
    contact_topic_placeholder: "Topic",
    contact_message: "Message",
    contact_message_placeholder: "Enter your message",
    contact_submit: "Send",
    contact_subject_hidden: "New message from portfolio"
  }
};

export const t = derived(locale, ($locale) => (key) =>
  translations[$locale]?.[key] ?? translations.no[key] ?? key
);

export function getTranslations() {
  let $locale;
  locale.subscribe((v) => ($locale = v))();
  return translations[$locale] || translations.no;
}
