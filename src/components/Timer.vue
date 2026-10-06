<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const goalDate = new Date(2026, 9, 30, 20, 0).getTime();
const display = ref("00D 00H 00M 00S");
let timerId = null;

const pad = (n) => String(n).padStart(2, "0");

function updateTimer() {
  const diff = Math.max(0, Math.floor((goalDate - Date.now()) / 1000));

  const d = Math.floor(diff / 86400);
  const h = Math.floor((diff % 86400) / 3600);
  const m = Math.floor((diff % 3600) / 60);
  const s = diff % 60;

  display.value = `${pad(d)}D ${pad(h)}H ${pad(m)}M ${pad(s)}S`;
}

onMounted(() => {
  updateTimer();
  timerId = setInterval(updateTimer, 1000);
});

onUnmounted(() => clearInterval(timerId));
</script>

<template>
  <section class="timer-section">
    <p class="decompte glitch" :data-text="display">{{ display }}</p>
  </section>
</template>

<style scoped>
.timer-section {
  display: flex;
  align-self: center;
  justify-content: center;
  z-index: 100;
  padding: 5px;
}

.decompte {
  margin: 0;
  color: var(--white);
  font-family: 'Nunito', sans-serif;
  font-size: clamp(1.5rem, 6vw, 3rem);
  font-weight: bold;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.05em;
  white-space: nowrap;
}

/* GLITCH */
.glitch {
  position: relative;
}

.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
}

.glitch::before {
  color: rgba(0, 255, 234, 0.863);
  transform: translateX(-2px);
  animation: glitch-top 2.5s infinite linear alternate-reverse;
}

.glitch::after {
  color: rgba(225, 0, 255, 0.911);
  transform: translateX(2px);
  animation: glitch-bottom 3s infinite linear alternate-reverse;
}

@keyframes glitch-top {
  0%, 90%  { clip-path: inset(0 0 100% 0); }
  92%      { clip-path: inset(10% 0 60% 0); transform: translateX(-4px); }
  94%      { clip-path: inset(50% 0 20% 0); transform: translateX(3px); }
  96%      { clip-path: inset(30% 0 40% 0); transform: translateX(-3px); }
  98%, 100% { clip-path: inset(0 0 100% 0); }
}

@keyframes glitch-bottom {
  0%, 85%  { clip-path: inset(100% 0 0 0); }
  87%      { clip-path: inset(60% 0 10% 0); transform: translateX(4px); }
  91%      { clip-path: inset(20% 0 50% 0); transform: translateX(-3px); }
  95%      { clip-path: inset(70% 0 5% 0); transform: translateX(3px); }
  97%, 100% { clip-path: inset(100% 0 0 0); }
}

/* Respect users who disable animations */
@media (prefers-reduced-motion: reduce) {
  .glitch::before,
  .glitch::after {
    animation: none;
    display: none;
  }
}
</style>