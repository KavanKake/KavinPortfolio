<script>
  import { onMount } from "svelte";

  let { once = true, delay = 0, threshold = 0.1, children } = $props();

  /** @type {HTMLElement} */
  let el;
  let visible = $state(false);

  onMount(() => {
    if (!el || !("IntersectionObserver" in window)) {
      visible = true;
      return;
    }
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            if (delay > 0) setTimeout(() => (visible = true), delay);
            else visible = true;
            if (once) observer.unobserve(entry.target);
          } else if (!once) {
            visible = false;
          }
        }
      },
      { threshold, rootMargin: "0px 0px -40px 0px" }
    );
    observer.observe(el);
    return () => observer.disconnect();
  });
</script>

<div class="reveal" class:visible bind:this={el}>
  {@render children?.()}
</div>

<style>
  .reveal {
    opacity: 0;
    transform: translateY(24px);
    transition:
      opacity 0.6s ease-out,
      transform 0.6s ease-out;
  }
  .reveal.visible {
    opacity: 1;
    transform: none;
  }
  /* Uten JS: vis alt */
  :global(html:not(.js)) .reveal {
    opacity: 1;
    transform: none;
  }
</style>
