<script>
  // Tittel, beskrivelse, kanonisk URL og delingsdata (Open Graph / X) for én side.
  // Brukes øverst i hver side: <Seo title="Prosjekter" description="…" path="/projects" />
  import { locale } from "$lib/i18n";
  import { links } from "$lib/data/profile.js";

  let { title = "", description, path = "/", image = "/img/og.jpg", noindex = false } = $props();
  const isHome = $derived(path === "/");

  const NAME = "Kavin Lokeswaran";
  // Navnet står alltid i tittelen: først på forsiden, ellers til slutt ("Prosjekter – Kavin Lokeswaran")
  const fullTitle = $derived(!title ? NAME : isHome ? `${NAME} – ${title}` : `${title} – ${NAME}`);
  const url = $derived(links.site + path);
  const imageUrl = $derived(links.site + image);
</script>

<svelte:head>
  <title>{fullTitle}</title>
  <meta name="description" content={description} />
  {#if noindex}
    <meta name="robots" content="noindex" />
  {:else}
    <link rel="canonical" href={url} />
  {/if}

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content={NAME} />
  <meta property="og:locale" content={$locale === "en" ? "en_GB" : "nb_NO"} />
  <meta property="og:title" content={fullTitle} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={url} />
  <meta property="og:image" content={imageUrl} />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={fullTitle} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={imageUrl} />
</svelte:head>
