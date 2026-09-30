<script>
  import { t, locale } from "$lib/i18n";
  import { links } from "$lib/data/profile.js";
  import ScrollReveal from "$lib/Components/ScrollReveal.svelte";
  import Icon from "$lib/Components/Icon.svelte";

  // Husk å oppdatere datoen når innholdet endres
  const UPDATED = "2026-09-30";

  const content = {
    no: {
      title: "Personvern",
      lead: "Kort og ærlig om hvilke opplysninger denne nettsiden behandler, og hvorfor. Siden bruker ingen informasjonskapsler (cookies).",
      updated: "Sist oppdatert",
      sections: [
        {
          icon: "users",
          h: "Hvem er ansvarlig?",
          p: [
            `Kavin Lokeswaran er behandlingsansvarlig for personopplysningene på kavinlokeswaran.no. Spørsmål om personvern kan sendes til <a href="mailto:${links.email}">${links.email}</a>.`
          ]
        },
        {
          icon: "mail",
          h: "Kontaktskjemaet",
          p: [
            "Når du sender en melding, behandles navnet, e-postadressen, emnet og meldingen du skriver inn. Opplysningene brukes bare til å svare deg.",
            `Skjemaet sendes via tjenesten <a href="https://web3forms.com" target="_blank" rel="noopener noreferrer">Web3Forms</a>, som videresender meldingen til e-posten min. Web3Forms kan behandle opplysningene utenfor EØS. Les mer i <a href="https://web3forms.com/privacy" target="_blank" rel="noopener noreferrer">Web3Forms' personvernerklæring</a>.`,
            "Meldingen blir liggende i innboksen min så lenge vi har dialog, og slettes senest 12 måneder etter at samtalen er avsluttet. Behandlingsgrunnlaget er berettiget interesse (GDPR art. 6 nr. 1 bokstav f): du har tatt kontakt og forventer svar.",
            `Vil du ikke bruke skjemaet, kan du sende e-post direkte til <a href="mailto:${links.email}">${links.email}</a>.`
          ]
        },
        {
          icon: "target",
          h: "Besøksstatistikk",
          p: [
            `Jeg bruker <a href="https://www.goatcounter.com" target="_blank" rel="noopener noreferrer">GoatCounter</a> for å se hvor mange som besøker siden. GoatCounter bruker ikke informasjonskapsler og lagrer ikke IP-adressen din. Det som registreres, er hvilken side du ser på, hvilken side du kom fra, nettleser, operativsystem, skjermstørrelse og omtrentlig land.`,
            "Tallene er anonyme og kan ikke knyttes til deg som person. Behandlingsgrunnlaget er berettiget interesse (GDPR art. 6 nr. 1 bokstav f): å forstå om nettsiden blir brukt. Mer informasjon finnes i <a href=\"https://www.goatcounter.com/help/privacy\" target=\"_blank\" rel=\"noopener noreferrer\">GoatCounters personvernerklæring</a>."
          ]
        },
        {
          icon: "github",
          h: "GitHub",
          p: [
            "Nettsiden ligger på GitHub Pages. Som alle nettservere mottar GitHub IP-adressen din når du åpner siden, og lagrer den en kort periode for sikkerhet og drift.",
            "Prosjektlisten hentes direkte fra GitHub sitt API i nettleseren din, så nye prosjekter vises med en gang. GitHub ser da IP-adressen din. Aktivitetsgrafen hentes derimot når siden bygges, og kontakter ikke GitHub fra nettleseren din.",
            `Se <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener noreferrer">GitHubs personvernerklæring</a>.`
          ]
        },
        {
          icon: "code",
          h: "Fonter og lokal lagring",
          p: [
            "Alle fonter ligger på min egen server, så ingen tredjepart (som Google eller Adobe) får vite at du besøker siden.",
            "Nettleseren din husker språkvalget ditt (localStorage) og mellomlagrer prosjektlisten i 30 minutter (sessionStorage). Dette ligger bare på din enhet og sendes ikke til meg."
          ]
        },
        {
          icon: "check",
          h: "Dine rettigheter",
          p: [
            `Du har rett til innsyn i, retting av og sletting av opplysningene jeg har om deg, og du kan protestere mot behandlingen. Send en e-post til <a href="mailto:${links.email}">${links.email}</a>, så svarer jeg innen 30 dager.`,
            `Mener du at jeg behandler opplysninger i strid med regelverket, kan du klage til <a href="https://www.datatilsynet.no" target="_blank" rel="noopener noreferrer">Datatilsynet</a>.`
          ]
        }
      ]
    },
    en: {
      title: "Privacy",
      lead: "A short and honest overview of the personal data this website processes, and why. The site uses no cookies.",
      updated: "Last updated",
      sections: [
        {
          icon: "users",
          h: "Who is responsible?",
          p: [
            `Kavin Lokeswaran is the data controller for kavinlokeswaran.no. Questions about privacy can be sent to <a href="mailto:${links.email}">${links.email}</a>.`
          ]
        },
        {
          icon: "mail",
          h: "The contact form",
          p: [
            "When you send a message, the name, email address, subject and message you enter are processed. They are only used to reply to you.",
            `The form is sent through <a href="https://web3forms.com" target="_blank" rel="noopener noreferrer">Web3Forms</a>, which forwards the message to my email. Web3Forms may process the data outside the EEA. Read more in <a href="https://web3forms.com/privacy" target="_blank" rel="noopener noreferrer">Web3Forms' privacy policy</a>.`,
            "The message stays in my inbox while we are in contact, and is deleted no later than 12 months after the conversation has ended. The legal basis is legitimate interest (GDPR Art. 6(1)(f)): you contacted me and expect a reply.",
            `If you'd rather not use the form, you can email me directly at <a href="mailto:${links.email}">${links.email}</a>.`
          ]
        },
        {
          icon: "target",
          h: "Visitor statistics",
          p: [
            `I use <a href="https://www.goatcounter.com" target="_blank" rel="noopener noreferrer">GoatCounter</a> to see how many people visit the site. GoatCounter uses no cookies and does not store your IP address. It records the page you view, the page you came from, browser, operating system, screen size and approximate country.`,
            "The numbers are anonymous and can't be linked to you as a person. The legal basis is legitimate interest (GDPR Art. 6(1)(f)): understanding whether the website is used. More information is in <a href=\"https://www.goatcounter.com/help/privacy\" target=\"_blank\" rel=\"noopener noreferrer\">GoatCounter's privacy policy</a>."
          ]
        },
        {
          icon: "github",
          h: "GitHub",
          p: [
            "The website is hosted on GitHub Pages. Like any web server, GitHub receives your IP address when you open the site, and keeps it for a short period for security and operations.",
            "The project list is fetched directly from GitHub's API in your browser, so new projects show up right away. GitHub then sees your IP address. The activity graph, on the other hand, is fetched when the site is built and does not contact GitHub from your browser.",
            `See <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener noreferrer">GitHub's privacy statement</a>.`
          ]
        },
        {
          icon: "code",
          h: "Fonts and local storage",
          p: [
            "All fonts are hosted on my own server, so no third party (such as Google or Adobe) learns that you visit the site.",
            "Your browser remembers your language choice (localStorage) and caches the project list for 30 minutes (sessionStorage). This stays on your device and is never sent to me."
          ]
        },
        {
          icon: "check",
          h: "Your rights",
          p: [
            `You have the right to access, correct and delete the data I hold about you, and to object to the processing. Send an email to <a href="mailto:${links.email}">${links.email}</a> and I'll reply within 30 days.`,
            `If you believe I process data in breach of the rules, you can complain to the Norwegian Data Protection Authority, <a href="https://www.datatilsynet.no/en/" target="_blank" rel="noopener noreferrer">Datatilsynet</a>.`
          ]
        }
      ]
    }
  };

  const c = $derived(content[$locale] ?? content.no);
  const updated = $derived(
    new Intl.DateTimeFormat($locale === "no" ? "nb-NO" : "en-GB", { dateStyle: "long" }).format(new Date(UPDATED))
  );
