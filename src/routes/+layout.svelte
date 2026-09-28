<script>
  import "../app.css";
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import { locale, t, initLocale } from "$lib/i18n";
  import Icon from "$lib/Components/Icon.svelte";
  import Footer from "$lib/Components/Footer.svelte";

  let { children } = $props();

  let open = $state(false);
  let scrolled = $state(false);

  const links = [
    { href: "/projects", key: "nav_projects" },
    { href: "/aboutme", key: "nav_about" },
    { href: "/contactme", key: "nav_contact" }
  ];

  onMount(() => {
    initLocale();
    const onScroll = () => (scrolled = window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  });

  // Lukk mobilmenyen ved navigasjon
  $effect(() => {
    $page.url.pathname;
    open = false;
  });

  const isActive = (href) => $page.url.pathname.startsWith(href);
</script>

<svelte:head>
  <title>Kavin Lokeswaran – student & utvikler</title>
  <meta
    name="description"
    content="Portefølje for Kavin Lokeswaran – bachelorstudent i programmering og systemarkitektur og webutvikler fra Oslo. Prosjekter i SvelteKit, JavaScript, Node/Express og Python."
  />
  <meta property="og:title" content="Kavin Lokeswaran – student & utvikler" />
  <meta property="og:description" content="Prosjekter, ferdigheter og kontaktinfo." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://kavinlokeswaran.no" />
  <meta property="og:image" content="https://kavinlokeswaran.no/img/og.jpg" />
</svelte:head>

<a class="skip" href="#main">{$t("skip")}</a>

<header class="nav" class:scrolled class:open>
  <div class="nav-inner container">
    <a class="brand" href="/" aria-label="Kavin Lokeswaran – {$t('nav_home')}">
      <img src="/assets/Kavin_logo.svg" alt="" width="34" height="40" />
      <span class="brand-name">Kavin Lokeswaran</span>
    </a>

    <nav class="links" aria-label="Hovedmeny">
      {#each links as l}
        <a href={l.href} class:active={isActive(l.href)} aria-current={isActive(l.href) ? "page" : undefined}>
          {$t(l.key)}
        </a>
      {/each}
    </nav>

    <div class="actions">
      <div class="lang" role="group" aria-label="Språk / Language">
        <button type="button" class:active={$locale === "no"} aria-pressed={$locale === "no"} onclick={() => locale.set("no")}>NO</button>
        <button type="button" class:active={$locale === "en"} aria-pressed={$locale === "en"} onclick={() => locale.set("en")}>EN</button>
      </div>
      <a class="btn btn-primary nav-cta" href="/contactme">{$t("hero_cta_contact")}</a>
      <button
        class="burger"
        type="button"
        aria-expanded={open}
        aria-controls="mobile-menu"
        aria-label={$t("nav_menu")}
        onclick={() => (open = !open)}
      >
        <Icon name={open ? "close" : "menu"} size={22} />
      </button>
    </div>
  </div>

  {#if open}
    <nav id="mobile-menu" class="mobile" aria-label={$t("nav_menu")}>
      <a href="/">{$t("nav_home")}</a>
      {#each links as l}
        <a href={l.href} class:active={isActive(l.href)}>{$t(l.key)}</a>
      {/each}
    </nav>
  {/if}
</header>

<main id="main">
  {@render children()}
</main>

<Footer />

<style>
  .skip {
    position: absolute;
    left: 16px;
    top: -60px;
    z-index: 200;
    background: var(--brand);
    color: #fff;
    padding: 10px 14px;
    border-radius: 8px;
    text-decoration: none;
  }
  .skip:focus {
    top: 12px;
  }

  .nav {
    position: fixed;
    inset: 0 0 auto 0;
    z-index: 100;
    transition:
      background-color 0.3s ease,
      border-color 0.3s ease,
      backdrop-filter 0.3s ease;
    border-bottom: 1px solid transparent;
  }
  .nav.scrolled,
  .nav.open {
    background: rgba(3, 0, 39, 0.78);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom-color: var(--border);
  }

  .nav-inner {
    height: var(--nav-h);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
  }

  .brand {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--text);
  }
  .brand img {
    height: 38px;
    width: auto;
    transition: transform 0.3s ease;
  }
  .brand:hover img {
    transform: rotate(-6deg) scale(1.06);
  }
  .brand-name {
    font-family: var(--font-brand);
    font-size: 1.15rem;
    letter-spacing: 0.04em;
    color: var(--accent);
  }

  .links {
    display: flex;
    gap: 6px;
  }
  .links a {
    position: relative;
    padding: 8px 14px;
    border-radius: 999px;
    color: var(--text-muted);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.95rem;
    transition:
      color 0.2s ease,
      background-color 0.2s ease;
  }
  .links a:hover {
    color: var(--text);
    background: var(--surface);
  }
  .links a.active {
    color: var(--text);
    background: var(--surface-2);
  }

  .actions {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .lang {
    display: inline-flex;
    padding: 3px;
    border-radius: 999px;
    background: var(--surface);
    border: 1px solid var(--border);
  }
  .lang button {
    border: 0;
    background: none;
    color: var(--text-faint);
    font: 600 0.75rem var(--font-head);
    letter-spacing: 0.08em;
    padding: 6px 10px;
    border-radius: 999px;
    cursor: pointer;
  }
  .lang button.active {
    background: var(--brand);
    color: #fff;
  }

  .nav-cta {
    padding: 0.6em 1.1em;
    font-size: 0.9rem;
  }

  .burger {
    display: none;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
    border-radius: 12px;
    width: 42px;
    height: 42px;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }

  .mobile {
    display: flex;
    flex-direction: column;
    padding: 8px var(--gutter) 20px;
    gap: 4px;
  }
  .mobile a {
    color: var(--text);
    text-decoration: none;
    font-family: var(--font-head);
    font-size: 1.25rem;
    padding: 12px 4px;
    border-bottom: 1px solid var(--border);
  }
  .mobile a.active {
    color: var(--accent);
  }

  @media (max-width: 860px) {
    .links,
    .nav-cta {
      display: none;
    }
    .burger {
      display: inline-flex;
    }
  }
  @media (max-width: 420px) {
    .brand-name {
      display: none;
    }
  }
</style>
