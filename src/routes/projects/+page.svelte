<script>
  import Footer from "$lib/Components/Footer.svelte";
  import { githubProjects } from "$lib/Components/projects.js";
  import { t } from "$lib/i18n";
  import ScrollReveal from "$lib/Components/ScrollReveal.svelte";
</script>

<div class="page-wrapper">
  <div class="spacer"></div>
  <main class="page">
    <ScrollReveal>
      <div class="overskrift">
        <h1>{$t("projects_title")}</h1>
        <p class="subtitle">{$t("projects_subtitle")}</p>
      </div>
    </ScrollReveal>
    <div class="projects-grid">
    {#each githubProjects as project, i}
      <ScrollReveal delay={i * 80}>
      {#if project.githubUrl}
      <a
        class="project-card"
        href={project.githubUrl}
        target="_blank"
        rel="noopener noreferrer"
      >
        {#if project.image}
          <img class="project-image" src={project.image} alt={project.title} />
        {:else}
          <div class="project-placeholder">
            <span class="placeholder-icon">📁</span>
          </div>
        {/if}
        <div class="project-info">
          <h2 class="project-title">{project.title}</h2>
          {#if project.status === "in_progress"}
            <span class="status-badge">{$t("projects_in_progress")}</span>
          {/if}
          {#if project.description}
            <p class="project-description">{project.description}</p>
          {/if}
          <span class="github-link">{$t("projects_github")}</span>
        </div>
      </a>
      {:else}
      <div class="project-card disabled" role="article" aria-label={project.title}>
        {#if project.image}
          <img class="project-image" src={project.image} alt={project.title} />
        {:else}
          <div class="project-placeholder">
            <span class="placeholder-icon">📁</span>
          </div>
        {/if}
        <div class="project-info">
          <h2 class="project-title">{project.title}</h2>
          <span class="status-badge">{$t("projects_in_progress")}</span>
          {#if project.description}
            <p class="project-description">{project.description}</p>
          {/if}
          <span class="github-link muted">{$t("projects_in_progress")}</span>
        </div>
      </div>
      {/if}
      </ScrollReveal>
    {/each}
    </div>
  </main>
  <div class="footer-spacer"></div>
  <Footer />
</div>

<style>
  .page-wrapper {
    background-color: #030027;
    min-height: 100vh;
  }

  :global(body.dark-mode) .page-wrapper {
    background-color: #0d0c1d;
  }

  .spacer {
    height: 10em;
    background-color: #030027;
  }

  .page {
    padding-top: 2em;
  }

  :global(body.dark-mode) .spacer {
    background-color: #0d0c1d;
  }

  .footer-spacer {
    height: 4em;
    background-color: #030027;
  }

  :global(body.dark-mode) .footer-spacer {
    background-color: #0d0c1d;
  }

  .page {
    background-color: #030027;
    min-height: 60vh;
    padding: 0 2rem 2rem;
  }

  :global(body.dark-mode) .page {
    background-color: #0d0c1d;
  }

  .overskrift {
    text-align: center;
    padding: 2em 0 3em;
  }

  .overskrift h1 {
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 2.5em;
    color: #024d98;
    margin: 0 0 0.25em;
  }

  .subtitle {
    font-family: "coolvetica", sans-serif;
    font-size: 1.2em;
    color: #3066be;
    margin: 0;
  }

  :global(body.dark-mode) .overskrift h1 {
    color: #6fa3ff;
  }

  :global(body.dark-mode) .subtitle {
    color: #9ab8ff;
  }

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .project-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: inherit;
    border: 3px solid #024d98;
    border-radius: 20px;
    background-color: #024d98;
    overflow: hidden;
    transition: transform 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
  }

  .project-card:hover {
    transform: scale(1.03);
    background-color: #1e2a4d;
    border-color: #3066be;
  }

  :global(body.dark-mode) .project-card {
    background-color: #1e2a4d;
    border-color: #3066be;
  }

  :global(body.dark-mode) .project-card:hover {
    background-color: #2a3d5a;
    border-color: #6fa3ff;
  }

  .project-image {
    width: 100%;
    height: 12em;
    object-fit: cover;
    background: rgba(0, 0, 0, 0.2);
  }

  .project-placeholder {
    width: 100%;
    height: 12em;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.2);
  }

  .placeholder-icon {
    font-size: 4em;
    opacity: 0.7;
  }

  .project-info {
    padding: 1.25em;
    text-align: center;
    flex: 1;
  }

  .project-title {
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 1.25em;
    font-weight: 600;
    color: white;
    margin: 0 0 0.35em;
    line-height: 1.3;
  }

  .project-description {
    font-family: "coolvetica", sans-serif;
    font-size: 0.95em;
    color: rgba(255, 255, 255, 0.85);
    margin: 0 0 0.75em;
  }

  .github-link {
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 0.9em;
    color: #7fa1ff;
    font-weight: 500;
  }

  .project-card:hover .github-link {
    text-decoration: underline;
  }

  .project-card.disabled {
    cursor: default;
    opacity: 0.9;
  }

  .project-card.disabled:hover {
    transform: none;
  }

  .status-badge {
    display: inline-block;
    margin: 0.25em 0 0.5em;
    padding: 0.25em 0.6em;
    border-radius: 999px;
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 0.75em;
    font-weight: 600;
    letter-spacing: 0.02em;
    background: rgba(255, 255, 255, 0.15);
    color: rgba(255, 255, 255, 0.95);
  }

  .github-link.muted {
    text-decoration: none;
    opacity: 0.85;
  }

  :global(body.dark-mode) .project-title {
    color: #f0f0f0;
  }

  :global(body.dark-mode) .project-description {
    color: rgba(240, 240, 240, 0.85);
  }

  @media (max-width: 640px) {
    .projects-grid {
      grid-template-columns: 1fr;
    }

    .spacer {
      height: 6em;
    }
  }
</style>
