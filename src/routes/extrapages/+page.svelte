<script>
  import Button from "$lib/Components/button.svelte";
    import Footer from "$lib/Components/Footer.svelte";
    import { onMount } from 'svelte';

    onMount(() => {
        const url = 'https://www.sofascore.com/api/v1/unique-tournament/8/season/61643/events/round/5';

    fetch(url)
        .then(response => {
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error(`Error: ${response.status}`);
            }
        })
        .then(posts => {
            let n = 0;
            let team = '';
            let teamId = null;

            while (team !== 'Barcelona') {
                n++;
                const hometeam = posts.events[n].homeTeam.name;
                if (hometeam === 'Barcelona') {
                    teamId = posts.events[n].homeTeam.id;
                    team = 'Barcelona';
                }
                const awayteam = posts.events[n].awayTeam.name;
                if (awayteam === 'Barcelona') {
                    teamId = posts.events[n].awayTeam.id;
                    team = 'Barcelona';
                }
            }

            const match = posts.events[n];

            const performanceUrl = `https://www.sofascore.com/api/v1/team/${teamId}/performance`;
            return fetch(performanceUrl);
        })
        .then(response => {
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error(`Error: ${response.status}`);
            }
        })
        .then(performanceData => {
            const gameweek = performanceData.events[9];
            const tournament = gameweek.tournament.name;
            document.getElementById("tournament").innerText = tournament;

            const season = gameweek.season.name;
            document.getElementById("season").innerText = season;

            const homeTeam = gameweek.homeTeam.name;
            document.getElementById("homeTeamName").innerText = homeTeam;

            const homeTeamScore = gameweek.homeScore.display;
            document.getElementById("homeTeamScore").innerText = homeTeamScore;

            const awayTeam = gameweek.awayTeam.name;
            document.getElementById("awayTeamName").innerText = awayTeam;

            const awayTeamScore = gameweek.awayScore.display;
            document.getElementById("awayTeamScore").innerText = awayTeamScore;
        })
        .then(preiviusMatch => {
            const preiviusurl = 'https://www.sofascore.com/api/v1/team/2817/events/last/0';
            return fetch(preiviusurl);
        })
        .then(response => {
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error(`Error: ${response.status}`);
            }
        })
        .then(preiviusData => {
            let pm = 29; 

            const preiviusMatch = preiviusData.events[pm - 1];

            const preiviusHomeTeam = preiviusMatch.homeTeam.name;
            // console.log(preiviusHomeTeam);
            document.getElementById("preiviusHomeTeamName").innerText = preiviusHomeTeam;

            const preiviusAwayTeam = preiviusMatch.awayTeam.name;
            // console.log(preiviusAwayTeam);
            document.getElementById("preiviusAwayTeamName").innerText = preiviusAwayTeam;

            const preiviusMatch2 = preiviusData.events[pm - 2]

            const preiviusHomeTeam2 = preiviusMatch2.homeTeam.name;
            // console.log(preiviusHomeTeam2);
            document.getElementById("preiviusHomeTeamName2").innerText = preiviusHomeTeam2;

            const preiviusAwayTeam2 = preiviusMatch2.awayTeam.name;
            // console.log(preiviusAwayTeam2);
            document.getElementById("preiviusAwayTeamName2").innerText = preiviusAwayTeam2;

            const matchnow = preiviusData.events[pm];

            const homeTeam = matchnow.homeTeam.name;
            // console.log(homeTeam);
            document.getElementById("homeTeamNameNow").innerText = homeTeam;

            const awayTeam = matchnow.awayTeam.name;
            // console.log(awayTeam);
            document.getElementById("awayTeamNameNow").innerText = awayTeam;

            document.getElementById('preiviusbtn').addEventListener('click', () => {
                pm--;
                console.log(pm);
                const preiviusMatch = preiviusData.events[pm-1];

            const preiviusHomeTeam = preiviusMatch.homeTeam.name;
            // console.log(preiviusHomeTeam);
            document.getElementById("preiviusHomeTeamName").innerText = preiviusHomeTeam;

            const preiviusAwayTeam = preiviusMatch.awayTeam.name;
            // console.log(preiviusAwayTeam);
            document.getElementById("preiviusAwayTeamName").innerText = preiviusAwayTeam;

            const preiviusMatch2 = preiviusData.events[pm - 2]

            const preiviusHomeTeam2 = preiviusMatch2.homeTeam.name;
            // console.log(preiviusHomeTeam2);
            document.getElementById("preiviusHomeTeamName2").innerText = preiviusHomeTeam2;

            const preiviusAwayTeam2 = preiviusMatch2.awayTeam.name;
            // console.log(preiviusAwayTeam2);
            document.getElementById("preiviusAwayTeamName2").innerText = preiviusAwayTeam2;

            const matchnow = preiviusData.events[pm];

            const homeTeam = matchnow.homeTeam.name;
            // console.log(homeTeam);
            document.getElementById("homeTeamNameNow").innerText = homeTeam;

            const awayTeam = matchnow.awayTeam.name;
            // console.log(awayTeam);
            document.getElementById("awayTeamNameNow").innerText = awayTeam;


            }) 
        })
        .then(nextMatch => {
            const nexturl = 'https://www.sofascore.com/api/v1/team/2817/events/next/0';
            return fetch(nexturl);
        })
        .then(response => {
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error(`Error: ${response.status}`);
            }
        })
        .then(nextData => {
            let nm = 0; 
            const nextMatch = nextData.events[nm];

            const nextHomeTeam = nextMatch.homeTeam.name;
            // console.log(nextHomeTeam);
            document.getElementById("nextHomeTeamName").innerText = nextHomeTeam;

            const nextAwayTeam = nextMatch.awayTeam.name;
            // console.log(nextAwayTeam);
            document.getElementById("nextAwayTeamName").innerText = nextAwayTeam;

            const nextMatch2 = nextData.events[nm + 1];

            const nextHomeTeam2 = nextMatch2.homeTeam.name;
            // console.log(nextHomeTeam2);
            document.getElementById("nextHomeTeamName2").innerText = nextHomeTeam2;

            const nextAwayTeam2 = nextMatch2.awayTeam.name;
            // console.log(nextAwayTeam2);
            document.getElementById("nextAwayTeamName2").innerText = nextAwayTeam2;

            document.getElementById('nmbutton').addEventListener('click', () => {
                nm++;
                console.log(nm);

                const nextMatch = nextData.events[nm];

            const nextHomeTeam = nextMatch.homeTeam.name;
            // console.log(nextHomeTeam);
            document.getElementById("nextHomeTeamName").innerText = nextHomeTeam;

            const nextAwayTeam = nextMatch.awayTeam.name;
            // console.log(nextAwayTeam);
            document.getElementById("nextAwayTeamName").innerText = nextAwayTeam;

            const nextMatch2 = nextData.events[nm + 1];

            const nextHomeTeam2 = nextMatch2.homeTeam.name;
            // console.log(nextHomeTeam2);
            document.getElementById("nextHomeTeamName2").innerText = nextHomeTeam2;

            const nextAwayTeam2 = nextMatch2.awayTeam.name;
            // console.log(nextAwayTeam2);
            document.getElementById("nextAwayTeamName2").innerText = nextAwayTeam2;   

        })
        .catch(error => {
            console.error('Error:', error.message);
        });
    });

})
</script>






