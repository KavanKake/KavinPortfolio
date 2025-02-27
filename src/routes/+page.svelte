<script>
    import Footer from "$lib/Components/Footer.svelte";

    import LoadingScreen from "$lib/Components/LoadingScreen.svelte";

let isLoading = true;

// Simulate a delay (e.g., fetching data)
setTimeout(() => {
isLoading = false;
},1500);
    
</script>

{#if isLoading}
    <LoadingScreen class="loading-screen" message="Please wait while we load the app..." />
{:else}

<main>
    <div class="space"></div>
    <div class="frontpage1">
        <div class="section_1">
            <div class="tekst">
                <h6 class="hello">Hello, my name is</h6>
                <h1 class="myname">Kavin</h1>
                <h1 class="myname">Lokeswaran</h1>
            </div>
            
            
            
            <div class="btns">
            
                <a class="button" href="https://github.com/KavanKake">
                    <img class="logo" src=/assets/githubblack.png alt="button" />
                </a>
            
                <a class="button" href="https://www.instagram.com/kavin_lokeswaran_/">
                    <img class="logo" src=/assets/instablack.png alt="button" />
                </a>
            
                <a class="button" href="https://www.facebook.com/profile.php?id=61550619093513">
                    <img class="logo" src=/assets/faceblack.png alt="button" />
                </a>
            
                <a class="button" href="https://www.linkedin.com/in/kavin-lokeswaran/">
                    <img class="logo" src=/assets/linkedinblack.png alt="button" />
                </a>
            </div>
        </div>
        
        
        <div class="section_2">
            <img class="frontpage_picture" src=/assets/homepagebilde.png alt="Bilde av Kavin Lokeswaran">
        </div>
        
        
        
    </div>
    <div class="space2"></div>
    <div class="projects">
        <div class="projectHeader">
            <h1>Featured projects</h1>
        </div>
        <div class="projectsContainer">
            <a href="https://github.com/KavanKake/KavinPortfolio"> 
            <div class="project1">
                <img class="project1_image" src=/assets/portfolioFront.png alt="Portfolio-picture">
                    <h1 class="project1_title">Portfolio</h1>
                </div>
            </a>
            <a href="https://github.com/KavanKake/Express-js"> 
            <div class="project2">
                <img class="project2_image" src=/assets/expressJSFront.png alt="ExpressJS-picture">
                    <h1 class="project2_title">Login page with ExpressJS</h1>
                </div>
            </a>

        </div>
    </div>
    <div class="space"></div>
    
    <Footer/>
</main>

{/if}

<style>
    :global(body) {
        background-color: white;
    }

    :global(body.dark-mode) {
        background-color: #0d0c1d;
    }


    main {
        background-color: white;
    }

    :global(body.dark-mode) main {
        background-color: #0d0c1d;
    }

    .frontpage1 {
        display: flex;
        flex-direction: row;
        gap: 20em;
        padding-top: 2em;
        border-bottom: #024D98 10px solid;
    }

    :global(body.dark-mode) .frontpage1 {
        background-color: #0d0c1d;
    }

    .space {
        height: 4em;
    }

    .space2 {
        height: 0em;
    }

    .section_1{
        margin-top: 15em;
        margin-left: 6em;
    }

    .section_2{
        margin: 0em;
        height: 640px;
        margin-top: 5em;
    }

    .hello{
        text-align: left;
        color: black;
        font-family: "coolvetica";
        font-size: 1.5em;   
        margin-bottom: 0.25em;
        margin-top: 0em;
        width: fit-content;
    }

    :global(body.dark-mode) .hello {
        color: #EFEFEF;
    }

    .myname{
        color: white;
        text-shadow: 0px 0px 10px #024D98,
                    0px 0px 10px #024D98,
                    0px 0px 20px #024D98,
                    0px 0px 30px #024D98,
                    0px 0px 40px #024D98;
        font-family: "industry-inc-stencil", sans-serif;
        font-weight: 750;
        font-size: 5em;   
        margin-bottom: 0em;
        margin-top: 0em;

        width: fit-content;
    }

    .btns{
        display: flex;
        flex-direction: row;
        gap: 2.5em;
        padding: 20px;
        padding-left: 0px;
        width: fit-content;
    }

    .btns:has(.button:hover) .button:not(:hover) {
    opacity: 0.8;
    transform: scale(0.8); /* Use transform instead of scale */
    filter: blur(4px);
}

    .button {
    align-content: space-between;
    border: 3px solid #024D98;
    border-radius: 30%;
    padding: 0.25em;
    transition: transform 0.3s ease-in-out; /* Smooth transition */

    &:hover {
        transform: scale(1.2); /* Use transform instead of scale */
    }
}

    .logo{
        width: 3em;
        height: auto;
    }

    :global(body.dark-mode) .logo {
        filter: invert(1);
    }

    :global(body.dark-mode) .button {
        border: 3px solid #EFEFEF;
    }


    .frontpage_picture{
        height: 40em;
        width: fit-content;
        opacity: 100;
    }

    .projects{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .projectHeader{
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 1em;
        font-size: 1.5em;
        padding-top: 2em;
        padding-bottom: 2em;
        font-family: "coolvetica";
        font-weight: 600;
        color: #024D98;
    }

    .projectsContainer{
        display: flex;
        flex-direction: row;
        gap: 10em;
        font-family: coolvetica;
    }

    .project1{
        display: flex;
        flex-direction: column;
        gap: 2em;
        height: 30em;
        width: 30em;
        align-items: center;
        justify-content: center;
        border: #024D98 3px solid;
        border-radius: 20px;
        background-color: #024D98;
    }

    .project2{
        display: flex;
        flex-direction: column;
        gap: 2em;
        height: 30em;
        width: 30em;
        align-items: center;
        justify-content: center;
        border: #024D98 3px solid;
        border-radius: 20px;
        background-color: #024D98;
    }

    .project1_image{
        height: 15em;
        width: auto;
        border: black 3px solid;
    }

    .project2_image{
        height: 15em;
        width: auto;
        border: black 3px solid;
    }

    .project1_title{
        color: white;
        font-size: 2em;
        text-align: center;
        font-weight: 600;
        text-decoration: none;
        transition: transform 0.3s ease-in-out;
    }

    .project1_title:hover{
        transform: scale(1.3);
    }

    .project1:hover .project1_title{
        transform: scale(1.3);
    }

    .project2:hover .project2_title{
        transform: scale(1.3);
    }

    .project2_title{
        color: white;
        font-size: 2em;
        text-align: center;
        font-weight: 600;
        text-decoration: none;
        transition: transform 0.3s ease-in-out;
    }

    .project2_title:hover{
        transform: scale(1.3);
    }


    @media (max-width: 1167px) {
        .frontpage1 {
            gap: 1em;
            margin-left: 0;
        }

        .section_1{
            margin-left: 2em;
        }

        .myname{
            font-size: 5em;
        }
    }


    @media (max-width: 920px) {
        .hello{
            font-size: 1em;
        }

        .myname{
            font-size: 3em;
        }

        .btns{
            gap: 1em;
            scale: 0.8;
        }

        .frontpage1 {
            flex-direction: column;
            gap: 0em;
        }

        .frontpage_picture{
            height: 30em;
            width: auto;
            justify-content: center;
            align-items: center;
            transform: scaleX(-1);
        }

        .section_1{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-left: 0em;
            margin-top: 10em;
        }

        .section_2{
            margin-top: 0em;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .myname{
            text-align: center;
        }

        .hello{
            text-align: center;
        }

        .tekst {
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .btns{
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
        }
    }

    @media (min-height: 1200px) {
        
        .frontpage1{
            padding-top: 7em;
        }
    }

    @media (min-height: 1230px) {
        
        .frontpage1{
            padding-top: 10em;
        }
    }

    @media (min-height: 1200px) {
        
        .frontpage1{
            padding-top: 12em;
        }
    }
</style>



