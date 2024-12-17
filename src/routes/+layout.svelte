<script>
    import Button from "$lib/Components/button.svelte"
    import Switch from "$lib/Components/switch.svelte"
    import { Hamburger } from 'svelte-hamburgers';
    import { fly } from 'svelte/transition';

    

    let open = $state(false);

    let acceptTerms = $state(false);



</script>   


<nav>
    
    <img class= "logo-navbar" src=/assets/logo.png alt="logo"/>
    <ul class="links">
        <li class="knapper">
            <a href="/">Home</a>
        </li>
        <li class="knapper">
            <a href="/projects">Projects</a>
        </li>
        <li class="knapper">
            <a href="/aboutme">About me</a>
        </li>
        <li class="blå_knapp">
            <a class = "contactme" href="/contactme">Contact me</a>
        </li>
        <li class="switchtext">
            <p>Dark mode:</p>
            <Switch  bind:checked={acceptTerms}></Switch>
        
        </li>
    </ul>  

    <div class="hamburger">
        <Hamburger
        bind:open
        type="collapse"
        title="Toggle nav links"
        ariaControls="nav"
        --color="#024D98"
    />

    {#if open}
        <ul id="nav" class="menu" transition:fly={{x: 50 }}>
            <li><a href="/">Home</a></li>
            <li><a href="/projects">projects</a></li>
            <li><a href="/aboutme">About me</a></li>
            <li><a class = "contactme" href="/contactme">Contactme</a></li>
            <li class="switchtext">
                <p>Dark mode:</p>
                <Switch class="switch" bind:checked={acceptTerms}></Switch>
            
            </li>
        </ul>
    {/if}
    </div>
    


</nav>




<slot/>

<style>
    nav {
        display: flex;
        position: fixed;
        width: 100%;
        justify-content: space-between;
        align-items: center;   
        border-bottom: 2px solid #024D98; 
        box-shadow: 0px 0px 10px #024D98;
        background-color: white;
        z-index: 100;
    }

    :global(body.dark-mode) nav {
        background-color: black;
        border-bottom: white;
        box-shadow: 0px 0px 10px white;
    }

    :global(body.dark-mode) nav a {
        color: white;
    }

    .links {
        display: flex;
        list-style: none; 
        text-decoration: none;
        font-size: 1.45em;   
        align-items: center;
    }

    li {
        margin-right: 40px;
        text-decoration: none;
        text-align: center;
    }

    .knapper {
        text-decoration: none;
        margin-right: 40px;
        padding:0;
    }

    .links .knapper a:hover {
	color: #024D98;
	transition: 0.3s;
    padding-bottom: 5px;
    }   

    :global(body.dark-mode) .links .knapper a:hover {
        color: white;
    }


    .logo-navbar {
        width: 80px;
        height: auto;
        margin-left: 7.5em;
        padding: 15px;
        scale: 1.2;
    } 

    a {
        font-family: coolvetica;
        font-size: 1.2em;
        text-decoration: none;
        color: black;
        padding: 0;
    }

    .contactme {
        color: white;
        background-color: #024D98;
        border-radius: 10px;
        padding: 10px;
    }

    .hamburger {
        display: none;
    }

    nav ul {
    list-style: none;
    display: flex;
    gap: 10px;
    padding: 0;
    margin: 0;
    }

    nav li {
    position: relative; 
    }

    nav a {
    text-decoration: none;
    color: black;
    display: inline-block;
    }

  
    nav .knapper a::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 0;
    height: 4px;
    background-color: #024D98;
    transition: width 0.3s ease;
    }

    :global(body.dark-mode) nav .knapper a::after {
        background-color: white;
    }

    nav a:hover::after {
    width: 100%;
    }

    .menu {
        gap: 10px;
    }

    .contactme:hover {
        background-color: white;
        color: #024D98;
        transition: 0.3s;
        border: #024D98 2px solid;
        padding: 7.5px;
        
    }

    p {
        margin: 0;
        font-size: 1.2em;
        font-family: coolvetica;
    }

    :global(body.dark-mode) p {
        color: white;
    }

    .switchtext {
        margin-right: 2em;
        scale: 0.75;
    }

    @media (max-width: 1040px) {
        .logo-navbar {
            margin-left: 2em;
        }
        a {
            font-size: 1em;
        }
        .contactme {
            display: flex;
            background-color: transparent;
            color: #024D98;
            padding: 0;

        }
    }
    @media (max-width: 750px) {
        .hamburger {
            display: flex;
        }

        .contactme:hover {
            border: 0;
            transition: 0;
            padding: 0;
        }
        .links {
            display: none;
        }

        a {
            font-size: 1em;
        }

        ul {
            flex-direction: column;
        }

        nav {
            justify-content: none;
        }
    
    }
</style>




