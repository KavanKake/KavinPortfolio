<script>
import Button from "$lib/Components/button.svelte";
import Footer from "$lib/Components/Footer.svelte";
import { onMount, onDestroy } from "svelte";

// Reactive variables to store fetched data
let lastMatch = null;
let nextMatch = null;

onMount(async () => {
    try {
    // Fetch performance data

    // Fetch previous match data
    const previousUrl = "https://www.sofascore.com/api/v1/team/2817/events/last/0";
    const previousResponse = await fetch(previousUrl);
    if (!previousResponse.ok) throw new Error(`Error: ${previousResponse.status}`);
    const previousData = await previousResponse.json();
    let pm = previousData.events.length - 1;
    lastMatch = previousData.events[pm];
    
    let previousPreviousMatch = previousData.events[pm - 2];
    let previousPreviousHomeTeam = previousPreviousMatch.homeTeam.name;
    let previousPreviousAwayTeam = previousPreviousMatch.awayTeam.name;

    let previousMatch = previousData.events[pm - 1];
    let previousHomeTeam = previousMatch.homeTeam.name;
    let previousAwayTeam = previousMatch.awayTeam.name;

    let lastMatchHomeTeam = lastMatch.homeTeam.name;
    let lastMatchAwayTeam = lastMatch.awayTeam.name;

    let previous3Match = previousData.events[pm - 3]
    let previous3HomeTeam = previous3Match.homeTeam.name;
    let previous3AwayTeam = previous3Match.awayTeam.name;

    let previous4Match = previousData.events[pm-4]
    let previous4HomeTeam = previous4Match.homeTeam.name;
    let previous4AwayTeam = previous4Match.awayTeam.name; 

    let previous5Match = previousData.events[pm-5]
    let previous5HomeTeam = previous5Match.homeTeam.name;
    let previous5AwayTeam = previous5Match.awayTeam.name

    let previous6Match = previousData.events[pm-6]
    let previous6HomeTeam = previous6Match.homeTeam.name;
    let previous6AwayTeam = previous6Match.awayTeam.name

    let previous7Match = previousData.events[pm-7]
    let previous7HomeTeam = previous7Match.homeTeam.name;
    let previous7AwayTeam = previous7Match.awayTeam.name
    

    // Fetch next match data
    const nextUrl = "https://www.sofascore.com/api/v1/team/2817/events/next/0";
    const nextResponse = await fetch(nextUrl);
    if (!nextResponse.ok) throw new Error(`Error: ${nextResponse.status}`);
    const nextData = await nextResponse.json();
    let nm = 0
    nextMatch = nextData.events[nm];
    let nextMatchHomeTeam = nextMatch.homeTeam.name;
    let nextMatchAwayTeam = nextMatch.awayTeam.name;

    let nextNextMatch = nextData.events[nm + 1];
    let nextNextMatchHomeTeam = nextNextMatch.homeTeam.name;
    let nextNextMatchAwayTeam = nextNextMatch.awayTeam.name;

    let next3Match = nextData.events[nm + 2]
    let next3HomeTeam = next3Match.homeTeam.name;
    let next3AwayTeam = next3Match.awayTeam.name;

    let next4Match = nextData.events[nm+3]
    let next4HomeTeam = next4Match.homeTeam.name;
    let next4AwayTeam = next4Match.awayTeam.name;

    let next5Match = nextData.events[nm+4]
    let next5HomeTeam = next5Match.homeTeam.name;
    let next5AwayTeam = next5Match.awayTeam.name

    let next6Match = nextData.events[nm+5]
    let next6HomeTeam = next6Match.homeTeam.name;
    let next6AwayTeam = next6Match.awayTeam.name

    let next7Match = nextData.events[nm+6]
    let next7HomeTeam = next7Match.homeTeam.name;
    let next7AwayTeam = next7Match.awayTeam.name


    
    
    
    
    document.getElementById('nmbutton').addEventListener('click', () => {
        nm++;
        pm++; 
        console.log(nm, pm)
    })
    
    document.getElementById('priviousbtn').addEventListener('click', () => {
        pm--;
        nm--;
        console.log(nm, pm)
    })


    console.log(pm,nm)
    const interval = setInterval(()=>{
        console.log("Checking if contition ")
        if (pm === 29 && nm === 0) {
            document.getElementById("previousPreviousHomeTeamName").innerText = previousPreviousHomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = previousPreviousAwayTeam
            document.getElementById("previousHomeTeamName").innerText = previousHomeTeam
            document.getElementById("previousAwayTeamName").innerText = previousAwayTeam
            document.getElementById("homeTeamNameNow").innerText = lastMatchHomeTeam
            document.getElementById("awayTeamNameNow").innerText = lastMatchAwayTeam
            document.getElementById("nextHomeTeamName").innerText = nextMatchHomeTeam
            document.getElementById("nextAwayTeamName").innerText = nextMatchAwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = nextNextMatchHomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = nextNextMatchAwayTeam
        } else if (nm === 1) {
            document.getElementById("previousPreviousHomeTeamName").innerText = previousHomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = previousAwayTeam
            document.getElementById("previousHomeTeamName").innerText = lastMatchHomeTeam
            document.getElementById("previousAwayTeamName").innerText = lastMatchAwayTeam
            document.getElementById("homeTeamNameNow").innerText = nextMatchHomeTeam
            document.getElementById("awayTeamNameNow").innerText = nextMatchAwayTeam
            document.getElementById("nextHomeTeamName").innerText = nextNextMatchHomeTeam
            document.getElementById("nextAwayTeamName").innerText = nextNextMatchAwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = next3HomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = next3AwayTeam
        } else if (nm === 2) {
            document.getElementById("previousPreviousHomeTeamName").innerText = lastMatchHomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = lastMatchAwayTeam
            document.getElementById("previousHomeTeamName").innerText = nextMatchHomeTeam
            document.getElementById("previousAwayTeamName").innerText = nextMatchAwayTeam
            document.getElementById("homeTeamNameNow").innerText = nextNextMatchHomeTeam
            document.getElementById("awayTeamNameNow").innerText = nextNextMatchAwayTeam
            document.getElementById("nextHomeTeamName").innerText = next3HomeTeam
            document.getElementById("nextAwayTeamName").innerText = next3AwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = next4HomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = next4AwayTeam
        } else if (nm === 3) {
            document.getElementById("previousPreviousHomeTeamName").innerText = nextMatchHomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = nextMatchAwayTeam
            document.getElementById("previousHomeTeamName").innerText = nextNextMatchHomeTeam
            document.getElementById("previousAwayTeamName").innerText = nextNextMatchAwayTeam
            document.getElementById("homeTeamNameNow").innerText = next3HomeTeam
            document.getElementById("awayTeamNameNow").innerText = next3AwayTeam
            document.getElementById("nextHomeTeamName").innerText = next4HomeTeam
            document.getElementById("nextAwayTeamName").innerText = next4AwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = next5HomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = next5AwayTeam
        }   else if (nm === 4) {
            document.getElementById("previousPreviousHomeTeamName").innerText = nextNextMatchHomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = nextNextMatchAwayTeam
            document.getElementById("previousHomeTeamName").innerText = next3HomeTeam
            document.getElementById("previousAwayTeamName").innerText = next3AwayTeam
            document.getElementById("homeTeamNameNow").innerText = next4HomeTeam
            document.getElementById("awayTeamNameNow").innerText = next4AwayTeam
            document.getElementById("nextHomeTeamName").innerText = next5HomeTeam
            document.getElementById("nextAwayTeamName").innerText = next5AwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = next6HomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = next6AwayTeam
        } else if (nm === 5) {
            document.getElementById("previousPreviousHomeTeamName").innerText = next3HomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = next3AwayTeam
            document.getElementById("previousHomeTeamName").innerText = next4HomeTeam
            document.getElementById("previousAwayTeamName").innerText = next4AwayTeam
            document.getElementById("homeTeamNameNow").innerText = next5HomeTeam
            document.getElementById("awayTeamNameNow").innerText = next5AwayTeam
            document.getElementById("nextHomeTeamName").innerText = next6HomeTeam
            document.getElementById("nextAwayTeamName").innerText = next6AwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = next7HomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = next7AwayTeam
        }   else if (pm === 28) {
            document.getElementById("previousPreviousHomeTeamName").innerText = previous3HomeTeam
            document.getElementById("previousPreviousAwayTeamName").innerText = previous3AwayTeam
            document.getElementById("previousHomeTeamName").innerText = previousPreviousHomeTeam
            document.getElementById("previousAwayTeamName").innerText = previousPreviousAwayTeam
            document.getElementById("homeTeamNameNow").innerText = previousHomeTeam
            document.getElementById("awayTeamNameNow").innerText = previousAwayTeam
            document.getElementById("nextHomeTeamName").innerText = lastMatchHomeTeam
            document.getElementById("nextAwayTeamName").innerText = lastMatchAwayTeam
            document.getElementById("nextNextHomeTeamName").innerText = nextMatchHomeTeam
            document.getElementById("nextNextAwayTeamName").innerText = nextMatchAwayTeam
         } // else if (pm === 27) {
        //     document.getElementById("previousPreviousHomeTeamName").innerText = previous4HomeTeam
        //     document.getElementById("previousPreviousAwayTeamName").innerText = previous4AwayTeam
        //     document.getElementById("previousHomeTeamName").innerText = previous3HomeTeam
        //     document.getElementById("previousAwayTeamName").innerText = previous3AwayTeam
        //     document.getElementById("homeTeamNameNow").innerText = previousPreviousHomeTeam
        //     document.getElementById("awayTeamNameNow").innerText = previousPreviousAwayTeam
        //     document.getElementById("nextHomeTeamName").innerText = previousHomeTeam
        //     document.getElementById("nextAwayTeamName").innerText = previousAwayTeam
        //     document.getElementById("nextNextHomeTeamName").innerText = lastMatchHomeTeam
        //     document.getElementById("nextNextAwayTeamName").innerText = lastMatchAwayTeam
        // } else if (pm === 26) {
        //     document.getElementById("previousPreviousHomeTeamName").innerText = previous5HomeTeam
        //     document.getElementById("previousPreviousAwayTeamName").innerText = previous5AwayTeam
        //     document.getElementById("previousHomeTeamName").innerText = previous4HomeTeam
        //     document.getElementById("previousAwayTeamName").innerText = previous4AwayTeam
        //     document.getElementById("homeTeamNameNow").innerText = previous3HomeTeam
        //     document.getElementById("awayTeamNameNow").innerText = previous3AwayTeam
        //     document.getElementById("nextHomeTeamName").innerText = previousPreviousHomeTeam
        //     document.getElementById("nextAwayTeamName").innerText = previousPreviousAwayTeam
        //     document.getElementById("nextNextHomeTeamName").innerText = previousHomeTeam
        //     document.getElementById("nextNextAwayTeamName").innerText = previousAwayTeam
        // } else if (pm === 25) {
        //     document.getElementById("previousPreviousHomeTeamName").innerText = previous6HomeTeam
        //     document.getElementById("previousPreviousAwayTeamName").innerText = previous6AwayTeam
        //     document.getElementById("previousHomeTeamName").innerText = previous5HomeTeam
        //     document.getElementById("previousAwayTeamName").innerText = previous5AwayTeam
        //     document.getElementById("homeTeamNameNow").innerText = previous4HomeTeam
        //     document.getElementById("awayTeamNameNow").innerText = previous4AwayTeam
        //     document.getElementById("nextHomeTeamName").innerText = previous3HomeTeam
        //     document.getElementById("nextAwayTeamName").innerText = previous3AwayTeam
        //     document.getElementById("nextNextHomeTeamName").innerText = previousPreviousHomeTeam
        //     document.getElementById("nextNextAwayTeamName").innerText = previousPreviousAwayTeam
        // } else if (pm === 24) {
        //     document.getElementById("previousPreviousHomeTeamName").innerText = previous7HomeTeam
        //     document.getElementById("previousPreviousAwayTeamName").innerText = previous7AwayTeam
        //     document.getElementById("previousHomeTeamName").innerText = previous6HomeTeam
        //     document.getElementById("previousAwayTeamName").innerText = previous6AwayTeam
        //     document.getElementById("homeTeamNameNow").innerText = previous5HomeTeam
        //     document.getElementById("awayTeamNameNow").innerText = previous5AwayTeam
        //     document.getElementById("nextHomeTeamName").innerText = previous4HomeTeam
        //     document.getElementById("nextAwayTeamName").innerText = previous4AwayTeam
        //     document.getElementById("nextNextHomeTeamName").innerText = previous3HomeTeam
        //     document.getElementById("nextNextAwayTeamName").innerText = previous3AwayTeam
        // } 

        if (pm < 28) {
            document.getElementById("previousPreviousHomeTeamName").innerText = previousData.events[pm - 2].homeTeam.name
            document.getElementById("previousPreviousAwayTeamName").innerText = previousData.events[pm - 2].awayTeam.name
            document.getElementById("previousHomeTeamName").innerText = previousData.events[pm - 1].homeTeam.name
            document.getElementById("previousAwayTeamName").innerText = previousData.events[pm - 1].awayTeam.name
            document.getElementById("homeTeamNameNow").innerText = previousData.events[pm].homeTeam.name
            document.getElementById("awayTeamNameNow").innerText = previousData.events[pm].awayTeam.name
            document.getElementById("nextHomeTeamName").innerText = previousData.events[pm + 1].homeTeam.name
            document.getElementById("nextAwayTeamName").innerText = previousData.events[pm + 1].awayTeam.name
            document.getElementById("nextNextHomeTeamName").innerText = previousData.events[pm + 2].homeTeam.name
            document.getElementById("nextNextAwayTeamName").innerText = previousData.events[pm + 2].awayTeam.name
        }

        if (nm > 5) {
            document.getElementById("nextNextHomeTeamName").innerText = nextData.events[nm + 1].homeTeam.name
            document.getElementById("nextNextAwayTeamName").innerText = nextData.events[nm + 1].awayTeam.name            
            document.getElementById("nextHomeTeamName").innerText = nextData.events[nm ].homeTeam.name
            document.getElementById("nextAwayTeamName").innerText = nextData.events[nm ].awayTeam.name
            document.getElementById("homeTeamNameNow").innerText = nextData.events[nm - 1].homeTeam.name
            document.getElementById("awayTeamNameNow").innerText = nextData.events[nm - 1].awayTeam.name
            document.getElementById("previousHomeTeamName").innerText = nextData.events[nm - 2].homeTeam.name
            document.getElementById("previousAwayTeamName").innerText = nextData.events[nm - 2].awayTeam.name
            document.getElementById("previousPreviousHomeTeamName").innerText = nextData.events[nm - 3].homeTeam.name
            document.getElementById("previousPreviousAwayTeamName").innerText = nextData.events[nm - 3].awayTeam.name
        }

        if (nm > 0){
            let gameweek = nextData.events[nm-1];
            const tournament = gameweek.tournament.name;
            document.getElementById("tournament").innerText = tournament;
            const round = gameweek.roundInfo.round;
            document.getElementById("round").innerText = round;
            const homeTeam = gameweek.homeTeam.name;
            document.getElementById("homeTeamName").innerText = homeTeam;
            const homeTeamScore = 0;
            document.getElementById("homeTeamScore").innerText = homeTeamScore;
            const awayTeam = gameweek.awayTeam.name;
            document.getElementById("awayTeamName").innerText = awayTeam;
            const awayTeamScore = 0;
            document.getElementById("awayTeamScore").innerText = awayTeamScore;
            const status = gameweek.status.description
            document.getElementById("status").innerText = status;

        } else if (pm <= 29) {
            let gameweek = previousData.events[pm];
            const tournament = gameweek.tournament.name;
            document.getElementById("tournament").innerText = tournament;
            const round = gameweek.roundInfo.round;
            document.getElementById("round").innerText = round;
            const homeTeam = gameweek.homeTeam.name;
            document.getElementById("homeTeamName").innerText = homeTeam;
            const homeTeamScore = gameweek.homeScore.display;
            document.getElementById("homeTeamScore").innerText = homeTeamScore;
            const awayTeam = gameweek.awayTeam.name;
            document.getElementById("awayTeamName").innerText = awayTeam;
            const awayTeamScore = gameweek.awayScore.display;
            document.getElementById("awayTeamScore").innerText = awayTeamScore;
            const status = gameweek.status.description
            document.getElementById("status").innerText = status;
        }

        
    }, 1000)


    } catch (error) {
    console.error("Error:", error.message);
    }
});


