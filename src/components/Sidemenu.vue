<script setup>
import { reactive } from 'vue';
import Player from './Player.vue';

defineProps(["open"])

const state = reactive({
  playerDisplayed: false,
})

function displayPlayer(e) {
  e.preventDefault();
  state.playerDisplayed = true
}

</script>

<template>
    <div :class="open ? 'sidebar opened' : 'sidebar'">
      <section class="sidebar-section">
        <a href="#">Line-up</a>
        <hr class="sidebar-links-hr">
        <a href="#">Infos</a>
        <hr class="sidebar-links-hr">
        <a href="#">Sponsors</a>
        <hr class="sidebar-links-hr">
        <a href="#">Qui sommes-nous?</a>
        <hr class="sidebar-links-hr">
        <a href="#">Programmation</a>
        <hr class="sidebar-links-hr">
        <a href="#">À propos</a>
        <hr class="sidebar-links-hr">
        <a href="#">Plan du Festival</a>
        <hr class="sidebar-links-hr">
        <a href="#">FAQ</a>
      </section>
      <section id="player-button">
        <a href="#" @click="displayPlayer">Player</a>
        <Player :displayed="state.playerDisplayed" @displayedUpdated="val => state.playerDisplayed = val"></Player>
      </section>
    </div>
</template>

<style scoped>
     /* The sidebar menu */
.sidebar {
  z-index: 900;
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  top: 0;
  right: 0;
  background-color: var(--primary); /* Black*/
  background-position: bottom;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: calc(var(--navbar-height) + var(--global-margin)); /* Place content 60px from the top */
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
  
  padding: 8px 8px 6px 0px;
  text-decoration: none;
  font-size: 25px;
  color: var(--white);
  display: block;
  transition: 0.3s;
}

/* When you mouse over the navigation links, change their color */
.sidebar a:hover {
  color: var(--third);
}

/* Position and style the close button (top right corner) */
.sidebar .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

/* Style page content - use this if you want to push the page content to the right when you open the side navigation */
/* #main {
  transition: margin-left .5s;
  padding: 20px;
} */

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}
} 

#player-button{
  flex-grow: 1;
}

.sidebar-links-hr{
  width: 80%;
  color: var(--third);
}

</style>