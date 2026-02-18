<script>
  import { fade } from "svelte/transition";
  import { onMount } from "svelte";

  export let isLoading = true;
</script>

{#if isLoading}
  <div class="loading-wrapper" transition:fade={{ duration: 600 }}>
    <div class="content">
      <h1>KAVIN LOKESWARAN</h1>
      <div class="loader">
        <div class="bar"></div>
      </div>
    </div>
  </div>
{/if}

<style>
  .loading-wrapper {
    position: fixed;
    inset: 0;
    background: #05061a; /* mørk blå som i bildene */
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
  }

  .content {
    text-align: center;
  }

  h1 {
    font-family: "alphabet-soup-pro", sans-serif;
    font-size: 2.5rem;
    letter-spacing: 0.05em;
    color: #6fa3ff; /* blå tekst */
    margin-bottom: 1.5rem;
  }

  .loader {
    width: 280px;
    height: 4px;
    background: rgba(111, 163, 255, 0.25);
    overflow: hidden;
    border-radius: 2px;
    margin: 0 auto;
  }

  .bar {
    width: 40%;
    height: 100%;
    background: #6fa3ff;
    animation: slide 1.6s ease-in-out infinite;
    border-radius: 2px;
  }

  @keyframes slide {
    0% {
      transform: translateX(-100%);
    }
    50% {
      transform: translateX(150%);
    }
    100% {
      transform: translateX(-100%);
    }
  }
</style>