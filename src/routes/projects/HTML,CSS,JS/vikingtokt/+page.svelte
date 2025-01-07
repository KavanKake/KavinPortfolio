<script>
    import Footer from "$lib/Components/Footer.svelte";
    import LoadingScreen from "$lib/Components/LoadingScreen.svelte";

let isLoading = true;

// Simulate a delay (e.g., fetching data)
setTimeout(() => {
isLoading = false;
}, 750);
</script>


{#if isLoading}
    <LoadingScreen class="loading-screen" message="Please wait while we load the app..." />
{:else}

<main>

    <div class="spacer"></div>
    
    <div class="page">
        <div class="header">
        <div class="overskrift">
            <div class="tekst">
                <h1>Vikingtokt</h1>
            </div>
            <div class="backbutton">
                <img class="goback" src="/assets/Goback.png" alt="Go Back">
                <a class="goback_tekst" href="/projects/HTML,CSS,JS"> Go Back</a>
            </div>
        </div>
    
        <div class="partner">
            <h1>Co-workers:</h1>
            <a href="https://github.com/HenrikPaaGithub">Henrik Luan</a>
        </div>
    
        </div>
    
        <div class="mini-spacer"></div>
    
        <div class="innhold">
    
            <div class="section">
                <div class="container">
                    <img class="img" src="/assets/vikingtokthome.png" alt="Vikingtokt">
                </div>
                <div class="tekst-right">
                    <p>This web page, titled "Wolfheart Tribe," is a project I designed and coded to capture a Viking-inspired theme. The centerpiece of the design is a detailed 3D model of a Viking longship, adding depth and interactivity to the layout. The background, styled to resemble aged parchment, enhances the historical aesthetic, while the navigation links for "Shop," "About Us," and "Join Us" provide a clean and functional user experience. This project showcases my ability to blend creative design with 3D model integration and functional web development.</p>
                </div>
            </div>
    
            <div class="section">
                <div class="tekst-left">
                    <p>This web page delves into the tribe's fictional lore and cultural heritage. It features a striking visual design, including images of Viking warriors, which enhance the immersive storytelling. The page layout combines a bold header, textured parchment background, and clean typography to emphasize the tribe's legendary bravery and connection to nature. The content explores their traditions, alliances, and spiritual practices, providing a rich narrative experience. This project highlights my ability to create visually engaging and thematic web pages that combine historical inspiration with modern design principles.</p>
                </div>
                <div class="container">
                    <img class="img" src="/assets/vikingtoktomoss.png" alt="Vikingtokt">
                </div>
            </div>
    
            <div class="section">
                <div class="container">
                    <img class="img" src="/assets/vikingtoktshop.png" alt="Vikingtokt">
                </div>
                <div class="tekst-right">
                    <p>
                        This web page, part of the "Wolfheart Tribe" project, showcases a Viking-themed shop section. It features a clean layout with categories for "Weapons" and "Shields," highlighting detailed visual representations of items like axes, along with their prices listed in "gold coins" to enhance the immersive historical feel. The parchment-style background and simple typography align with the overall Viking aesthetic of the project.</p>
                </div>
            </div>
    
            <div class="section">
                <div class="tekst-left">
                    <p>This page from the "Wolfheart Tribe" project features a registration form inviting users to join a Viking-inspired community. With a dramatic backdrop of a Viking ship at sea, it combines immersive visuals with functional elements, such as input fields for personal details. The design emphasizes a sense of adventure and camaraderie, showcasing my ability to create engaging and thematic user interfaces.</p>
                </div>
                <div class="container">
                    <img class="img" src="/assets/vikingtoktjoin.png" alt="Vikingtokt">
                </div>
            </div>
    
            <div class="download">
                <button>
                    <a href="/My_projects/vikingtokt.zip" download="Vikingtokt">Click here to download zip-file</a>
                </button>
            </div>

        </div>
    
    </div>

    <Footer/>
</main>

{/if}




<style>
    .spacer{
        height: 10em;
    }

    .mini-spacer{
        height: 3.5em;
    }

    :global(body.dark-mode) .spacer {
        background-color: black;
    }

    .overskrift{
        display: flex;
        flex-direction: row;
        font-size: 2em;
        font-family: "industry-inc-stencil", sans-serif;
        align-items: center;
        gap: 1em;
        padding-left: 1.5em;
    }

    h1{
        margin: 0;
    }

    :global(body.dark-mode) h1 {
        color: white;
    }

    .partner{
        display: flex;
        flex-direction: row;
        font-size: 1em;
        font-family: coolvetica;
        align-items: center;
        gap: 1em;
        padding-left: 3em;
    }

    :global(body.dark-mode) .overskrift {
        color: white;
    }

    :global(body.dark-mode) .page  {
        background-color: black;
    }




    .goback{
    height: 4em;
    width: auto;
}

:global(body.dark-mode) .goback {
    filter: invert(1);
}

.backbutton{
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 0.25em;
    gap: 10px;
}


.goback_tekst{
    text-decoration: none;
    color: black;
    font-size: 2em;
    letter-spacing: 0.1em;
    font-family: coolvetica;    
}

:global(body.dark-mode) .goback_tekst {
    color: white;
}

.goback_tekst:hover{
    text-decoration: underline;
}

.section{
    padding-top: 2em;
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1.5em;
    font-size: 1.25em;
    padding-left: 2em;
    padding-right: 2em;
    padding-bottom: 2em;
    font-family: "coolvetica";
    justify-content: space-evenly;
}

.img{
    width: 100%;
    min-height: 200px;
    height: auto;
    min-height: auto;
    border: 5px solid #024D98;
}


.download{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    list-style: none;
    background: transparent;
    border-radius: 10px;  
    padding: 0.5em;  
    padding-bottom: 2em;
}

button{
    text-decoration: none;
    list-style: none;
    background: transparent;
    border: #024D98 3px solid;
    border-radius: 10px;  
    padding: 0.5em;  
}

a{
    text-decoration: none;
    color: black;
    font-size: 2em;
}

a:hover{
    text-decoration: underline;
}

:global(body.dark-mode) a {
    color: white;
}

button:hover{
    transform: scale(1.1);
    transition: 0.5s;
}


:global(body.dark-mode) button {
    border: white 3px solid;
}


.tekst-right{
    text-align: right;
    font-size: 1em;
}

:global(body.dark-mode) .tekst-right {
    color: white;
}

.tekst-left{
    text-align: left;
    font-size: 1em;
}

:global(body.dark-mode) .tekst-left {
    color: white;
}


@media (max-width: 750px) {
    .overskrift{
        display: flex;
        flex-direction: column;
        gap: 0;
        padding-top: 2em;
    }
    .section{
        display: flex;
        flex-direction: column;
        gap: 0;
        padding-top: 2em;
    }
    .img{
        width: 100%;
        min-height: 200px;
        height: auto;
        min-height: auto;
        border: 5px solid #024D98;
    }

    .tekst-left{
        text-align: center;
        font-size: 1em;
    }

    .tekst-right{
        text-align: center;
        font-size: 1em;
    }
}


</style>