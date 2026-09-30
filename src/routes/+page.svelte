<script>
  import { onMount } from "svelte";
  import { t, locale } from "$lib/i18n";
  import { skills, links } from "$lib/data/profile.js";
  import { curatedProjects } from "$lib/data/projects.js";
  import { github, loadRepos, timeAgo } from "$lib/github.js";
  import ScrollReveal from "$lib/Components/ScrollReveal.svelte";
  import ProjectCard from "$lib/Components/ProjectCard.svelte";
  import RepoCard from "$lib/Components/RepoCard.svelte";
  import Icon from "$lib/Components/Icon.svelte";
  import ActivityGraph from "$lib/Components/ActivityGraph.svelte";

  const featured = curatedProjects.filter((p) => p.featured);
  const latest = $derived($github.repos.slice(0, 6));
  const lastActive = $derived($github.repos[0]?.pushedAt ?? null);

  onMount(loadRepos);

  const values = [
    { icon: "zap", t: "value_1_t", d: "value_1_d" },
    { icon: "target", t: "value_2_t", d: "value_2_d" },
    { icon: "users", t: "value_3_t", d: "value_3_d" }
  ];
</script>

<!-- ============ HERO ============ -->
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-text">
      <span class="status"><span class="pulse"></span>{$t("hero_available")}</span>
      <p class="eyebrow">{$t("hero_eyebrow")}</p>
      <h1>
        <span class="hi">{$t("hero_hi")}</span>
        <span class="name">Kavin Lokeswaran</span>
      </h1>
      <p class="headline">{$t("hero_title")}</p>
      <p class="pitch">{$t("hero_pitch")}</p>

      <div class="cta">
        <a class="btn btn-primary" href="/projects">
          {$t("hero_cta_projects")}
          <Icon name="arrow" />
        </a>
        <a class="btn btn-ghost" href="/contactme">
          <Icon name="mail" />
          {$t("hero_cta_contact")}
        </a>
        <a class="icon-btn" href={links.github} target="_blank" rel="noopener noreferrer" aria-label="GitHub">
          <Icon name="github" size={20} />
        </a>
        {#if links.linkedin}
          <a class="icon-btn" href={links.linkedin} target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            <Icon name="linkedin" size={20} />
          </a>
        {/if}
      </div>
    </div>

    <div class="hero-visual" aria-hidden="true">
      <div class="glow"></div>
      <img class="logo-bg" src="/assets/Kavin_logo.svg" alt="" />
      <div class="code card always-dark">
        <div class="code-bar">
          <span class="dotc r"></span><span class="dotc y"></span><span class="dotc g"></span>
          <span class="file">kavin.js</span>
        </div>
        <pre><code><span class="k">const</span> <span class="v">kavin</span> = {"{"}
  <span class="p">{$locale === "no" ? "studerer" : "studying"}</span>: <span class="s">"{$t("edu_bachelor")}"</span>,
  <span class="p">{$locale === "no" ? "år" : "years"}</span>: <span class="s">"2026 – 2029"</span>,
  <span class="p">stack</span>: [<span class="s">"JavaScript"</span>, <span class="s">"Svelte"</span>,
          <span class="s">"Node"</span>, <span class="s">"Python"</span>],
  <span class="p">{$locale === "no" ? "base" : "location"}</span>: <span class="s">"Oslo"</span>,
  <span class="p">{$locale === "no" ? "åpenForJobb" : "openToWork"}</span>: <span class="b">true</span>
{"}"};</code></pre>
      </div>
    </div>
  </div>

  <!-- Faktarad -->
  <div class="container">
    <dl class="facts card">
      <div>
        <dt>
          {#if $github.status === "ready"}{$github.repos.length}{:else}–{/if}
        </dt>
        <dd>{$t("stat_repos")}</dd>
      </div>
      <div>
        <dt>{lastActive ? timeAgo(lastActive, $locale) : "–"}</dt>
        <dd>{$t("stat_last")}</dd>
      </div>
      <div>
        <dt><Icon name="pin" size={18} /> Oslo</dt>
        <dd>{$t("stat_location")}</dd>
      </div>
      <div>
        <dt><Icon name="globe" size={18} /> NO / EN</dt>
        <dd>{$t("stat_languages")}</dd>
      </div>
    </dl>
  </div>
</section>

<!-- ============ FERDIGHETER ============ -->
<section class="section" id="skills">
  <div class="container">
    <ScrollReveal>
      <div class="section-head">
        <div>
          <p class="eyebrow">{$t("skills_eyebrow")}</p>
          <h2 class="section-title">{$t("skills_title")}</h2>
          <p class="section-lead">{$t("skills_lead")}</p>
        </div>
        <ul class="legend" aria-hidden="true">
          <li><span class="lvl l3"></span>{$t("level_3")}</li>
          <li><span class="lvl l2"></span>{$t("level_2")}</li>
          <li><span class="lvl l1"></span>{$t("level_1")}</li>
        </ul>
      </div>
    </ScrollReveal>

    <div class="skills-grid">
      {#each skills as group, i}
        <ScrollReveal delay={i * 80}>
          <div class="card skill-card">
            <h3>{$t(`skills_${group.key}`)}</h3>
            <ul>
              {#each group.items as s}
                <li>
                  <span>{s.name}</span>
                  <span class="meter" title={$t(`level_${s.level}`)}>
                    <span class="sr-only">{$t(`level_${s.level}`)}</span>
                    {#each [1, 2, 3] as n}
                      <span class="seg" class:on={n <= s.level}></span>
                    {/each}
                  </span>
                </li>
              {/each}
            </ul>
          </div>
        </ScrollReveal>
      {/each}
    </div>
  </div>
</section>

<!-- ============ UTVALGTE PROSJEKTER ============ -->
<section class="section alt" id="projects">
  <div class="container">
    <ScrollReveal>
      <div class="section-head">
        <div>
          <p class="eyebrow">{$t("featured_eyebrow")}</p>
          <h2 class="section-title">{$t("featured_title")}</h2>
          <p class="section-lead">{$t("featured_lead")}</p>
        </div>
        <a class="btn btn-ghost" href="/projects">{$t("featured_all")} <Icon name="arrow" /></a>
      </div>
    </ScrollReveal>

    <div class="featured-grid" class:single={featured.length === 1}>
      {#each featured as project, i}
        <ScrollReveal delay={i * 90}>
          <ProjectCard {project} large={i === 0} horizontal={featured.length === 1} />
        </ScrollReveal>
      {/each}
    </div>
  </div>
</section>

<!-- ============ GITHUB (AUTOMATISK) ============ -->
<section class="section" id="github">
  <div class="container">
    <ScrollReveal>
      <div class="section-head">
        <div>
          <p class="eyebrow"><span class="live-dot"></span>{$t("gh_eyebrow")}</p>
          <h2 class="section-title">{$t("gh_title")}</h2>
          <p class="section-lead">{$t("gh_lead")}</p>
        </div>
        <a class="btn btn-ghost" href={links.github} target="_blank" rel="noopener noreferrer">
          <Icon name="github" />
          {$t("gh_profile")}
        </a>
      </div>
    </ScrollReveal>

    <ScrollReveal>
      <ActivityGraph />
    </ScrollReveal>

    {#if $github.status === "ready" && latest.length}
      <div class="repo-grid">
        {#each latest as repo (repo.name)}
          <RepoCard {repo} />
        {/each}
      </div>
    {:else if $github.status === "ready" || $github.status === "error"}
      <p class="empty card">
        {$github.status === "error" ? $t("gh_error") : $t("gh_empty")}
        <a href={links.github} target="_blank" rel="noopener noreferrer">github.com/KavanKake</a>
      </p>
    {:else}
      <div class="repo-grid" aria-busy="true" aria-label={$t("gh_loading")}>
        {#each Array(3) as _}
          <div class="card skeleton"></div>
        {/each}
      </div>
    {/if}
  </div>
</section>

<!-- ============ OM MEG ============ -->
<section class="section alt" id="about">
  <div class="container about-grid">
    <ScrollReveal>
      <div class="card now">
        <h3><span class="live-dot"></span>{$t("now_title")}</h3>
        <dl>
          <div>
            <dt><Icon name="school" size={18} /> {$t("now_study")}</dt>
            <dd>{$t("edu_bachelor")}<span>{$t("edu_bachelor_sub")} · 2026 – 2029</span></dd>
          </div>
          <div>
            <dt><Icon name="code" size={18} /> {$t("now_focus")}</dt>
            <dd>{$t("now_focus_v")}</dd>
          </div>
          <div>
            <dt><Icon name="target" size={18} /> {$t("now_open")}</dt>
            <dd>{$t("now_open_v")}</dd>
          </div>
          <div>
            <dt><Icon name="check" size={18} /> {$t("edu_done")}</dt>
            <dd>{$t("edu_elvebakken")}<span>{$t("edu_elvebakken_sub")} · 2023 – 2026</span></dd>
          </div>
        </dl>
      </div>
    </ScrollReveal>
    <ScrollReveal delay={100}>
      <div>
        <p class="eyebrow">{$t("about_eyebrow")}</p>
        <h2 class="section-title">{$t("about_title")}</h2>
        <div class="about-text">
          <p>{$t("about_p1")}</p>
          <p>{$t("about_p2")}</p>
        </div>

        <ul class="values">
          {#each values as v}
            <li>
              <span class="v-icon"><Icon name={v.icon} size={20} /></span>
              <div>
                <strong>{$t(v.t)}</strong>
                <p>{$t(v.d)}</p>
              </div>
            </li>
          {/each}
        </ul>

        <a class="btn btn-ghost" href="/aboutme">{$t("about_more")} <Icon name="arrow" /></a>
      </div>
    </ScrollReveal>
  </div>
</section>

<!-- ============ CTA ============ -->
<section class="section">
  <div class="container">
    <ScrollReveal>
      <div class="cta-band always-dark">
        <img src="/assets/Kavin_logo.svg" alt="" aria-hidden="true" class="cta-logo" />
        <h2>{$t("cta_title")}</h2>
        <p>{$t("cta_lead")}</p>
        <div class="cta">
          <a class="btn btn-primary" href="/contactme">{$t("cta_button")} <Icon name="arrow" /></a>
          <a class="btn btn-ghost" href="mailto:{links.email}"><Icon name="mail" /> {links.email}</a>
        </div>
      </div>
    </ScrollReveal>
  </div>
</section>

<style>
  /* ---------- Hero ---------- */
  .hero {
    padding-top: calc(var(--nav-h) + clamp(24px, 6vw, 72px));
    padding-bottom: 24px;
    position: relative;
    overflow-x: clip;
  }
  .hero-grid {
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    align-items: center;
    gap: 40px;
  }
  .status {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 6px 14px 6px 10px;
    border-radius: 999px;
    background: var(--success-bg);
    border: 1px solid var(--success-border);
    color: var(--on-success);
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 22px;
    width: fit-content;
  }
  .hero-text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  .pulse {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--success);
    box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    70% {
      box-shadow: 0 0 0 10px rgba(74, 222, 128, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(74, 222, 128, 0);
    }
  }
  h1 {
    margin: 14px 0 18px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .hi {
    font-size: clamp(1.1rem, 2vw, 1.35rem);
    color: var(--text-muted);
    font-weight: 500;
  }
  .name {
    font-family: var(--font-brand);
    font-weight: 400;
    font-size: clamp(2.6rem, 7vw, 5rem);
    line-height: 1;
    letter-spacing: 0.01em;
    background: linear-gradient(120deg, var(--name-from) 10%, var(--accent) 55%, var(--brand) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  .headline {
    font-family: var(--font-head);
    font-size: clamp(1.3rem, 2.4vw, 1.75rem);
    font-weight: 600;
    color: var(--text);
    max-width: 24ch;
    margin-bottom: 14px;
    line-height: 1.3;
  }
  .pitch {
    color: var(--text-muted);
    max-width: 56ch;
    font-size: 1.05rem;
  }
  .cta {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 30px;
    align-items: center;
  }
  .icon-btn {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    display: inline-grid;
    place-items: center;
    color: var(--text);
    background: var(--surface);
    border: 1px solid var(--border);
    transition:
      transform 0.2s ease,
      border-color 0.2s ease;
  }
  .icon-btn:hover {
    transform: translateY(-2px);
    border-color: var(--border-strong);
  }

  .hero-visual {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    height: clamp(380px, 44vw, 520px);
  }
  .logo-bg {
    position: absolute;
    height: 88%;
    width: auto;
    top: 2%;
    left: 50%;
    transform: translateX(-50%);
    opacity: var(--logo-opacity);
    filter: drop-shadow(0 0 60px rgba(48, 102, 190, 0.5));
  }
  .glow {
    position: absolute;
    bottom: 10%;
    width: 90%;
    height: 50%;
    background: radial-gradient(ellipse at center, rgba(48, 102, 190, 0.45), transparent 70%);
    filter: blur(20px);
  }
  .code {
    position: relative;
    width: min(100%, 440px);
    margin-bottom: 8%;
    border-radius: 16px;
    background: rgba(5, 8, 48, 0.82);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: var(--shadow);
    overflow: hidden;
    transform: rotate(-2deg);
  }
  .code-bar {
    display: flex;
    align-items: center;
    gap: 7px;
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
  }
  .dotc {
    width: 11px;
    height: 11px;
    border-radius: 50%;
  }
  .dotc.r {
    background: #ff5f57;
  }
  .dotc.y {
    background: #febc2e;
  }
  .dotc.g {
    background: #28c840;
  }
  .file {
    margin-left: 8px;
    font-size: 0.8rem;
    color: var(--text-faint);
    font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  }
  pre {
    margin: 0;
    padding: 18px 20px 22px;
    font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    font-size: 0.84rem;
    line-height: 1.75;
    color: var(--text);
    white-space: pre-wrap;
  }
  .k {
    color: #c792ea;
  }
  .v {
    color: #82aaff;
  }
  .p {
    color: #89ddff;
  }
  .s {
    color: #c3e88d;
  }
  .b {
    color: #f78c6c;
  }

  .facts {
    margin: 36px 0 0;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    padding: 8px;
    border-radius: var(--radius);
  }
  .facts div {
    padding: 16px 20px;
  }
  .facts div + div {
    border-left: 1px solid var(--border);
  }
  dt {
    font-family: var(--font-head);
    font-size: 1.35rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--text);
  }
  dt :global(svg) {
    color: var(--accent);
  }
  dd {
    margin: 2px 0 0;
    color: var(--text-faint);
    font-size: 0.85rem;
  }

  /* ---------- Seksjoner ---------- */
  .alt {
    background: linear-gradient(180deg, transparent, var(--alt-bg) 12%, var(--alt-bg) 88%, transparent);
  }

  /* ---------- Ferdigheter ---------- */
  .legend {
    list-style: none;
    display: flex;
    gap: 16px;
    padding: 0;
    margin: 0;
    color: var(--text-faint);
    font-size: 0.82rem;
  }
  .legend li {
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .lvl {
    display: inline-block;
    width: 22px;
    height: 6px;
    border-radius: 3px;
    background: linear-gradient(90deg, var(--accent) var(--w), var(--track) var(--w));
  }
  .l3 {
    --w: 100%;
  }
  .l2 {
    --w: 66%;
  }
  .l1 {
    --w: 33%;
  }
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
  }
  .skill-card {
    padding: 22px;
    height: 100%;
  }
  .skill-card h3 {
    font-size: 1.05rem;
    margin-bottom: 14px;
    color: var(--accent);
  }
  .skill-card ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    gap: 10px;
  }
  .skill-card li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    font-size: 0.95rem;
  }
  .meter {
    display: inline-flex;
    gap: 3px;
  }
  .seg {
    width: 14px;
    height: 6px;
    border-radius: 3px;
    background: var(--track);
  }
  .seg.on {
    background: var(--accent);
  }

  /* ---------- Prosjekter ---------- */
  .featured-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
  }

  .featured-grid.single {
    grid-template-columns: 1fr;
  }
  .repo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
  }
  .live-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--success);
    display: inline-block;
    animation: pulse 2s infinite;
  }
  .skeleton {
    height: 190px;
    background: linear-gradient(100deg, var(--surface) 30%, var(--surface-2) 50%, var(--surface) 70%);
    background-size: 200% 100%;
    animation: shimmer 1.4s infinite linear;
  }
  @keyframes shimmer {
    to {
      background-position: -200% 0;
    }
  }
  .empty {
    padding: 24px;
    color: var(--text-muted);
  }

  /* ---------- Om meg ---------- */
  .about-grid {
    display: grid;
    grid-template-columns: 0.8fr 1.2fr;
    gap: clamp(32px, 6vw, 72px);
    align-items: center;
  }
  .now {
    padding: 28px;
  }
  .now h3 {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.15rem;
    margin-bottom: 18px;
  }
  .now dl {
    margin: 0;
    display: grid;
  }
  .now dl > div {
    padding: 14px 0;
    border-top: 1px solid var(--border);
  }
  .now dt {
    font-size: 0.78rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-faint);
    gap: 8px;
    margin-bottom: 4px;
    font-family: var(--font-body);
  }
  .now dd {
    margin: 0;
    font-family: var(--font-head);
    font-weight: 600;
    font-size: 1.05rem;
    color: var(--text);
    display: flex;
    flex-direction: column;
  }
  .now dd span {
    font-family: var(--font-body);
    font-weight: 400;
    font-size: 0.88rem;
    color: var(--text-muted);
  }
  .about-text {
    display: grid;
    gap: 14px;
    color: var(--text-muted);
    margin-bottom: 28px;
  }
  .values {
    list-style: none;
    padding: 0;
    margin: 0 0 30px;
    display: grid;
    gap: 16px;
  }
  .values li {
    display: flex;
    gap: 14px;
    align-items: flex-start;
  }
  .v-icon {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    display: grid;
    place-items: center;
    color: var(--accent);
    background: var(--surface-2);
    border: 1px solid var(--border);
    flex-shrink: 0;
  }
  .values strong {
    font-family: var(--font-head);
  }
  .values p {
    color: var(--text-muted);
    font-size: 0.93rem;
  }

  /* ---------- CTA ---------- */
  .cta-band {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: clamp(40px, 7vw, 80px) var(--gutter);
    border-radius: 28px;
    background:
      radial-gradient(600px 300px at 50% 0%, rgba(111, 163, 255, 0.25), transparent 70%),
      linear-gradient(135deg, #0a1a6b, #041046 60%, #030027);
    border: 1px solid var(--border-strong);
  }
  .cta-logo {
    position: absolute;
    right: -40px;
    bottom: -60px;
    height: 280px;
    width: auto;
    opacity: 0.18;
    pointer-events: none;
  }
  .cta-band h2 {
    font-size: clamp(1.9rem, 4.5vw, 3rem);
    margin-bottom: 14px;
  }
  .cta-band p {
    color: var(--text-muted);
    max-width: 52ch;
    margin: 0 auto;
  }
  .cta-band .cta {
    justify-content: center;
  }

  /* ---------- Responsivt ---------- */
  @media (max-width: 1000px) {
    .skills-grid {
      grid-template-columns: repeat(2, 1fr);
    }
    .repo-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  @media (max-width: 860px) {
    .hero-grid {
      grid-template-columns: 1fr;
    }
    .hero-visual {
      height: auto;
      padding: 24px 0 8px;
      justify-content: flex-start;
    }
    .logo-bg {
      height: 120%;
      left: auto;
      right: -10%;
      transform: none;
      top: -10%;
    }
    .code {
      margin-bottom: 0;
      transform: none;
    }
    .facts {
      grid-template-columns: repeat(2, 1fr);
    }
    .facts div {
      padding: 14px 16px;
    }
    dt {
      font-size: 1.05rem;
    }
    .facts div:nth-child(3) {
      border-left: 0;
    }
    .facts div:nth-child(n + 3) {
      border-top: 1px solid var(--border);
    }
    .featured-grid {
      grid-template-columns: 1fr;
    }
    .about-grid {
      grid-template-columns: 1fr;
    }

  }
  @media (max-width: 600px) {
    .skills-grid,
    .repo-grid {
      grid-template-columns: 1fr;
    }
    pre {
      font-size: 0.78rem;
    }
    .cta .btn {
      flex: 1 1 auto;
    }
  }
</style>
