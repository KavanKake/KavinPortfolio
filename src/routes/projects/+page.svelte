<script>
    import Footer from "$lib/Components/Footer.svelte";
</script>



<div class="spacer"></div>

<div class="page">
    <div class="overskrift">
        <div class="tekst">
            <h1>Projects</h1>
        </div>
    </div>
<div class="space"></div>
    <div class="projects">
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
            <a href="https://github.com/KavanKake/BakkaSmak"> 
                <div class="project1">
                    <img class="project1_image" src=/assets/BakkaSmak.png alt="Portfolio-picture">
                        <h1 class="project1_title">BakkaSmak</h1>
                    </div>
                </a>
        </div>
        <div class="projectsContainer">
            <a href="https://github.com/KavanKake/Ratingsystem-fotball"> 
            <div class="project1">
            
                    <h1 class="project1_title_python">Ratingsystem - football</h1>
                    <h1 class="project1_title_python">Python</h1>

                </div>
            </a>
            <a href="https://github.com/KavanKake/Quizspill"> 
            <div class="project1">
                    <h1 class="project1_title_python">Who wants to be a millionaire</h1>
                    <h1 class="project1_title_python">Python game</h1>
                </div>
            </a>                                                    
            <a href="https://github.com/KavanKake/Viking_game">  
                <div class="project1">
                        <h1 class="project1_title_python">Viking game</h1>
                        <h1 class="project1_title_python">Godot game</h1>   
                    </div>
                </a>
        </div>  
        
        <div class="projectsContainer">
            <a href="https://github.com/KavanKake/Vikingtokt"> 
            <div class="project1">
                <img class="project1_image" src=/assets/vikingtokthome.png alt="Portfolio-picture">
                    <h1 class="project1_title_python">Viking webpage</h1>
                    <h1 class="project1_title_python">With Henrik Luan</h1>
                </div>
            </a>
        </div>
    </div>

</div>






<div class="spacer"></div>
<Footer/>

<style>

.spacer {
    height: 10em;
}

.space {
    height: 2em;
}
/* Global transition for background and text color */
:root, :global(body.dark-mode) {
    transition: background-color 0.5s ease-in-out, color 0.5s ease-in-out, filter 0.5s ease-in-out;
}

/* General page background transition */
.page {
    background-color: white;
    transition: background-color 0.5s ease-in-out;
}

:global(body.dark-mode) .page {
    background-color: #0d0c1d;
}

/* Header text and general elements */
.tekst {
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-size: 2em;
    font-family: "industry-inc-stencil", sans-serif;
    align-items: center;
    gap: 1em;
    padding-left: 1.5em;
    color: #024D98;
    transition: color 0.5s ease-in-out;
}



/* Project container styles */
.projects {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10em;
}

/* Projects container for responsive grid */
.projectsContainer {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    gap: 5em;
    font-family: coolvetica;
}

/* Individual project box with smooth hover transition */
.project1, .project2 {
    display: flex;
    flex-direction: column;
    gap: 2em;
    height: 25em;
    width: 25em;
    align-items: center;
    justify-content: center;
    border: #024D98 3px solid;
    border-radius: 20px;
    background-color: #024D98;
    transition: transform 0.3s ease-in-out, background-color 0.5s ease-in-out;
}

/* Hover effects for project items */
.project1:hover, .project2:hover {
    transform: scale(1.05);
    transition: transform 0.3s ease-in-out;
    background-color: #1e2a4d; /* Darker shade on hover */
}

/* Image styling inside project boxes */
.project1_image, .project2_image {
    height: 10em;
    width: auto;
    border: black 3px solid;
}

/* Titles inside the project items */
.project1_title, .project2_title {
    color: white;
    font-size: 1.5em;
    text-align: center;
    font-weight: 600;
    text-decoration: none;
    transition: transform 0.3s ease-in-out, color 0.5s ease-in-out;
}

.project1_title_python, .project2_title {
    color: white;
    font-size: 1.5em;
    text-align: center;
    font-weight: 600;
    text-decoration: none;
    transition: transform 0.3s ease-in-out, color 0.5s ease-in-out;
    margin: 0;
}

/* Hover effect to scale up the text */
.project1_title:hover, .project2_title:hover {
    transform: scale(1.3);
}

/* Dark mode text color changes */
:global(body.dark-mode) .project1_title,
:global(body.dark-mode) .project2_title {
    color: #f0f0f0;
}

:global(body.dark-mode) .project1_title:hover,
:global(body.dark-mode) .project2_title:hover {
    color: #ffcc00; /* Highlight color on hover */
}

/* Dark mode project box background */
:global(body.dark-mode) .project1, :global(body.dark-mode) .project2 {
    background-color: #1e2a4d; /* Darker shade for projects in dark mode */
}

:global(body.dark-mode) .project1:hover, :global(body.dark-mode) .project2:hover {
    background-color: #2a3d5a; /* Slightly darker shade on hover */
}


@media (max-width: 1040px) {
    .projectsContainer {
        flex-direction: column;
        align-items: center;
        gap: 5em;
    }
    
}
</style>





