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
    
    <div class="aboutme">
        <div class="section_1">
            <div class="conteiner">
                <img src="assets/OmmegBilde.png" alt="Kavin Lokeswaran">
            </div>
        </div>
    
        <div class="section_2">
            <div class="overskrift">
                <h1>About me</h1>
            </div>
            <div class="underoverskrift">
                <h3>Kavin Lokeswaran - IT student</h3>
            </div>
    
            <div class="tekst">
                <p>Hello, my name is Kavin Lokeswaran. I am a passionate IT student with a strong interest in technology, programming, at Elvebakken VGS in Oslo, Norway. I am currently studying IT, because I enjoy understanding how technology work and how it could improve our daily lives. I have worked with many projects, for example this website. When I’m not working on IT related projects, I enjoy playing games or play football. My dream is to became an IT engineer. </p>
            </div>
    
            <div class="skole">
                <div class="barneskole">
                    <div class="barneskole-icon">
                        <img class="icon" src="assets/skoleicon.png" alt="icon">
                    </div>
                    <div class="barneskole-tekst">
                        <h4>Mortensrud skole</h4>
                        <p>2013-2020</p>
                    </div>
                </div>
    
                <i class="arrow"></i>
    
                <div class="ungdomskole">
                    <div class="ungdomskole-icon">
                        <img class="icon" src="assets/skoleicon.png" alt="icon">
                    </div>
                    <div class="ungdomskole-tekst">
                        <h4>Lofsrud skole</h4>
                        <p>2020-2023</p>
                    </div>
                </div>
    
                <i class="arrow"></i>
    
                <div class="vgs">
                    <div class="vgs-icon">
                        <img class="icon" src="assets/skoleicon.png" alt="icon">
                    </div>
                    <div class="vgs-tekst">
                        <h4>Elvebakken VGS</h4>
                        <p>2023 - present</p>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
    
    
    <div class="mini_spacer"></div>
    
    <Footer/>
</main>

{/if}




<style>


    .spacer{
        height: 10em;
    }

    :global(body.dark-mode) .spacer {
        background-color: #0d0c1d;
    }

    .mini_spacer{
        height: 5.5em;
    }

    :global(body.dark-mode) .mini_spacer {
        background-color: #0d0c1d;
    }

    .aboutme{
        display: flex;
        flex-direction: row;
        gap: 7.5em;
    }

    main{
        background-color: white;
        overflow-y: scroll;
    }


    :global(body.dark-mode) .aboutme {
        background-color: #0d0c1d;
    }

    .section_1{
        display: flex;
        margin-left: 1em;
        align-items: center;
    }

    .conteiner{
        display: flex;
        width: auto;
        height:35em;
        border: 3px solid #024D98;
        z-index: 0;
    }

    .overskrift{
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 2.5em;
        font-family: "industry-inc-stencil", sans-serif;
    }

    :global(body.dark-mode) .overskrift {
        color: white;
    }

    .underoverskrift{
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 1.75em;
        font-family: coolvetica;
        color: #024D98;
    }

    .tekst{
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 1.5em;
        width: 90%;
        font-family: coolvetica;
    }

    :global(body.dark-mode) .tekst {
        color: white;
    }

    h1{
        margin: 0;
    }

    h3{
        margin: 0;
    }

    h4{
        margin: 0;
    }

    .icon{
        width: 4em;
        height: auto;
        margin-right: 0.5em;
        scale: 0.9;
        border: #024D98 3px solid;
        padding: 5px;
        border-radius: 50%;
    }

    :global(body.dark-mode) .icon {
        filter: invert(1);
    }

    .barneskole{
        display: flex;
        flex-direction: column;
        font-size: 1.25em;
        font-family: coolvetica;
    }

    :global(body.dark-mode) .barneskole {
        color: white;
    }

    .ungdomskole{
        display: flex;
        flex-direction: column;
        font-size: 1.25em;
        font-family: coolvetica;
    }

    :global(body.dark-mode) .ungdomskole {
        color: white;
    }

    .vgs{
        display: flex;
        flex-direction: column;
        font-size: 1.25em;
        font-family: coolvetica;
        width: fit-content;
    }

    :global(body.dark-mode) .vgs {
        color: white;
    }

    .arrow{
        border: solid #024D98;
        border-width: 0 3px 3px 0;
        display: inline-block;
        padding: 3px;
        transform: rotate(-45deg);
        -webkit-transform: rotate(-45deg);
        margin-left: 1em;
        margin-right: 1em;
        scale: 1.5;
    }

    .skole{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
        width: 100%;
        margin-right: 10em;
        margin-top: 2.5em;
    }

    /* Apply smooth transition to dark mode changes */
:root, :global(body.dark-mode) {
    transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out, filter 0.5s ease-in-out;
}

.spacer, .mini_spacer, main, .aboutme, .overskrift, .tekst, .icon, .barneskole, .ungdomskole, .vgs {
    transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out, filter 0.5s ease-in-out;
}

/* Add fade-in effect when switching themes */
:global(body.dark-mode) {
    animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0.8;
    }
    to {
        opacity: 1;
    }
}

    

    @media (max-width: 1000px) {
        .aboutme{
            flex-direction: column;
            gap: 1em;
            justify-content: center;
            align-items: center;
        }

        .section_2{
            margin-left: 1em;
            margin-right: 1em;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .conteiner {
            scale: 0.8;
            height: 30em;
            justify-content: center;
        }

        .section_1{
            margin-left: 0em;

        }

        .tekst{
            width: 100%;
            text-align: center;
        }

        .skole{
            scale: 0.8;
        }

        .underoverskrift{
            text-align: center;
        }

        .overskrift{
            text-align: center;
        }
    }
</style>

