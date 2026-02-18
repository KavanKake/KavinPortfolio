<script>
    import Footer from "$lib/Components/Footer.svelte";
    import LoadingScreen from "$lib/Components/LoadingScreen.svelte";


  import { onMount } from "svelte";

  let isLoading = true;

  onMount(async () => {
    // Simuler lasting (erstatt med ekte data/komponent-load)
    await new Promise((res) => setTimeout(res, 2000));
    isLoading = false;
  });


import { projects } from '$lib/Components/projects.js';

  // Klon første og siste
  const extended = [
    projects[projects.length - 1],
    ...projects,
    projects[0]
  ];

  let index = 1;
  let transitioning = true;

  function next() {
    transitioning = true;
    index += 1;
  }

  function prev() {
  if (index === 1) {
    // Gå til klonen bakerst først (med animasjon)
    transitioning = true;
    index = 0;

    // Etter animasjonen: hopp til ekte siste slide
    setTimeout(() => {
      transitioning = false;
      index = extended.length - 2;
    }, 400); // samme som transition-tiden
  } else {
    transitioning = true;
    index -= 1;
  }
}

  function handleTransitionEnd() {
    // Hopper uten animasjon når vi er på kloner
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

<LoadingScreen {isLoading} />

{#if isLoading}
    <LoadingScreen class="loading-screen" message="Please wait while we load the app..." />
{:else}

<main>
    <div class="space"></div>
    <div class="backgroundtext">
        <h1>Kavin</h1>
        <h1>Lokeswaran</h1>
    </div>
    <div class="frontpage1">
        <div class="title">
            <h1 class="title_text">Hi, and welcome to my Portfolio</h1>
        </div>



    </div>
    <div class="projects">
        <div class="projectHeader">
            <h1>Projects</h1>
            <h2>Here are some featured projects</h2>
        </div>
        <div class="carousel">
        <button class="arrow left" on:click={prev}>◀</button>

        <div
        class="track"
        style="
            transform: translateX(-{index * 100}%);
            transition: {transitioning ? 'transform 0.4s ease' : 'none'};
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

  <button class="arrow right" on:click={next}>▶</button>
</div>
    </div>
    <div class="footer-space"></div>
    
    <Footer/>
</main>

{/if}

<style>
    :global(body) {
        background-color: white;
    }

    :global(body.dark-mode) {
        background-color: #0d0c1d;
    }


    main {
        background-color: #030027;
    }

    :global(body.dark-mode) main {
        background-color: #0d0c1d;
    }

    :global(body), :global(body.dark-mode), main, :global(body.dark-mode) main {
    transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out;
}



    .frontpage1 {
        display: flex;
        flex-direction: column;
        height: 85vh;
        gap: 20em;
        padding-top: 2em;
        border-bottom: #024D98 10px solid;
    }

    :global(body.dark-mode) .frontpage1 {
        background-color: #0d0c1d;
    }

    .space {
        height: 15vh;
    }

    .title {
       font-family: "alphabet-soup-pro", sans-serif;
        font-size: 2em;
        color: #024D98;
        font-weight: 600;
    }

    .title_text{
        margin-top: 0.5em;
        text-align: center;
        align-items: center;
        justify-content: center;
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
        height: 85vh;
    }

    .projectHeader{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0em;
        font-size: 1.5em;
        padding-top: 2em;
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

    @media (max-width: 1167px) {
        .frontpage1 {
            gap: 1em;
            margin-left: 0;
        }

    }

  


@media (max-width: 1090px) {
    .frontpage1 {
        flex-direction: column;
        gap: 0em;
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
    height: 85%;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 3rem;
    color: #030027;
    padding: 2rem;
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



