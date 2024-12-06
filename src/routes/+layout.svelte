<script>

    import { Hamburger } from 'svelte-hamburgers';
    import { fly } from 'svelte/transition';

    let open = $state(false);
</script>


<nav>

    
    <img class= "logo-navbar" src=/assets/Logo_portfolio.png alt="logo"/>
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
        <ul id="nav" class="menu" transition:fly={{y: -15 }}>
            <li><a href="/">Home</a></li>
            <li><a href="/projects">projects</a></li>
            <!-- <li><a href="/extrapages">Extra pages</a></li> -->
            <li><a class = "contactme" href="/contactme">Contactme</a></li>
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
        margin-right: 20px;
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
    gap: 20px;
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
    @media (max-width: 655px) {
        .hamburger {
            display: flex;
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




