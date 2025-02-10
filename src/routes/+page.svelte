<script>
    import Footer from "$lib/Components/Footer.svelte";

    import LoadingScreen from "$lib/Components/LoadingScreen.svelte";

let isLoading = true;
setTimeout(() => {
isLoading = false;
}, 2500);
    
</script>

{#if isLoading}
    <LoadingScreen class="loading-screen" message="Please wait while we load the app..." />
{:else}

<main>
    <div class="space"></div>
    <div class="frontpage">
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
    
    <Footer/>
</main>

{/if}

<style>
    :global(body) {
        background-color: white;
    }

    :global(body.dark-mode) {
        background-color: black;
    }


    main {
        background-color: white;
    }

    :global(body.dark-mode) main {
        background-color: black;
    }

    .frontpage {
        display: flex;
        flex-direction: row;
        gap: 20em;
        padding-top: 5em;
    }

    :global(body.dark-mode) .frontpage {
        background-color: black;
    }

    .space {
        height: 1em;
    }

    .section_1{
        margin-top: 15em;
        margin-left: 6em;
    }

    .section_2{
        margin-top: 5em;
        height: fit-content;
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

    .btns:has(.button:hover) .button:not(:hover){
        opacity: 0.8;
        scale: 0.8;
        filter: blur(4px);
        
    }

    .button{
        align-content: space-between;
        border: 3px solid #024D98;
        border-radius: 30%;
        padding: 0.25em;
        &:hover{
            animation: scaleAnimation 0.75s ease-in ;
        }
    }

    @keyframes scaleAnimation{
        0%{
            transform: scale(1);
        }
        100%{
            transform: scale(1.1);
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
        height: 45em;
        width: fit-content;
        opacity: 100;

    }




    @media (max-width: 1167px) {
        .frontpage {
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

        .frontpage {
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
        
        .frontpage{
            padding-top: 7em;
        }
    }

    @media (min-height: 1230px) {
        
        .frontpage{
            padding-top: 10em;
        }
    }

    @media (min-height: 1200px) {
        
        .frontpage{
            padding-top: 12em;
        }
    }
</style>



