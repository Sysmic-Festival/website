<script setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import Player from './Player.vue';

defineProps(["open"])
const emits = defineEmits(["openedUpdate"])

const state = reactive({
  playerDisplayed: false,
})

function closeSideMenu() {
  emits("openedUpdate", false)
}

function displayPlayer(e) {
  e.preventDefault();
  state.playerDisplayed = true
}

const router = useRouter();

router.beforeEach(() => {
  emits("openedUpdate", false);
});

</script>

<template>
    <div :class="open ? 'sidebar opened' : 'sidebar'">
      <section class="sidebar-section">
        <label class="cross" @click="closeSideMenu">
          <div class="line"></div>
          <div class="line"></div>
        </label>
        <router-link to="/#line-up">Line-up</router-link>
        <hr id="sidebar-links-hr">
        <router-link to="/#infos">Infos</router-link>
        <hr id="sidebar-links-hr">
        <router-link to="/#sponsors">Sponsors</router-link>
        <hr id="sidebar-links-hr">
        <router-link to="/#association">Qui sommes-nous?</router-link>
        <hr id="sidebar-links-hr">
        <router-link to="/portfolio">Portfolio</router-link>
        <hr id="sidebar-links-hr">
        <router-link to="/about-us">À propos</router-link>
        <hr id="sidebar-links-hr">
        <router-link to="/faq">FAQ</router-link>
        <hr id="sidebar-links-hr">

      </section>
      <section id="player-button-section">
        <a href="#" @click="displayPlayer"><img class="player-button" src="@/assets/images/utilitaries/play-button.png"></a>
        <Player :displayed="state.playerDisplayed" @displayedUpdated="val => state.playerDisplayed = val"></Player>
      </section>
    </div>
</template>

<style scoped>
     /* The sidebar menu */
.sidebar {
  z-index: 902;
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  top: 0;
  right: 0;
  background-color: var(--primary); /* Black*/
  background-position: bottom;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: calc(var(--navbar-height) + 2*var(--global-margin)); /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidebar */
  display: flex;
  flex-direction: column;
  justify-content: start;
}

.sidebar.opened {
  width: calc(min(350px, 100vw));
  box-shadow: 0px 0px 20px 60px rgba(0,0,0,.1);
}

/* The sidebar links */
.sidebar a {
  white-space: nowrap;
  overflow: hidden;
  
  padding: 4px 8px 6px 0px;
  text-decoration: none;
  font-size: 25px;
  color: var(--white);
  display: block;
  transition: 0.3s;
}

#player-button-section{
  display:flex;
}

.player-button{
  height: 20%;
  transition-duration: 0.5s;
}

.player-button:hover{
  transform: scale(1.05);
  
}

/* When you mouse over the navigation links, change their color */
.sidebar a:hover {
  color: var(--third);
}

/* Style page content - use this if you want to push the page content to the right when you open the side navigation */
/* #main {
  transition: margin-left .5s;
  padding: 20px;
} */


/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 400px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}

} 

@media screen and (max-width: 500px) {
  .sidebar.opened {
    width: 100vw;
    box-shadow: 0px 0px 20px 60px rgba(0,0,0,.1);
  }
} 

#player-button-section{
  flex-grow: 1;
  vertical-align: bottom;
}

#sidebar-links-hr{
  width: 80%;
  border: 1px solid var(--third);
}

@media only screen and (max-height: 700px){
   .sidebar a{
    font-size: 15px;
  }
}
.cross {
  position: relative;
  min-width: 20px;
  height: 40px;
  display: block;
  outline: none;
  cursor: pointer;
  left: 20px;
  top: -50px;
}
.cross .line {
  position: absolute;
  left: 10px;
  width: 30px;
  height: 4px;
  background: var(--white);
  border-radius: 10px;
  overflow: hidden;
}
.cross:hover .line::after {
    transform: translateX(0);
    transform: translateY(0);
  }
.cross .line:nth-child(1){
    transform:  rotate(45deg);
    top: 50%;
}

.cross .line:nth-child(2){
    transform:  rotate(-45deg);
    top: 50%;
}

.cross .line::after {
  position: absolute;
  content: "";
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--third);
  transform: translateX(-100%);
}
.cross .line:nth-child(1)::after {
    transition: 0.1s;
}
.cross .line:nth-child(2)::after {
    transition: 0.3s;
}


</style>