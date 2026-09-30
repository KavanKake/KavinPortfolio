<script>
  import { page } from "$app/stores";
  import { t } from "$lib/i18n";
  import Icon from "$lib/Components/Icon.svelte";
  import Seo from "$lib/Components/Seo.svelte";

  const is404 = $derived($page.status === 404);

  const destinations = [
    { href: "/projects", key: "nav_projects", icon: "folder" },
    { href: "/aboutme", key: "nav_about", icon: "users" },
    { href: "/contactme", key: "nav_contact", icon: "mail" }
  ];
</script>

<Seo title={is404 ? $t("nf_title") : $t("nf_error_title")} description={$t("seo_404_desc")} path={$page.url.pathname} noindex />

<section class="page">
  <div class="container inner">
    <img class="logo" src="/assets/Kavin_logo.svg" alt="" aria-hidden="true" />
    <p class="code" aria-hidden="true">{$page.status}</p>
    <p class="eyebrow">{is404 ? $t("nf_eyebrow") : `${$page.status}`}</p>
    <h1>{is404 ? $t("nf_title") : $t("nf_error_title")}</h1>
    <p class="section-lead">{is404 ? $t("nf_lead") : $page.error?.message}</p>

    <a class="btn btn-primary home" href="/">{$t("nf_home")} <Icon name="arrow" /></a>

    <ul class="links">
      {#each destinations as d}
        <li>
          <a class="card" href={d.href}>
            <span class="i"><Icon name={d.icon} size={20} /></span>
            <strong>{$t(d.key)}</strong>
            <Icon name="arrow" size={16} />
          </a>
        </li>
      {/each}
    </ul>
  </div>
</section>

<style>
  .page {
    padding: calc(var(--nav-h) + clamp(40px, 8vw, 90px)) 0 80px;
    min-height: 70vh;
    position: relative;
    overflow: hidden;
  }
  .inner {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .logo {
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    height: 360px;
    width: auto;
    opacity: 0.08;
    pointer-events: none;
  }
  .code {
    font-family: var(--font-brand);
    font-size: clamp(5rem, 18vw, 9rem);
    line-height: 1;
    background: linear-gradient(120deg, var(--name-from) 10%, var(--accent) 55%, var(--brand) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 12px;
  }
  h1 {
    font-size: clamp(1.9rem, 4.5vw, 2.8rem);
    margin: 10px 0 14px;
  }
  .section-lead {
    margin: 0 auto;
  }
  .home {
    margin-top: 30px;
  }
  .links {
    list-style: none;
    padding: 0;
    margin: 40px 0 0;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    width: min(100%, 720px);
  }
  .links a {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px 18px;
    color: var(--text);
    text-decoration: none;
    border-radius: 14px;
    text-align: left;
  }
  .links a:hover {
    border-color: var(--border-strong);
    transform: translateY(-2px);
  }
  .links strong {
    flex: 1;
    font-family: var(--font-head);
  }
  .links a > :global(svg:last-child) {
    color: var(--text-faint);
  }
  .i {
    width: 38px;
    height: 38px;
    border-radius: 11px;
    display: grid;
    place-items: center;
    color: var(--accent);
    background: var(--surface-2);
    border: 1px solid var(--border);
  }
  @media (max-width: 640px) {
    .links {
      grid-template-columns: 1fr;
    }
  }
</style>
