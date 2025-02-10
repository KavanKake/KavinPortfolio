<script>
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
    height: 17em;
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
</style>