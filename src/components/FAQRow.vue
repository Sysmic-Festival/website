<script setup>
import { reactive } from "vue";

defineProps(["title"]);

const data = reactive({
  opened: false,
});
</script>

<template>
  <div class="row container" @click="data.opened = !data.opened">
    <div class="img">
      <img v-if="data.opened" src="@/assets/images/utilitaries/minus.svg" />
      <img v-else src="@/assets/images/utilitaries/plus.svg" />
    </div>
    <div class="text">
      <p class="title">{{ title }}</p>
      <p :class="data.opened ? 'openableContent opened' : 'openableContent'">
        <slot />
      </p>
    </div>
  </div>
</template>

<style scoped>
.row {
  cursor: pointer;
  display: flex;
  flex-wrap: nowrap;
}

/* div p {
  text-align: left;
  display: inline-block;
} */

div.img img {
  position: relative;
  top: 17px;
  width: 25px;
  margin-right: 12px;
  height: 25px;
  fill: var(--primary);
}

.openableContent {
  max-height: 0;
  padding-bottom: 0px;
  transform-origin: top;
  overflow: hidden;
  padding-left: 15px;
  transition: max-height ease 0.8s;
}

.opened {
  max-height: 200px;
}

.title {
  margin-bottom: 5px;
}

.title {
  transition: all 0.2s ease-in-out;
}
.title:hover {
  color: var(--blue);
}

span {
  color: var(--secondary);
}

.title:hover span {
  color: var(--third);
}

@media only screen and (max-width: 800px) {
  .openableTitle,
  .openableContent {
    font-size: 10pt;
    width: 85%;
    text-align: left !important;
  }

  .cacheBlack {
    width: 10%;
  }

  .opened {
    max-height: 500px;
  }

  div.img img {
    top: 8px;
  }
}
</style>
