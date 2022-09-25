<script setup>
import { VueperSlides, VueperSlide } from 'vueperslides';
import 'vueperslides/dist/vueperslides.css'; 

const slides = [
  {
    title: 'Slide #1',
    content: 'Slide 1 content.'
  },
  {
    title: 'Slide #2',
    content: 'Slide 2 content.'
  }
]
</script>

<template>
  <vueper-slides :slide-ratio="1 / 3" fixed-height="60vh">
      <vueper-slide
        v-for="(slide, i) in slides"
        :key="i"
        :title="slide.title"
        :content="slide.content">
      </vueper-slide>
    </vueper-slides>
</template>

<style scoped>
</style>