<main>

    <div class="spacer"></div>
    
    <div class="frontpage">


        <div class="matchbar">
            <div class="preiviusButton" id="preiviusbtn"></div>
            <div class="preiviusMatch">
                <div class="preiviusMatch1">
                    <p id = preiviusHomeTeamName2>Loading...</p>
                    <p id = preiviusAwayTeamName2>Loading...</p>
                </div>
                <div class="preiviusMatch2">
                    <p id = preiviusHomeTeamName>Loading...</p>
                    <p id = preiviusAwayTeamName>Loading...</p>
                </div>
            </div>
            <div class="thisMatch">
                <p id="homeTeamNameNow"></p>
                <p id="awayTeamNameNow"></p>
            </div>
            
            <div class="nextMatch">
                <div class="nextMatch1">
                    <p id = nextHomeTeamName>Loading...</p>
                    <p id = nextAwayTeamName>Loading...</p>
                </div>
                <div class="nextMatch2">
                    <p id = nextHomeTeamName2>Loading...</p>
                    <p id = nextAwayTeamName2>Loading...</p>
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
                    <p id = season>Loading...</p>
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
        gap: 2em;
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

    .preiviusMatch{
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
    }

    .preiviusMatch1{
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

    .preiviusMatch2{
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

    .preiviusButton{    
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
    .preiviusButton:hover{
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



    p{
        font-size: 1em;
        font-family: "coolvetica";
        margin: 0;
    }
</style>