</script>


<main>

    <div class="spacer"></div>
    
    <div class="frontpage">


        <div class="matchbar">
            <div class="previousButton" id="priviousbtn"></div>
            <div class="previousMatch">
                <div class="previousMatch1">
                    <p id = previousPreviousHomeTeamName>Loading...</p>
                    <p id = previousPreviousAwayTeamName>Loading...</p>
                </div>
                <div class="previousMatch2">
                    <p id = previousHomeTeamName>Loading...</p>
                    <p id = previousAwayTeamName>Loading...</p>
                </div>
            </div>
            <div class="thisMatch">
                <p id="homeTeamNameNow">Loading...</p>
                <p id="awayTeamNameNow">Loading...</p>
            </div>
            
            <div class="nextMatch">
                <div class="nextMatch1">
                    <p id = nextHomeTeamName>Loading...</p>
                    <p id = nextAwayTeamName>Loading...</p>
                </div>
                <div class="nextMatch2">
                    <p id = nextNextHomeTeamName>Loading...</p>
                    <p id = nextNextAwayTeamName>Loading...</p>
                </div>
            </div>
                <div class="nextButton" id="nmbutton"></div>
        </div>

 

        <div class="mini-spacer"></div>
        <div class="info">
            <div class="homeTeam">
                <h1 id = homeTeamName>Loading...</h1>
            </div>

            <div class="middle">
                <div class="score">
                    <h2 class="home" id = homeTeamScore>Loading...</h2> - <h2 class="away" id = awayTeamScore>Loading...</h2> 
                </div>
                <div class="information">
                    <p id = tournament>Loading...</p>
                    <div class="info">
                        <p class="roundInfo">Round:</p><p class="roundInfo" id = round>Loading...</p>
                    </div>
                    <p id = status>Loading...</p>
                </div>
            </div>

            <div class="awayTeam">
                <h1 id = awayTeamName>Loading...</h1>
            </div>
        </div>
    </div>



    <div class="pageInfo">
        <p>This is a page that shows the results of the last matchday for my favorite football club FC Barcelona</p>    
    </div>
