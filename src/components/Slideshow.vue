<script setup>
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

import slide1 from "@/assets/images/PhotoGallery/slideshooow1.jpeg";
import slide2 from "@/assets/images/PhotoGallery/slideshooow5.jpeg";
// import slide3 from "@/assets/images/PhotoGallery/slideshow/3.jpg"
import slide4 from "@/assets/images/PhotoGallery/slideshow/4.jpg";
import slide5 from "@/assets/images/PhotoGallery/slideshooow3.jpeg";
import slide6 from "@/assets/images/PhotoGallery/slideshooow4.jpeg";
import slide7 from "@/assets/images/PhotoGallery/slideshooow2.jpeg";
import slide8 from "@/assets/images/PhotoGallery/slideshooow6.jpg";

const slides = [slide1, slide2, slide5, slide6, slide7, slide8];
</script>

<template>
  <vueper-slides
    id="slider"
    :slide-ratio="1 / 1"
    fixed-height="60vh"
    lazy
    lazy-load-on-drag
    :touchable="false"
    autoplay
  >
    <vueper-slide v-for="(slide, i) in slides" :key="i" :image="slide">
    </vueper-slide>
  </vueper-slides>
</template>

<style scoped>
#slider {
  max-width: 1000px;
  margin: auto;
  margin-top: 43px;
}

@media screen and (max-width: 850px) {
  #slider {
    margin-top: 0;
  }
}
</style>
