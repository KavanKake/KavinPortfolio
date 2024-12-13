<script>
    import Footer from "$lib/Components/Footer.svelte";

</script>


<div class="spacer"></div>

<div class="projectspage">
    <div class="overskrift">
        <div class="tekst">
            <h1>Python</h1>
        </div>
        <div class="backbutton">
                <img  src="/assets/Goback.png" class="goback_logo" alt="Go back">
                <a class="goback" href="/projects"> Go Back</a>
        </div>
    </div>

    <div class="mini_spacer"></div>
    <div class="projects">
        <div class="Python">
            <button>
                <a href="/projects/python/basic_python">Basic Python</a>
            </button>
        </div>

        <div class="html">
            <button>
                <a href="/projects/python/python_games">Python games</a>
            </button>
        </div>
    </div>

</div>


<div class="mini_spacer"></div>



<Footer/>
<style>
.spacer{
    height: 10em;
}

:global(body.dark-mode) .spacer {
    background-color: black;
}

.mini_spacer{
    height: 2.5em;
    width: 100%;
}

:global(body.dark-mode) .mini_spacer {
    background-color: black;
}

.projectspage{
    display: flex;
    flex-direction: column;
    padding-left: 2em;
    font-family: coolvetica;
    padding-bottom: 5em;

}

:global(body.dark-mode) .projectspage {
    background-color: black;
}



.overskrift{
    display: flex;
    flex-direction: row;
    font-size: 2.5em;
    font-family: "industry-inc-stencil", sans-serif;
    gap: 1em;
    width: fit-content;
}


button{
    text-decoration: none;
    list-style: none;
    background: transparent;
    border: #024D98 3px solid;
    border-radius: 10px;  
    padding: 0.5em;  
    width: fit-content;
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
    width: fit-content;
}

.goback_logo{
    height: 1em;
    width: auto;
}

:global(body.dark-mode) .goback_logo {
    filter: invert(1);
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

.goback{
    text-decoration: none;
    color: black;
    font-family: coolvetica;
    font-size: 0.5em;
    letter-spacing: 0.1em;
    padding: 0;
    width: fit-content;
}

:global(body.dark-mode) .goback {
    color: white;
}


.goback:hover{
    color: #024D98;
    text-decoration: underline;
}

.backbutton{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
}



h1{
    margin: 0;
}  

:global(body.dark-mode) h1 {
    color: white;
}

@media (max-width: 480px) {
    .overskrift{
        display: flex;
        flex-direction: column;
        gap: 0;
        padding-top: 2em;
    }
    .projectspage{
        overflow-x: hidden;
    }
}
</style>