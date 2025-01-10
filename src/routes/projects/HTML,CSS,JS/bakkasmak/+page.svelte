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
                <h1>Bakkasmak</h1>
            </div>
            <div class="backbutton">
                <img class="goback" src="/assets/Goback.png" alt="Go Back">
                <a class="goback_tekst" href="/projects/HTML,CSS,JS"> Go Back</a>
            </div>
        </div>
    
        <div class="partner">
            <h1>Co-workers:</h1>
            <a href="https://github.com/JohanArntzen">Johan Album Arntzen</a>, <a href="https://github.com/StormFire0G">Storm Davidsen</a>
        </div>
    
        </div>
    
        <div class="mini-spacer"></div>
    
        <div class="innhold">
    
            <div class="section">
                <div class="container">
                    <img class="img" src="/assets/bakkasmakhome.png" alt="Bakkasmak-home">
                </div>
                <div class="tekst-right">
                    <p>This page from the "Bakkasmak" project presents a visually appealing weekly menu design. The layout features vibrant food imagery, each labeled with a corresponding day of the week in Norwegian, offering a clear and appetizing overview. The minimalist top navigation, search functionality, and clean typography demonstrate my ability to create user-friendly and aesthetically pleasing interfaces, ideal for showcasing culinary content.</p>
                </div>
            </div>
    
            <div class="section">
                <div class="tekst-left">
                    <p>This page from "Elvebakken Kantinen" is focused on showcasing a specific meal offering for Monday ("Mandag"). The left side features a high-quality image of a burger, enticing the viewer, while the right side provides a detailed description in Norwegian. The footer contains clear contact information and a prominent call-to-action ("Om oss") button. The clean and contrasting color scheme complements the text and image content, making it user-friendly and visually appealing.</p>
                </div>
                <div class="container">
                    <img class="img" src="/assets/bakkasmakhome2.png" alt="Bakkasmak-home">
                </div>
            </div>
    
            <div class="section">
                <div class="container">
                    <img class="img" src="/assets/bakkasmaksnack.png" alt="Bakkasmak-snacks">
                </div>
                <div class="tekst-right">
                    <p>This page from Elvebakken Kantinen highlights drinks, salad ingredients, and food items with a clean and inviting green design. Drinks are priced individually, salads are available by weight, and the menu offers a variety of fresh, customizable options. The layout is simple and easy to navigate, maintaining a focus on clarity and freshness.</p>
                </div>
            </div>
    
            <div class="section">
                <div class="tekst-left">
                    <p>This page is for the user to see who the developers are. Thsi page telles about the developers and their background. The page also says a bit about what the webpage is all about.</p>
                </div>
                <div class="container">
                    <img class="img" src="/assets/bakkasmakomoss.png" alt="Bakkasmak-aboutus">
                </div>
            </div>

            <div class="section">
                <div class="container">
                    <img class="img" src="/assets/bakkasmakstem.png" alt="Bakkasmak-voting">
                </div>
                <div class="tekst-right">
                    <p>This page is for the user to vote on which project they want to work on next. They have the three option and could choose what they want in the cantine for next week</p>
                </div>
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