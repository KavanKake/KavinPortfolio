<script>
</script>



<div class="footer">
    <div class="section1">
        <div class="overskrift">
            <h1>Kavin Lokeswaran</h1>
        </div>

        <div class="info">
            <p>This is a portfolio website made by Kavin Lokeswaran</p>
        </div>

        <div class="btns">
        
            <a class="button" href="https://github.com/KavanKake">
                <img class="logo" src=/assets/githubwhite.png alt="button" />
            </a>
        
            <a class="button" href="https://www.instagram.com/kavin_lokeswaran_/">
                <img class="logo" src=/assets/instawhite.png alt="button" />
            </a>
        
            <a class="button" href="https://www.facebook.com/profile.php?id=61550619093513">
                <img class="logo" src=/assets/facewhite.png alt="button" />
            </a>
        
            <a class="button" href="https://www.linkedin.com/in/kavin-lokeswaran/">
                <img class="logo" src=/assets/linkedinwhite.png alt="button" />
            </a>
        
        </div>


        <div class="copyright">
            <h1>Copyright © Kavin Lokeswaran</h1>
            <h1>2025</h1>
        </div>
        
    </div>






</div>





<style>
    .footer{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        background-color: #024D98;
        height: 17.5em;
        color: white;
        font-family: coolvetica;
        position: relative;
    }

    .footer, 
:global(body.dark-mode) .footer, 
.button, 
.btns .button, 
.btns:has(.button:hover) .button:not(:hover) {
    transition: background-color 0.5s ease-in-out, 
                color 0.5s ease-in-out, 
                border-color 0.5s ease-in-out, 
                box-shadow 0.5s ease-in-out, 
                transform 0.3s ease-in-out, 
                opacity 0.3s ease-in-out;
}

    :global(body.dark-mode) .footer {
        background-color: #0d0c1d;
        border-bottom: white;
        box-shadow: 0px 0px 20px #024D98;
    }

    .section1{
        font-size: 0.5em;
        display: flex;
        flex-direction: column;
        text-align: center;
    }

    .overskrift{
        display: flex;
        flex-direction: column;
        text-align: center;
        font-size: 3em;
    }

    .info{
        display: flex;
        flex-direction: column;
        text-align: center;
        font-size: 2em ;
    }

    .copyright{
        display: flex;
        flex-direction: column;
        text-align: center;
        padding-bottom: 2.5em;
    }

    h1{
        margin: 0;
        margin-top: 10px;
    }

    p{
        margin: 0;
    }

    .btns{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 2.5em;
        padding: 20px;
    }

    .btns:has(.button:hover) .button:not(:hover){
        opacity: 0.8;
        scale: 0.9;
        
    }

    .button{
        align-content: space-between;
        justify-content: center;
        border: 3px solid white;
        border-radius: 30%;
        padding: 0.75em;
        &:hover{
            scale: 1.2;
        }
    }

    .logo{
        width: 5em;
        height: auto;
    }

    @media (max-width: 1040px) {
        .footer{
            display: flex;
            background-color: #024D98;
            height: 25em;
            color: white;
            font-family: coolvetica;
            height: fit-content;
        }

        .section1{
            font-size: 0.5em;   
        }

        .btns{
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            gap: 2.5em;
            padding: 20px;
        }
    }

    @media (max-width: 480px) {
        .section1{
            font-size: 0.5em;
            scale: 0.8;
        }

    }
</style>