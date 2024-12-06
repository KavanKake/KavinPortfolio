<script>
    import Footer from "$lib/Components/Footer.svelte";

    import goback from "$lib/assets/Goback.png";
</script>


<div class="spacer"></div>

<div class="projectspage">
    <div class="overskrift">
        <div class="tekst">
            <h1>Python</h1>
        </div>
        <div class="backbutton">
                <img src="{goback}" class="goback_logo" alt="Go back">
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
    height: 5em;
}

.mini_spacer{
    height: 2.5em;
}

.projectspage{
    display: flex;
    flex-direction: column;
    margin-left: 2em;
    font-family: coolvetica;
    margin-top: 5em;
    margin-bottom: 5em;
    width: 100%;

}

.overskrift{
    display: flex;
    flex-direction: row;
    font-size: 2.5em;
    font-family: "industry-inc-stencil", sans-serif;
    gap: 1em;
}


button{
    text-decoration: none;
    list-style: none;
    background: transparent;
    border: #024D98 3px solid;
    border-radius: 10px;  
    padding: 0.5em;  
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

.goback_logo{
    height: 1em;
    width: auto;
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

@media (max-width: 480px) {
    .overskrift{
        display: flex;
        flex-direction: column;
        gap: 0;
    }
    .projectspage{
        margin-left: 0.5em;
        overflow-x: hidden;
    }
}
</style>