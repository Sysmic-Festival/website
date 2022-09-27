<script setup>
import { onMounted, reactive } from 'vue'
import Sidemenu from './Sidemenu.vue'

const state = reactive({
  sticky: false,
  stickyPosition: 0,
  navbar: null,
  root: null,
  sideMenuOpened: false
})

onMounted(() => {
  // When the user scrolls the page, execute myFunction
  window.onscroll = function() {onScroll()};

  // Get the navbar
  state.navbar = document.getElementById("navbar");
  state.root = document.documentElement;

  // Get the offset position of the navbar
  state.stickyPosition = navbar.offsetTop;
})

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
// the minus part is so that the header sticks as soon as the top margin is reached, so it doesn't jump (removing the "px" from the margin)
function onScroll() {
  if (state.navbar && window.pageYOffset >= state.stickyPosition) {
    state.sticky = true
  } else {
    state.sticky = false
  }
}
</script>

<template>

  <Sidemenu :open="state.sideMenuOpened"></Sidemenu>

  <nav :class="{ sticky: state.sticky }" id="navbar" ref="main-navbar">
    <div class="container-navbar">
      <a class="logo" href="index.html">
        <img class = img-responsive src="@/assets/images/logo.svg" />
      </a>
      <ul class="bar-menu">
        <li><a href="#!">Line-up</a></li>
        <li><a href="#!">Infos</a></li>
        <li><a href="#!">Sponsors</a></li>
        <li><a href="#!">Qui sommes-nous?</a></li>
      </ul>
      
        <input type="checkbox" id="burger-toggle">
        <label for="burger-toggle" class="burger-menu" @click="state.sideMenuOpened = !state.sideMenuOpened">
          <div class="line"></div>
          <div class="line"></div>
          <div class="line"></div>
        </label>

    </div>
  </nav>
</template>

<style scoped>
#navbar{
  z-index: 901;
  position: absolute;
  height: calc(var(--navbar-height) + var(--global-margin));
  width: 100%;
  top: calc(100vh - var(--navbar-height) - var(--global-margin));
  background-color: var(--primary);
  box-shadow: 0px 0px 20px 30px rgba(0,0,0,.2);
  display: flex;
  flex-direction: column; 
  justify-content: center;
}

#navbar .container-navbar{  
  height: var(--navbar-height);
  display: flex;
  justify-content: space-between;
}

#navbar .container-navbar .logo{
  height: var(--navbar-height);
  /* adjusting Y axis to align with menu */
  /*transform: translateY(calc(-0.05*var(--navbar-height))); */
}

#navbar .container-navbar .logo img{
  max-height: 100%;
  max-width: none;
}


.container-navbar{
  position: relative;
  align-items: center;
  justify-content: space-between;
  margin-top: 0;
  margin-bottom: 0;
  margin-left: var(--global-margin);
  margin-right: var(--global-margin);
  display: flex;
}

/* bar menu for large enough screens + hover properties for whole navbar */
@media screen and (min-width: 790px){
  .bar-menu li a:hover {
    color: var(--third);
  }

  .burger-menu:hover .line::after {
    transform: translateX(0);
  }

  .bar-menu {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: var(--global-margin);
    list-style: none;
  }
  
  .bar-menu li {
    width: auto;
    height: auto;
    margin-right: 10%;
  }
  .bar-menu li a {
    font-size: 2vw;
    color: var(--white);
    text-decoration: none;
    transition: all 0.45s;
  }
  
}


@media screen and (max-width: 790px){
  
  .bar-menu {
    display: block;
    width: 100%;
    list-style: none;
  }

  .bar-menu li{
    display: none;
    width: auto;
    height: auto;
    text-align: center;
  }
  .bar-menu li a {
    font-size: 23px;
    color: var(--white);
    text-decoration: none;
    display: block;
    padding: 14px 16px;
  }
  
}

#burger-toggle {
  appearance: none;
  opacity: 0;
}

input[id = burger-toggle]:checked ~ .side-menu {
  transform: scaleX(1);
}

#burger-toggle:checked ~ .side-menu .sidebar-item span div,
#burger-toggle:checked ~ .side-menu img,
#burger-toggle:checked ~ .side-menu .sidebar-item {
  transform: translateY(0);
  transition: 0.5s 0.1s cubic-bezier(0.35, 0, 0.07, 1);
}

#burger-toggle:checked ~ .burger-menu .line::after {
  transform: translateX(0);
}
#burger-toggle:checked ~ .burger-menu .line:nth-child(1) {
  transform: translateY(calc(var(--navbar-height) / 5)) rotate(45deg);
}
#burger-toggle:checked ~ .burger-menu .line:nth-child(2) {
  transition-duration: 0.1s;
  transform: scaleX(0);
}
#burger-toggle:checked ~ .burger-menu .line:nth-child(3) {
  transform: translateY(calc(var(--navbar-height) / -5)) rotate(-45deg);
}

.burger-container{
  width: var(--navbar-height);
  height: var(--navbar-height);
}

.burger-menu {
  position: relative;
  min-width: var(--navbar-height);
  height: var(--navbar-height);
  display: block;
  outline: none;
  cursor: pointer;
}
.burger-menu .line {
  position: absolute;
  left: 25%;
  width: 50%;
  height: 4px;
  background: var(--white);
  border-radius: 10px;
  overflow: hidden;
  transition: 0.5s;
}
.burger-menu .line:nth-child(1) {
  top: 30%;
}
.burger-menu .line:nth-child(2) {
  top: 50%;
}
.burger-menu .line:nth-child(3) {
  top: 70%;
}
.burger-menu .line::after {
  position: absolute;
  content: "";
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--third);
  transform: translateX(-100%);
  transition: 0.25s;
}
.burger-menu .line:nth-child(2)::after {
  transition-delay: 0.1s;
}
.burger-menu .line:nth-child(3)::after {
  transition-delay: 0.2s;
}

#navbar.sticky {
  position: fixed;
  top: 0;
}

#navbar.img-responsive {
  display: block;
  max-height: 100%;
  width: auto;
}
</style>
