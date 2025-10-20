<script setup>
import { onMounted } from "vue";
onMounted(() => {
  startTimer();
});

/* TIMER */
function startTimer() {
  var goalDate = new Date(2025, 10, 7, 19, 0).getTime();
  var curDate = new Date().getTime();

  try {
    if (goalDate >= curDate) {
      var diff = (goalDate - curDate) / 1000;

      //console.log(diff)

      var jours = Math.floor(diff / (60 * 60 * 24));
      diff -= jours * 60 * 60 * 24;

      var heures = Math.floor(diff / (60 * 60));
      diff -= heures * 60 * 60;

      var minutes = Math.floor(diff / 60);
      diff -= minutes * 60;

      var secondes = Math.floor(diff);

      document.getElementById("daysBox").innerHTML = jours;
      document.getElementById("hoursBox").innerHTML = heures;
      document.getElementById("minutesBox").innerHTML = minutes;
      document.getElementById("secBox").innerHTML = secondes;

      document.getElementById("labelDay").innerHTML =
        jours == 1 || jours == 0 ? "Jour" : "Jours";
      document.getElementById("labelHours").innerHTML =
        heures == 1 || heures == 0 ? "Heure" : "Heures";
      document.getElementById("labelMinutes").innerHTML =
        minutes == 1 || minutes == 0 ? "Minute" : "Minutes";
      document.getElementById("labelSec").innerHTML =
        secondes == 1 || secondes == 0 ? "Seconde" : "Secondes";
    } else {
      document.getElementById("daysBox").innerHTML = 0;
      document.getElementById("hoursBox").innerHTML = 0;
      document.getElementById("minutesBox").innerHTML = 0;
      document.getElementById("secBox").innerHTML = 0;
    }
  } catch (e) {}

  setTimeout(startTimer, 1000);
}
</script>

<template>
  <section class="timer-section">
    <div class="decompte">
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
        <div id="labelSec" class="numberLabel label4">Secondes</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.decompte {
  display: flex;
  justify-content: space-around;
  align-items: center;
  text-align: center;
  margin-bottom: 30px;
}

.decompteNumber {
  opacity: 1;

  max-height: 80px;
  max-width: 100px;
  height: 10vw;
  width: 14vw;

  border-radius: 10px;
  margin-left: 20px;
  margin-right: 20px;
  color: var(--white);
  font-size: 8vh;
  padding-top: 0px;
  font-weight: bold;

  font-family: Roboto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#daysBox {
  background-color: var(--third);
  max-width: 240px;
  width: 28vh;
  height: 10vh;
}

#hoursBox {
  background-color: var(--third);
  width: 20vh;
  height: 10vh;
}

#minutesBox {
  background-color: var(--third);
  width: 20vh;
  height: 10vh;
}

#secBox {
  background-color: var(--third);
  width: 20vh;
  height: 10vh;
}

.numberLabel {
  text-align: left;
  margin-left: 20px;
  font-size: 4vh;
  margin-top: 5px;
}

.label1 {
  color: var(--white);
}

.label2 {
  color: var(--white);
}

.label3 {
  color: var(--white);
}

.label4 {
  color: var(--white);
}

.decompteLine hr {
  width: 75px;
  position: relative;
  top: -17px;
  border: 1px solid var(--secondary);
}

.timer-section {
  display: flex;
  align-self: center;
  justify-content: center;
  z-index: 100;
}

@media only screen and (max-width: 850px) {
  .decompte {
    width: 100%;
    justify-content: center;
    position: relative;
    margin-bottom: 10px;
  }

  .decompteNumber {
    font-size: 8.5vw;
    margin-left: 2vw;
    margin-right: 2vw;
  }

  .decompteLine {
    display: none;
  }

  .numberLabel {
    text-align: center;
    font-size: 3vw;
    margin-left: 0;
  }

  .newsContainer {
    width: 90vw;
    margin-left: 4vw;
  }
}

@media only screen and (max-height: 1280px) {
  .timer-section {
    padding: 0;
    padding-top: 3px;
  }
}

@media only screen and (max-height: 700px) {
}

@media only screen and (max-width: 700px) {
  #daysBox {
    height: 5%;
    width: 25vw;
  }
  #hoursBox {
    height: 5%;
    width: 15vw;
  }
  #minutesBox {
    height: 5%;
    width: 15vw;
  }
  #secBox {
    height: 5%;
    width: 15vw;
  }
  .h2BorderContainer {
    margin-left: 20px;
  }

  .newsTitre {
    font-size: 7vw;
  }

  .newsSousTitre {
    font-size: 2.8vw;
  }

  .newsContainer:hover .newsTitre {
    font-size: 7vw;
  }

  .newsContainer:hover .newsSousTitre {
    font-size: 2.8vw;
  }

  .mainP {
    font-size: 8vw;
  }

  .secondP {
    font-size: 5vw;
  }

  .timer-section {
    padding: 25px;
  }
}
</style>
