<script>
    import Footer from "$lib/Components/Footer.svelte";
</script>

<div class="space"></div>
<div class="frontpage">
    <div class="section_1">
        <h6 class="hello">Hello, my name is</h6>
        <h1 class="myname">Kavin</h1>
        <h1 class="myname">Lokeswaran</h1>
        
        
        
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
        <img class="frontpage_picture" src=/assets/homepagebilde.png alt="">
    </div>
    
    
    
</div>

<Footer/>

<style>

    .frontpage {
        display: flex;
        flex-direction: row;
        gap: 10em;
        margin-left: 2em;
        overflow-x: hidden;
        overflow-y: none;
    }

    .space {
        height: 7.5em;
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
            scale: 1.2;
        }
    }

    .logo{
        width: 3em;
        height: auto;
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

    @media (max-width: 730px) {
        .frontpage_picture{
            opacity: 0;
        }
    }

    @media (max-width: 570px) {
        .frontpage_picture{
            opacity: 0;
            overflow-x: hidden;
        }

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
    }
</style>



