<script>
    import Footer from "$lib/Components/Footer.svelte";

    
</script>


<div class="spacer"></div>

<div class="projectspage">
    <div class="overskrift">
        <div class="tekst">
            <h1>Basic Python</h1>
        </div>
        <div class="backbutton">
            <img class="goback" src="/assets/Goback.png" alt="Go Back">
            <a href="/projects/python"> Go Back</a>
        </div>
    </div>
        <div class="undertext">
        <h3>Click on file to download</h3>
    </div>

    <div class="mini_spacer"></div>
    <div class="projects">
        <div class="section_1">
            <button>
                <a href="/My_projects/Python/Calculator.py" download="Advanced Calculator">Advanced calculator</a>
            </button>
            <button>
                <a href="/My_projects/Python/bankkonto.py" download="Bank account code">Bank account code</a>
            </button>
            <button>
                <a href="/My_projects/Python/krytpert_kode.py" download="Encryption code">Encryption code</a>
            </button>
            <button>
                <a href="/My_projects/Python/Gjett_tallet.py" download="Guess the number ">Guess the number </a>
            </button>
        </div>
        <div class="section_2">
            <button>
                <a href="/My_projects/Python/Stein, saks, papir-kopi.py" download="Rock, paper, scissors ">Rock, paper, scissors </a>
            </button>
            <button>
                <a href="/My_projects/Python/Dekryptert_melding.py" download="Crypted code">Crypted message</a>
            </button>
            <button>
                <a href="/My_projects/Python/ordsjekk-kopi.py" download="Word checker">Word checker</a>
            </button>
            <button>
                <a href="/My_projects/Python/Primtallsjekk-kopi.py" download="Prime number checker">Prime number checker</a>
            </button>
        </div>
    </div>
</div>

<div class="mini_spacer1"></div>




<Footer/>
<style>
.spacer{
    height: 5em;
}

.mini_spacer{
    height: 2em;
}

.mini_spacer1{
    height: 4em;
}

.projectspage{
    display: flex;
    flex-direction: column;
    margin-left: 2em;
    font-family: coolvetica;
    margin-top: 5em;
    margin-bottom: 5em;

}

.overskrift{
    display: flex;
    flex-direction: row;
    font-size: 2.5em;
    font-family: "industry-inc-stencil", sans-serif;
    align-items: center;
    gap: 1em;
}

.tekst{
    display: flex;
    flex-direction: row;
    font-family: "industry-inc-stencil", sans-serif;
    height: 100px;
    align-items: center;
    gap: 1em;
}

.goback{
    height: 2em;
    width: auto;
}

.backbutton{
    display: flex;
    flex-direction: row;
    font-size: 0.25em;
}

.undertext{
    height: fit-content;

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
    transform: scale(1.1);
    transition: 0.5s;
}

.projects{
    display: flex;
    flex-direction: row;
    gap: 1.5em;
    font-size: 1.25em;
    font-family: "coolvetica";
}

.section_1{
    display: flex;
    flex-direction: column;
    gap: 1.5em;
    font-size: 1.25em;
    font-family: "coolvetica";
    justify-content: space-evenly;
}

.section_2{
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
    letter-spacing: 0.1em;
    width: fit-content;
}

a:hover{
    color: #024D98;
    text-decoration: underline;
}

h1{
    margin: 0;
}     

@media (max-width: 480px) {
    .tekst{
        gap: 0.5em;
        font-size: 0.5em;
    }

    .overskrift{
        gap: 0.1em;
        
    }

    .projects{
        flex-direction: column;
        gap: 0.5em;
    }

    .projectspage{
        margin-left: 0.5em;
    }

}
</style>