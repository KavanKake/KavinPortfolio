<!-- <script>
    import Footer from "$lib/Components/Footer.svelte";
</script>



<div class="spacer"></div>

<div class="projectspage">
    <div class="overskrift">
        <h1>My projects</h1>
    </div>
    <div class="mini_spacer1"></div>
    <div class="projects">
        <div class="Python">
            <button>
                <a href="/projects/python">Python</a>
            </button>
        </div>

        <div class="html">
            <button>
                <a href="/projects/HTML,CSS,JS">HTML, CSS, JS</a>
            </button>
        </div>

        <div class="Other">
            <button>
                <a href="/projects/other">Others</a>
            </button>
        </div>
    </div>

    <div class="mini_spacer"></div>
</div>





<Footer/>
<style>

.spacer{
    height: 10em;
}

:global(body.dark-mode) .spacer {
    background-color: black;
}


.mini_spacer{
    height: 5em;
}

.mini_spacer1{
    height: 2em;
}

:global(body.dark-mode) .mini_spacer {
    background-color: black;
}

.projectspage{
    display: flex;
    flex-direction: column; 
    font-family: coolvetica;
    padding-left: 2.5em; 
    margin: 0;
}

:global(body.dark-mode) .projectspage {
    background-color: black;
}

.overskrift{
    display: flex;
    flex-direction: column;
    font-size: 2.5em;
    font-family: "industry-inc-stencil", sans-serif;
}

:global(body.dark-mode) .overskrift {
    color: white;
}


button{
    text-decoration: none;
    list-style: none;
    background: transparent;
    border: #024D98 3px solid;
    border-radius: 10px;  
    padding: 0.5em;  
}

:global(body.dark-mode) button {
    border: white 3px solid;
}

button:hover{
    background-color: #024D98;
    color: white;
    transform: scale(1.1);
    transition: 0.5s;
}

.projects{
    display: flex;
    flex-direction: column;
    gap: 1.5em;
    font-size: 1.25em;
    font-family: "coolvetica";
    justify-content: space-evenly;
}

a{
    text-decoration: none;
    color: black;
    font-family: coolvetica;
    font-size: 2em;
    padding: 20px;
    letter-spacing: 0.1em;
    width: fit-content;
}

:global(body.dark-mode) a {
    color: white;
}

a:hover{
    color: white;
}

h1{
    margin: 0;
}       

@media (max-width: 480px) {
    .overskrift{
        gap: 0.5em;
        font-size: 2em;
    }
    }
</style> -->


<script>
  let darkMode = false;
</script>

<style>


  :root {
    --bg: white;
    --text: black;
    --primary: #1e3a8a;
    --secondary: #f8fafc;
  }



  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: coolvetica;
  }

  :global(body.dark-mode) .container {
    background-color: black;
    color: white;
  }

  .title {
    font-size: 3rem;
    font-weight: bold;
    text-transform: uppercase;
  }

  .button {
    padding: 10px 20px;
    font-size: 1.2rem;
    border: 2px solid var(--primary);
    background: none;
    color: var(--primary);
    border-radius: 8px;
    cursor: pointer;
    margin-top: 20px;
    transition: all 0.3s;
  }

  :global(body.dark-mode) .button {
    border: 2px solid white;
    color: white;
  }

  .button:hover {
    background: var(--primary);
    color: var(--secondary);
  }


</style>

<div class="container">
  <h1 class="title">🚧 Under Construction 🚧</h1>
  <p>We're working hard to launch something amazing. Stay tuned!</p>
  
  <button class="button" on:click={() => alert('You will be notified soon!')}>
    Notify Me
  </button>
</div>



<svelte:head>
  <script>
    document.body.setAttribute('data-theme', 'light');
    document.querySelector('input[type="checkbox"]').addEventListener('change', (e) => {
      document.body.setAttribute('data-theme', e.target.checked ? 'dark' : 'light');
    });
  </script>
</svelte:head>