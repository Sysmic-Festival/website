<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import Player from "./Player.vue";

defineProps(["open"]);
const emits = defineEmits(["openedUpdate"]);

const state = reactive({
  playerDisplayed: false,
});

function closeSideMenu() {
  emits("openedUpdate", false);
}

function displayPlayer(e) {
  e.preventDefault();
  state.playerDisplayed = true;
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

      <router-link to="/#line-up" style="--x: 0px">Line up</router-link>
      <router-link to="/#infos" style="--x: 40px">Infos pratiques</router-link>
      <router-link to="/#association" style="--x: 10px">L'association</router-link>
      <router-link to="/portfolio" style="--x: 55px">Portfolio</router-link>
      <router-link to="/about-us" style="--x: 5px">À propos</router-link>
      <router-link to="/faq" style="--x: 45px">FAQ</router-link>
    </section>
    <!-- <section id="player-button-section">
      <a href="#" @click="displayPlayer"
        ><img
          class="player-button"
          src="@/assets/images/utilitaries/play-button.png"
      /></a>
      <Player
        :displayed="state.playerDisplayed"
        @displayedUpdated="(val) => (state.playerDisplayed = val)"
      ></Player>
    </section> -->
  </div>
</template>

<style scoped>
/* The sidebar menu */
.sidebar {
  z-index: 9002;
  width: 0;
  position: fixed;
  top: 0;
  right: 0;
  background-color: var(--primary);
  overflow-x: hidden;
  padding-top: calc(var(--navbar-height) + 2 * var(--global-margin));
  transition: 0.5s;
  display: flex;
  flex-direction: column;
  justify-content: start;
}

.sidebar.opened {
  width: calc(min(300px, 100vw));
  box-shadow: 0px 0px 20px 60px rgba(0, 0, 0, 0.1);
}

.sidebar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;                         
  padding: 0 30px 30px;
}

.sidebar a {
  white-space: nowrap;
  display: block;
  padding: 6px 18px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  text-decoration: none;

  font-size: 2rem;
  font-weight: bold;
  line-height: 1.1;
  letter-spacing: normal;
  transform: translateX(var(--x, 0) scaleY(0.85));   
  transition: background 0.2s, color 0.2s;
}

.sidebar a:hover {
  background: #0037ff;
  color: #fff;
}

/* current page */
.sidebar a.router-link-exact-active {
  background: #0037ff;
  color: #fff;
}

/* close button: white square with a cross */
.cross {
  position: relative;
  width: 44px;
  height: 44px;
  display: block;
  align-self: flex-end;
  margin-bottom: 10px;
  background: #fff;
  border: 2px solid #000;
  outline: none;
  cursor: pointer;
  transition: background 0.2s;
}
.cross:hover {
  background: #0037ff;
}

.cross .line {
  position: absolute;
  left: 6px;
  top: 50%;
  width: 28px;
  height: 4px;
  background: #000;
  transition: background 0.2s;
}
.cross:hover .line {
  background: #fff;
}
.cross .line:nth-child(1) {
  transform: translateY(-50%) rotate(45deg);
}
.cross .line:nth-child(2) {
  transform: translateY(-50%) rotate(-45deg);
}

#player-button-section {
  display: flex;
  flex-grow: 1;
  vertical-align: bottom;
}

.player-button {
  height: 20%;
  transition-duration: 0.5s;
}

.player-button:hover {
  transform: scale(1.05);
}

@media screen and (max-height: 400px) {
  .sidebar {
    padding-top: 15px;
  }
  .sidebar a {
    font-size: 18px;
  }
}

@media screen and (max-width: 500px) {
  .sidebar.opened {
    width: 100vw;
  }
  .sidebar-section {
    padding: 0 20px 30px;
  }
  .sidebar a {
    transform: translateX(calc(var(--x) * 0.5)) scaleY(0.85);
  }
}

@media only screen and (max-height: 700px) {
  .sidebar a {
    font-size: 15px;
    padding: 6px 16px;
  }
  .sidebar-section {
    gap: 12px;
  }
}
</style>