import adapter from '@sveltejs/adapter-static';


const dev = process.argv.includes('dev');

/** @type {import('@sveltejs/kit').Config} */
const config = {

	kit: {
	  adapter: adapter(	{
		pages: 'build',
		assets: 'build',
		fallback: null
	  }),
      paths: {
        base: dev ? '' : process.env.BASE_PATHS,
      },
	  appDir: 'internal',
	}
};

export default config;



