
<script setup>
import {onMounted} from 'vue'
onMounted(() => {
    startTimer();
})

/* TIMER */
function startTimer(){
    var goalDate = new Date(2022, 9, 21, 19, 30).getTime()
    var curDate  = new Date().getTime()
  
    if(goalDate >= curDate){
  
      var diff = (goalDate - curDate)/1000
  
      //console.log(diff)
  
      var jours  = Math.floor(diff / (60*60*24))
      diff -= jours*60*60*24
  
      var heures = Math.floor(diff / (60*60))
      diff -= heures*60*60
  
      var minutes = Math.floor(diff / 60)
      diff -= minutes*60
  
      var secondes = Math.floor(diff)
  
      document.getElementById("daysBox").innerHTML    = jours
      document.getElementById("hoursBox").innerHTML   = heures
      document.getElementById("minutesBox").innerHTML = minutes
      document.getElementById("secBox").innerHTML     = secondes
  
      document.getElementById("labelDay").innerHTML     = (jours == 1 ||  jours == 0)      ? "Jour" : "Jours"
      document.getElementById("labelHours").innerHTML   = (heures == 1 || heures == 0)     ? "Heure" : "Heures"
      document.getElementById("labelMinutes").innerHTML = (minutes == 1 || minutes == 0)   ? "Minute" : "Minutes"
      document.getElementById("labelSec").innerHTML     = (secondes == 1 || secondes == 0) ? "Seconde" : "Secondes"
  
      
    }else{
      document.getElementById("daysBox").innerHTML    = 0
      document.getElementById("hoursBox").innerHTML   = 0
      document.getElementById("minutesBox").innerHTML = 0
      document.getElementById("secBox").innerHTML     = 0
    }
  
    setTimeout(startTimer, 1000)
  }
</script>

<template>
    <section class="timer-section">
	    <div class="decompte">
	    	<div class="decompteLine"><hr></div>
	    	<div>
	    		<div id="daysBox" class="decompteNumber">000</div>
	    		<div id="labelDay" class="numberLabel label1">Jours</div>
	    	</div>
	    	<div>
	    		<div id="hoursBox" class="decompteNumber">00</div>
	    		<div id="labelHours" class="numberLabel label2">Heures</div>
	    	</div>
	    	<div>
	    		<div id="minutesBox" class="decompteNumber">00</div>
	    		<div id="labelMinutes" class="numberLabel label3">Minutes</div>
	    	</div>
	    	<div>
	    		<div id="secBox" class="decompteNumber">00</div>
	    		<div id="labelSec" class="numberLabel label4"> Secondes</div>
	    	</div>
	    	<div class="decompteLine"><hr></div>
	    </div>
    </section>
</template>


<style scoped>
    .decompte{  

        display: flex;
        justify-content: space-around;
        align-items: center;
        text-align: center;
        margin-bottom:25px;
    }
    .decompteNumber{
        max-height:120px;
        max-width:120px;
        height: 14vw;
        width: 14vw;
        
        border-radius: 10px;
        margin-left:20px;
        margin-right:20px;
        color : var(--primary);
        font-size: 58pt;
        padding-top: 0px;
        font-weight: bold;
    }

    #daysBox{
        background-color: var(--third);
        max-width:240px;
        width: 28vw;
    }
    #hoursBox{
        background-color: var(--third);
    }
    #minutesBox{
        background-color: var(--third);
    }
    #secBox{
        background-color: var(--third);
    }

    .numberLabel{
        text-align: left;
        margin-left: 20px;
        font-size: 25pt;
        margin-top: 5px;
    }
    .label1{
        color: var(--secondary);
    }
    .label2{
        color : var(--secondary);
    }
    .label3{
        color : var(--secondary);
    }
    .label4{
        color : var(--secondary);
    }

    .decompteLine hr{
        width:75px;
        position: relative;
        top: -17px;
        border: 1px solid var(--secondary);
    }

    @media only screen and (max-width: 850px){
        .decompte{
            width: 100%;
            justify-content: center;
            position: relative;
        }
        .decompteNumber{
            font-size: 8.5vw;
            margin-left: 2vw;
            margin-right: 2vw;
        }
        .decompteLine{
            display:none;
        }
        .numberLabel{
            text-align: center;
            font-size: 3vw;
            margin-left: 0;
        }

        .newsContainer{
            width:90vw;
            margin-left:4vw;
        }

    }

    .timer-section{
        display: flex;
        align-self: center;
        justify-content: center;
    }

    @media only screen and (max-width: 700px){
        .h2BorderContainer{
            margin-left: 20px;
        }
        .newsTitre{
            font-size: 7vw;
        }
        .newsSousTitre{
            font-size: 2.8vw;
        }
        .newsContainer:hover .newsTitre{
            font-size: 7vw;
        }
        .newsContainer:hover .newsSousTitre{
            font-size: 2.8vw;
        }
        .mainP{
            font-size:8vw;
        }
        .secondP{
        	font-size:5vw;
        }
    }



</style>