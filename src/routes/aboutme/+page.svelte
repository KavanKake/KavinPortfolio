<script>
  import Footer from "$lib/Components/Footer.svelte";
  import LoadingScreen from "$lib/Components/LoadingScreen.svelte";
  import { onMount } from "svelte";
  import { t } from "$lib/i18n";
  import ScrollReveal from "$lib/Components/ScrollReveal.svelte";

  let isLoading = $state(true);

  onMount(() => {
    const id = setTimeout(() => {
      isLoading = false;
    }, 750);
    return () => clearTimeout(id);
  });
</script>

{#if isLoading}
    <LoadingScreen {isLoading} />
{:else}

<main class="about-page">
  <div class="spacer"></div>
  <div class="aboutme">
    <ScrollReveal>
      <div class="section_1">
        <div class="container">
          <img src="/assets/OmmegBilde.png" alt="Kavin Lokeswaran" />
        </div>
      </div>
    </ScrollReveal>
    
    <div class="section_2">
      <ScrollReveal delay={100}>
        <div class="overskrift">
                <h1>{$t("about_title")}</h1>
            </div>
            <div class="underoverskrift">
                <h3>{$t("about_subtitle")}</h3>
            </div>
    
            <div class="tekst">
          <p>{$t("about_paragraph")}</p>
        </div>
      </ScrollReveal>
      <ScrollReveal delay={200}>
        <div class="skole">
                <div class="barneskole">
                    <div class="barneskole-icon">
                        <img class="icon" src="/assets/skoleicon.png" alt="icon">
                    </div>
                    <div class="barneskole-tekst">
                        <h4>{$t("about_school_mortensrud")}</h4>
                        <p>{$t("about_school_mortensrud_years")}</p>
                    </div>
                </div>
    
                <i class="arrow"></i>
    
                <div class="ungdomskole">
                    <div class="ungdomskole-icon">
                        <img class="icon" src="/assets/skoleicon.png" alt="icon">
                    </div>
                    <div class="ungdomskole-tekst">
                        <h4>{$t("about_school_lofsrud")}</h4>
                        <p>{$t("about_school_lofsrud_years")}</p>
                    </div>
                </div>
    
                <i class="arrow"></i>
    
                <div class="vgs">
                    <div class="vgs-icon">
                        <img class="icon" src="/assets/skoleicon.png" alt="icon">
                    </div>
                    <div class="vgs-tekst">
                        <h4>{$t("about_school_elvebakken")}</h4>
                        <p>{$t("about_school_elvebakken_years")}</p>
                    </div>
                </div>
        </div>
      </ScrollReveal>
    </div>
  </div>
  <div class="mini_spacer"></div>
  <Footer />
</main>

{/if}




<style>


    .spacer{
        height: 10em;
    }

    :global(body.dark-mode) .spacer {
        background-color: #0d0c1d;
    }

    .mini_spacer{
        height: 5.5em;
    }

    :global(body.dark-mode) .mini_spacer {
        background-color: #0d0c1d;
    }

    .aboutme{
        display: flex;
        flex-direction: row;
        gap: 7.5em;
    }

    main {
        background-color: #030027;
        overflow-y: auto;
    }

    :global(body.dark-mode) main {
        background-color: #0d0c1d;
    }


    :global(body.dark-mode) .aboutme {
        background-color: #0d0c1d;
    }

    .section_1{
        display: flex;
        margin-left: 1em;
        align-items: center;
    }

    .container {
        display: flex;
        width: 32em;
        max-width: 90vw;
        height: 42em;
        border: 3px solid #024D98;
        border-radius: 20px;
        overflow: hidden;
        z-index: 0;
    }

    .container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 18px;
    }

    .about-page {
        font-family: "coolvetica", sans-serif;
    }

    .overskrift {
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 2.5em;
        font-family: "alphabet-soup-pro", sans-serif;
        color: #ffffff;
    }

    :global(body.dark-mode) .overskrift {
        color: #ffffff;
    }

    .underoverskrift {
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 1.75em;
        font-family: "alphabet-soup-pro", sans-serif;
        font-weight: 500;
        color: #e8e8e8;
    }

    .tekst {
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 1.25rem;
        line-height: 1.6;
        width: 90%;
        font-family: "coolvetica", sans-serif;
        font-weight: 400;
        color: #ffffff;
    }

    :global(body.dark-mode) .tekst {
        color: #ffffff;
    }

    h1{
        margin: 0;
    }

    h3{
        margin: 0;
    }

    h4{
        margin: 0;
    }

    .icon{
        width: 3.25em;
        height: auto;
        margin-right: 0.5em;
        border: #024D98 3px solid;
        padding: 5px;
        border-radius: 50%;
        filter: brightness(0) invert(1);
    }

    .barneskole,
    .ungdomskole,
    .vgs {
        display: flex;
        flex-direction: column;
        font-size: 1.05em;
        font-family: "coolvetica", sans-serif;
        color: #ffffff;
    }

    :global(body.dark-mode) .barneskole,
    :global(body.dark-mode) .ungdomskole,
    :global(body.dark-mode) .vgs {
        color: #ffffff;
    }

    .vgs {
        width: fit-content;
    }

    .arrow{
        border: solid #024D98;
        border-width: 0 3px 3px 0;
        display: inline-block;
        padding: 3px;
        transform: rotate(-45deg);
        -webkit-transform: rotate(-45deg);
        margin-left: 1em;
        margin-right: 1em;
        scale: 1.2;
    }

    .skole{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
        width: 100%;
        margin-right: 0;
        margin-top: 2.5em;
        gap: 1.25em;
    }

    /* Apply smooth transition to dark mode changes */
:root, :global(body.dark-mode) {
    transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out, filter 0.5s ease-in-out;
}

.spacer, .mini_spacer, main, .aboutme, .overskrift, .tekst, .icon, .barneskole, .ungdomskole, .vgs {
    transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out, filter 0.5s ease-in-out;
}

/* Add fade-in effect when switching themes */
:global(body.dark-mode) {
    animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0.8;
    }
    to {
        opacity: 1;
    }
}

    

    @media (max-width: 1000px) {
        .aboutme{
            flex-direction: column;
            gap: 1em;
            justify-content: center;
            align-items: center;
        }

        .section_2{
            margin-left: 1em;
            margin-right: 1em;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .container {
            scale: 1;
            width: min(32em, 92vw);
            height: 34em;
            justify-content: center;
        }

        .section_1{
            margin-left: 0em;

        }

        .tekst{
            width: 100%;
            text-align: center;
        }

        .skole{
            scale: 0.7;
        }

        .underoverskrift{
            text-align: center;
        }

        .overskrift{
            text-align: center;
        }
    }
</style>


