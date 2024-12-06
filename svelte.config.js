import adapter from '@sveltejs/adapter-static';

export default {
  kit: {
    adapter: adapter(),
    paths: {
      base: process.env.NODE_ENV === 'production' ? '/KavinPortfolio' : '',
    },
    prerender: {
      handleMissingId: 'warn', // Optionally add this to handle missing paths gracefully
    },
  },
};
