<script>
  import Footer from "$lib/Components/Footer.svelte";
  import LoadingScreen from "$lib/Components/LoadingScreen.svelte";
  import { onMount } from "svelte";
  import { projects } from "$lib/Components/projects.js";
  import { t } from "$lib/i18n";
  import ScrollReveal from "$lib/Components/ScrollReveal.svelte";

  let isLoading = $state(true);

  onMount(async () => {
    await new Promise((res) => setTimeout(res, 2000));
    isLoading = false;
  });

  const extended = [
    projects[projects.length - 1],
    ...projects,
    projects[0]
  ];

  let index = $state(1);
  let transitioning = $state(true);

  function next() {
    transitioning = true;
    index += 1;
  }

  function prev() {
    if (index === 1) {
      transitioning = true;
      index = 0;
      setTimeout(() => {
        transitioning = false;
        index = extended.length - 2;
      }, 400);
    } else {
      transitioning = true;
      index -= 1;
    }
  }

  function handleTransitionEnd() {
    if (index === extended.length - 1) {
      transitioning = false;
      index = 1;
    }
    if (index === 0) {
      transitioning = false;
      index = extended.length - 2;
    }
  }
</script>

{#if isLoading}
  <LoadingScreen {isLoading} />
{:else}

<main>
  <div class="space"></div>
  <div class="backgroundtext" aria-hidden="true">
    <h1>Kavin</h1>
    <h1>Lokeswaran</h1>
  </div>
  <ScrollReveal>
    <div class="frontpage1">
      <div class="title">
        <h1 class="title_text">{$t("home_welcome")}</h1>
      </div>
    </div>
  </ScrollReveal>
  <div class="projects" id="projects">
    <ScrollReveal delay={150}>
      <div class="projectHeader">
        <h1>{$t("home_projects")}</h1>
        <h2>{$t("home_featured")}</h2>
      </div>
    </ScrollReveal>
    <div class="carousel">
      <button class="arrow left" type="button" on:click={prev} aria-label={$t("home_prev")}>◀</button>
      <div
        class="track"
        style="
          transform: translateX(-{index * 100}%);
          transition: {transitioning ? "transform 0.4s ease" : "none"};
        "
        on:transitionend={handleTransitionEnd}
      >
        {#each extended as project}
          <div class="slide">
            <div class="card">
              <img class="project-image" src={project.image} alt={project.title} />
              <h3>{project.title}</h3>
            </div>
          </div>
        {/each}
      </div>
      <button class="arrow right" type="button" on:click={next} aria-label={$t("home_next")}>▶</button>
    </div>
  </div>
  <div class="footer-space"></div>
  <Footer />
</main>

{/if}

<style>
    main {
        background-color: #030027;
    }

    .frontpage1 {
        display: flex;
        flex-direction: column;
        min-height: 70vh;
        gap: 4em;
        padding: 4em 1.5em 3em;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        position: relative;
    }

    .frontpage1::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 10px;
        background-color: #024D98;
    }

    .space {
        height: 15vh;
    }

    .title {
       font-family: "alphabet-soup-pro", sans-serif;
        font-size: 2em;
        color: #024D98;
        font-weight: 600;
        position: relative;
        z-index: 10;
    }

    .title_text{
        margin-top: 0.5em;
        text-align: center;
        align-items: center;
        justify-content: center;
        position: relative;
        z-index: 10;
    } 

    .backgroundtext {
    position: fixed; /* 👈 viktig */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    
    font-size: 5em;
    color: #3066BE;
    opacity: 0.25;

    font-family: "alphabet-soup-pro", sans-serif;
    font-weight: 400;

    user-select: none;
    pointer-events: none;

    z-index: 0;
    text-align: center;
}


    .projects{
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 70vh;
        padding-top: 2em;
    }

    .projectHeader{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0em;
        font-size: 1.5em;
        padding-top: 0;
        padding-bottom: 2em;
        font-family: "coolvetica";
        font-weight: 600;
        color: #024D98;
    }


    h1 {
        font-family: "alphabet-soup-pro", sans-serif;
        margin: 0;
    }

    h2 {
        font-family: "coolvetica", sans-serif;
        margin: 0;
        font-weight: 400;
    }

    @media (max-width: 1200px) {
        .backgroundtext {
            font-size: 4.2em;
        }
    }

    @media (max-width: 900px) {
        .space {
            height: 12vh;
        }
        .backgroundtext {
            font-size: 3.5em;
        }
        .frontpage1 {
            padding: 3em 1.25em 2.5em;
            gap: 2em;
        }
        .projects {
            padding: 2.5em 1.25em 2.5em;
        }
        .card {
            width: 75%;
            font-size: 2rem;
            padding: 1.5rem;
            min-height: 350px;
        }
        .title {
            font-size: 1.6em;
        }
    }

    @media (max-width: 600px) {
        .space {
            height: 10vh;
        }
        .backgroundtext {
            font-size: 2.5em;
        }
        .card {
            width: 85%;
            font-size: 1.5rem;
            padding: 1.25rem;
            min-height: 300px;
        }
        .title {
            font-size: 1.4em;
        }
        .projectHeader {
            font-size: 1.2em;
        }
    }

    @media (max-width: 400px) {
        .backgroundtext {
            font-size: 2em;
        }
    }


    .carousel {
  position: relative;
  overflow: hidden;
  width: 100%;
}

.track {
  display: flex;
}

.slide {
  min-width: 100%;
  display: flex;
  justify-content: center;
}

.card {
    background: #4a6fb3;
    padding: 2rem;
    width: 40%;
    min-height: 400px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 3rem;
    color: #030027;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.card img {
  width: 100%;
  height: auto;
  border-radius: 6px;
  background-color: white;
}

.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #7fa1ff;

  z-index: 10;          /* 👈 VIKTIG */
  pointer-events: auto; /* 👈 SIKKERHET */
}

.left { left: 1rem; }
.right { right: 1rem; }

.footer-space {
    height: 10vh;
}




</style>