</main>



<Footer/>

<style>


    .spacer {
        height: 10em;
    }

    .mini-spacer{
        height: 5em;
    }

    .info{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: top;
        padding-left: 1.5em;
        gap: 0.5em;
        padding-right: 1.5em;
    }

    .score{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding-left: 1.5em;
        padding-right: 1.5em;
    }

    h2{
        font-size: 2em;
        font-family: "coolvetica";
        padding-left: 2em;
        padding-right: 2em;
    }

    h1{
        font-size: 2em;
        font-family: "coolvetica";
    }

    p{
        font-size: 1em;
        font-family: "coolvetica";
    }

    .middle{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1.5em;
    }

    .pageInfo{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1.5em;
        padding-left: 2em;
        padding-right: 2em;
        padding-top: 2em;
        padding-bottom: 2em;
    }

    .matchbar{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1.5em;
        padding-left: 2em;
        padding-right: 2em;
        padding-top: 2em;
        padding-bottom: 2em;
    }

    .previousMatch{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
    }

    .nextMatch{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1m;
    }

    .thisMatch{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
        box-shadow: 0 0 30px 5px #024D98;
    }

    .previousMatch1{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
        padding:15px;
        border: 2px solid #024D98;
        border-radius: 10px; 
        width: 150px;
        scale: 0.8;
        
    }

    .previousMatch2{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
        padding:15px;
        border: 2px solid #024D98;
        border-radius: 10px;
        width: 150px;
        scale: 1.0;
    }

    .nextMatch2{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
        padding:15px;
        border: 2px solid #024D98;
        border-radius: 10px;
        width: 150px;
        scale: 0.8;
    }

    .nextMatch1{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
        padding:15px;
        border: 2px solid #024D98;
        border-radius: 10px;
        width: 150px;
        scale: 1.0;
    }

    .thisMatch{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: coolvertica;
        font-size: 1em;
        padding:15px;
        border: 2px solid #024D98;
        border-radius: 10px;
        width: 150px;
        scale: 1.2;
    }

    .previousButton{    
        width: 0;
        height: 0;
        border-left: 50px solid transparent;
        border-right: 50px solid transparent;
        border-bottom: 50px solid #024D98;
        margin-right: 0;
        margin-left: 0;
        rotate: 270deg;
        scale: 0.5;
    }
    .previousButton:hover{
        cursor: pointer;
        scale:0.6;
    }

    .nextButton{    
        width: 0;
        height: 0;
        border-left: 50px solid transparent;
        border-right: 50px solid transparent;
        border-top: 50px solid #024D98;
        margin-right: 0;
        margin-left: 0;
        rotate: -90deg;
        scale: 0.5;
    }
    .nextButton:hover{
        cursor: pointer;
        scale: 0.6;
    }

    #homeTeamName{
        max-width: 150px;
        text-align: center;
    }

    #awayTeamName{
        max-width: 150px;
        text-align: center;
    }

    .roundInfo{
        position: flex;
        flex-direction: row;
    }




    p{
        font-size: 1em;
        font-family: "coolvetica";
        margin: 0;
    }
</style>