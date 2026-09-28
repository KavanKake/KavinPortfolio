<script>
  import { t, locale } from "$lib/i18n";
  import { isNew, timeAgo, languageColors } from "$lib/github.js";
  import Icon from "$lib/Components/Icon.svelte";

  let { repo } = $props();
</script>

<article class="card repo">
  <div class="top">
    <Icon name="folder" size={20} />
    <div class="icons">
      {#if repo.homepage}
        <a href={repo.homepage} target="_blank" rel="noopener noreferrer" aria-label="{$t('project_live')}: {repo.title}">
          <Icon name="external" size={18} />
        </a>
      {/if}
      <a href={repo.url} target="_blank" rel="noopener noreferrer" aria-label="GitHub: {repo.title}">
        <Icon name="github" size={18} />
      </a>
    </div>
  </div>

  <h3>
    <a class="stretched" href={repo.url} target="_blank" rel="noopener noreferrer">{repo.title}</a>
    {#if isNew(repo)}
      <span class="tag tag-accent new">{$t("gh_new")}</span>
    {/if}
  </h3>
  <p class:muted={!repo.description}>{repo.description ?? $t("gh_no_desc")}</p>

  {#if repo.topics.length}
    <ul class="tags">
      {#each repo.topics.slice(0, 4) as topic}
        <li class="tag">{topic}</li>
      {/each}
    </ul>
  {/if}

  <div class="meta">
    {#if repo.language}
      <span class="lang">
        <span class="dot" style="background:{languageColors[repo.language] ?? 'var(--accent)'}"></span>
        {repo.language}
      </span>
    {/if}
    {#if repo.stars > 0}
      <span><Icon name="star" size={14} /> {repo.stars}</span>
    {/if}
    <span class="time"><Icon name="clock" size={14} /> {$t("gh_updated")} {timeAgo(repo.pushedAt, $locale)}</span>
  </div>
</article>

<style>
  .repo {
    position: relative;
    padding: 22px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    height: 100%;
  }
  .repo:hover {
    transform: translateY(-3px);
    border-color: var(--border-strong);
    box-shadow: var(--shadow);
  }
  .top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: var(--accent);
  }
  .icons {
    display: flex;
    gap: 10px;
    position: relative;
    z-index: 2;
  }
  .icons a {
    color: var(--text-muted);
    display: inline-flex;
  }
  .icons a:hover {
    color: var(--text);
  }
  h3 {
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }
  .stretched {
    color: var(--text);
    text-decoration: none;
  }
  .stretched::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
  }
  .repo:hover .stretched {
    color: var(--accent);
  }
  .new {
    font-size: 0.7rem;
    padding: 0.15em 0.55em;
  }
  p {
    color: var(--text-muted);
    font-size: 0.93rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  p.muted {
    color: var(--text-faint);
    font-style: italic;
  }
  .tags {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .meta {
    margin-top: auto;
    padding-top: 8px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px 16px;
    font-size: 0.82rem;
    color: var(--text-faint);
  }
  .meta span {
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }
</style>
