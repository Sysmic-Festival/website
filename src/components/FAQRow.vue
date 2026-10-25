<script setup>
import { reactive } from "vue";

defineProps(["title"]);

const data = reactive({
  opened: false,
});
</script>

<template>
  <div class="row" @click="data.opened = !data.opened">
    <div class="question">
      <p class="title">{{ title }}</p>
      <div class="icon" :class="{ 'is-open': data.opened }">+</div>
    </div>
    <div :class="data.opened ? 'openableContent opened' : 'openableContent'">
      <p class="answer"><slot /></p>
    </div>
  </div>
</template>

<style scoped>
.row {
  cursor: pointer;
  width: 100%;
  max-width: 640px;
  margin: 0 0 18px;
}

/* white block, blue square with the plus */
.question {
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  background: #fff;
  border: 2px solid #000;
  border-radius: 0;
}

.title {
  flex: 1;
  margin: 0;
  padding: 12px 18px;
  display: flex;
  align-items: center;
  color: #000;
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: -0.02em;
  text-align: left;
  transition: all 0.2s ease-in-out;
}
.title:hover {
  color: #0037ff;
}

.icon {
  flex: 0 0 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0037ff;
  color: #fff;
  font-size: 2rem;
  font-weight: bold;
  transition: transform 0.3s ease;
}
.icon.is-open {
  transform: rotate(45deg);   /* + becomes × */
}

/* the animated wrapper has no padding, so it collapses fully */
.openableContent {
  max-height: 0;
  overflow: hidden;
  transition: max-height ease 0.8s;
}
.opened {
  max-height: 300px;
}

.answer {
  margin: 8px 0 0 28px;       /* indented, slightly disaligned */
  padding: 14px 18px;
  background: #0037ff;
  color: #fff;
  font-size: 1.15rem;
  line-height: 1.4;
  text-align: left;
}

@media only screen and (max-width: 800px) {
  .title { font-size: 1.2rem; padding: 10px 14px; }
  .icon { flex-basis: 46px; }
  .answer { margin-left: 12px; font-size: 1rem; }
  .opened { max-height: 600px; }
}
</style>