</script>

<svelte:head>
  <title>{$t("nav_privacy")} – Kavin Lokeswaran</title>
</svelte:head>

<section class="page">
  <div class="container narrow">
    <ScrollReveal>
      <p class="eyebrow">{$t("nav_privacy")}</p>
      <h1>{c.title}</h1>
      <p class="section-lead">{c.lead}</p>
      <p class="updated"><Icon name="clock" size={14} /> {c.updated}: {updated}</p>
    </ScrollReveal>

    <div class="sections">
      {#each c.sections as s}
        <ScrollReveal>
          <section class="card block">
            <h2><span class="i"><Icon name={s.icon} size={18} /></span>{s.h}</h2>
            {#each s.p as para}
              <p>{@html para}</p>
            {/each}
          </section>
        </ScrollReveal>
      {/each}
    </div>
  </div>
</section>

<style>
  .page {
    padding: calc(var(--nav-h) + clamp(40px, 8vw, 90px)) 0 80px;
  }
  .narrow {
    max-width: 820px;
  }
  h1 {
    font-size: clamp(2.4rem, 6vw, 4rem);
    margin: 10px 0 14px;
  }
  .updated {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: 14px;
    color: var(--text-faint);
    font-size: 0.85rem;
  }
  .sections {
    display: grid;
    gap: 16px;
    margin-top: 40px;
  }
  .block {
    padding: clamp(20px, 4vw, 30px);
    display: grid;
    gap: 12px;
  }
  .block h2 {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 1.2rem;
    margin-bottom: 2px;
  }
  .i {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    display: grid;
    place-items: center;
    color: var(--accent);
    background: var(--surface-2);
    border: 1px solid var(--border);
    flex-shrink: 0;
  }
  .block p {
    color: var(--text-muted);
    max-width: 68ch;
  }
  .block p :global(a) {
    color: var(--accent);
    text-underline-offset: 2px;
  }
</style>
