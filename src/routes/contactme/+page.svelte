<script>
    import Footer from "$lib/Components/Footer.svelte";
    </script>
    
    
    
    
    <div class="spacer"></div>
    <div class="frontpage">
        <div class="section_1">
            <h1>Would you like to contact me?</h1>
            <h3>Fill out the form on the right side to automatically send me an email</h3>
            <h3>Or send a mail to the e-mail down below</h3>
    
            <div class="email">
                <img class="mail_logo"src="/assets/mail.png" alt="E-mail">
                <h3>contact@kavinlokeswaran.no</h3>
            </div>
    
        </div>
    
        <div class="section_2">
            <h1 class="contactform">Contact form</h1>
            <form method="POST" action="https://formsubmit.co/contact@kavinlokeswaran.no">
                <h3 class="name">Your name</h3>
                <div class="nameSplit">
                    <input name="Name" type="text" class="placeholderName" placeholder="First name" required>
                    <input name="Name" type="text" class="placeholderName" placeholder="Last name" required>
                </div>
                <h3 class="name">Your e-mail</h3>
                <input name="Email" type="email" class="placeholder" placeholder="Enter your e-mail" required>
                <h3 class="name">Topic</h3>
                <input name="Topic" type="text" class="placeholder" placeholder="Enter your topic">
                <h3 class="name">Message</h3>
                <textarea name="Message" placeholder="Enter message"></textarea>
                <button class="submit"type="submit">Send in</button>
            </form>
        </div>
    
    </div>


    <Footer/>
    
    <style>
        *{
            margin: 0;
        }
    
        .spacer{
            height: 7.5em;
        }

        :global(body.dark-mode) .spacer {
            background-color: #0d0c1d;
        }
    
        .frontpage {
            display: flex;
            flex-direction: row;
            gap: 10em;
            overflow-x: hidden;
            overflow-y: none;
            font-family: coolvetica;
        }

        :global(body.dark-mode) .frontpage {
            background-color: #0d0c1d;
        }
    
        .section_1 {
            display: flex;
            flex-direction: column;
            align-items: right;
            justify-content: center;
    
            margin-top: 5em;
            margin-left: 3em;
    
            
        }
    
        .section_2 {
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center ;
            border: #024D98 10px solid;
            border-radius: 20px;
            padding: 1.5em;
            margin-top: 2em;
            margin-right: 5em;
            margin-bottom: 2em;
            z-index: 0;
            height: fit-content;
            width: 35em;
            scale: 0.9;
            
            
        }
    
        .contactform{
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: coolvetica;
            color: black;
            font-size: 2.5em;
        }

    
        form{
            display: flex;
            text-align: left;
            flex-direction: column;
            gap: 0.5em;
        }
    
        textarea {
            height: 10em;
            border-radius: 10px;
            font-family: coolvetica;
            font-size: 1em;
            padding: 1em;
        }
    
        .name {
            padding-top: 0.5em;
            font-size: 1em;
            color: black;
        }
    
        button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 1em;
    
            font-family: coolvetica;
            font-size: 1em;
            padding: 0.5em;
            border-radius: 0.5em;
            border: 0;
            color: white;
            background-color: #024D98; ;
            width: 10em;
        }
    
    
        button:hover {
            cursor: pointer;
            background-color: #024D98;
            color: white;
            transform: scale(1.1);
            transition: 0.5s;
        }
    
        .placeholder {
            color: black;
            font-family: coolvetica;
            font-size: 1em;
            padding: 1em;
            border-radius: 10px;
        }

        .placeholderName {
            color: black;
            font-family: coolvetica;
            font-size: 1em;
            padding: 1em;
            border-radius: 10px;
            width: 20em;
        }
    
    
        .mail_logo {
            width: 2em;
            height: auto;
            margin-right: 0.5em;
        }

        :global(body.dark-mode) .mail_logo {
            filter: invert(1);
        }
    
        h3 {
            color: black;
        } 

        :global(body.dark-mode) h3 {
            color: white;
        }

        h1 {
            color: black;
        }
        :global(body.dark-mode) h1 {
            color: white;
        }

        .nameSplit {
            display: flex;
            flex-direction: row;
            gap: 1em;
        }
    
        .email {
            display: flex;
            flex-direction: row;
            
            align-items: center;
            margin-top: 10em;
            font-size: 1.5em;
            color: black;
            padding: 0.5em;
            border: 2px #024D98 solid;
            
        }
    
        @media (max-width: 950px) {
            .frontpage {
                gap: 1em;
                margin-left: 0;
            }
        }
    
        @media (max-width: 780px) {
            .section_1{
                display: none;
            }
    
            .frontpage{
                margin-left: 2em;
                justify-content: center;
            }
    
            .section_2{
                margin-right: 2em;
            }
    
        }
    </style>