import adapter from '@sveltejs/adapter-static';


const dev = process.argv.includes('dev');

/** @type {import('@sveltejs/kit').Config} */
const config = {

	kit: {
	  adapter: adapter(	{
		pages: 'build',
		assets: 'build',
		// GitHub Pages viser 404.html for ukjente adresser – den laster appen og viser src/routes/+error.svelte
		fallback: '404.html'
	  }),
      paths: {
        base: dev ? '' : process.env.BASE_PATHS,
      },
	  appDir: 'internal',
	}
};

export default config;



