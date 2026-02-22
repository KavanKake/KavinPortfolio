<script>
  import { onMount } from "svelte";

  /** @type {HTMLElement} */
  let el;
  let visible = $state(false);
  const { once = true, delay = 0, threshold = 0.1 } = $props();

  onMount(() => {
    if (!el) return;
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            if (delay > 0) {
              setTimeout(() => (visible = true), delay);
            } else {
              visible = true;
            }
            if (once && el) observer.unobserve(el);
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
  <slot />
</div>

<style>
  .reveal {
    opacity: 0;
    transform: translateY(28px);
    transition:
      opacity 0.6s ease-out,
      transform 0.6s ease-out;
  }

  .reveal.visible {
    opacity: 1;
    transform: translateY(0);
  }
</style>
