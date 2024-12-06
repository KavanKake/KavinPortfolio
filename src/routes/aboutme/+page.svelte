<script>
    import Footer from "../../lib/Components/Footer.svelte"
    import picture from "$lib/assets/aboutme.jpg"
</script>



<div class="spacer"></div>

<div class="aboutme">
    <div class="section_1">
        <div class="conteiner">
            <img src="{picture}" alt="Kavin Lokeswaran">
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
    </div>
    
</div>

<div class="mini_spacer"></div>

<Footer/>






<style>
    .spacer{
        height: 10em;
    }

    .mini_spacer{
        height: 5.5em;
    }

    .aboutme{
        display: flex;
        flex-direction: row;
        gap: 7.5em;
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
        z-index: -1;
    }

    .overskrift{
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: 2.5em;
        font-family: "industry-inc-stencil", sans-serif;
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
        width: 30em;
        font-family: coolvetica;
    }

    h1{
        margin: 0;
    }

    h3{
        margin: 0;
    }

    @media (max-width: 1280px) {
        .aboutme{
            flex-direction: column;
            gap: 1em;
        }

        .section_2{
            margin-left: 1em;
        }

        .conteiner {
            scale: 0.8;
            height: 30em;
        }

        .section_1{
            margin-left: 0em;
        }

        .tekst{
            width: 100%;
        }
    }
</style>

