<script setup>
</script>

<template>
    <div class="portfolio">
        <section>
            <div class="title-small-line"></div>
            <hr class="title-hr">
<h1>Année 2015</h1>
<img class="image_year" src="https://www.sysmic.ch/ressources/portfolio/year_images/2015.jpg">
            <hr class="title-hr">
            <div class="title-small-line"></div>
        </section>
        <div class="images_list">
          <section class="images_line">
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/004.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb004.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/004.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/006.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb006.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/006.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/007.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb007.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/007.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/009.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb009.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/009.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/012.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb012.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/012.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/014.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb014.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/014.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/015.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb015.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/015.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/017.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb017.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/017.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/018.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb018.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/018.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/019.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb019.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/019.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/020.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb020.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/020.jpg">
</a></div>
<div class="image">
<a href="https://www.sysmic.ch/ressources/portfolio/2015/021.jpg" class="thumbnail-link">
<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/2015/thumbnails/thumb021.jpg" data-src="https://www.sysmic.ch/ressources/portfolio/2015/021.jpg">
</a></div>
          </section>
        </div>
        <div id="modal">
            <img id="modal-image" src="" alt="Modal Image">
        </div>
    </div>
</template>

<style scoped>

#modal{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1;
  display: none;
}

#modal-image {
  max-width: 80%;
  max-height: 80%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.lazy {
  opacity: 0;
}

.loaded {
  opacity: 1;
  transition: opacity 0.3s;
}
.portfolio{
    margin: 10px;
    margin-top: calc(2*var(--global-margin) + var(--navbar-height));
}
.large-title {
  font-size: 90pt;
  font-weight: bold;
  color: var(--white);
}
.images_list{
    display: flex;
    max-width: 1400px;
    justify-content: space-evenly;
    margin: auto;
}

.images_line{
    padding: 10px;
    display: inline-block;
    width: 100%;
    align-items: center;
}

.image_image{
    width: 90%;
    height: 175px;
    padding: 5%;
    object-fit: cover;
}
.image{
  display: inline-block;
  align-items: center;
  width: 22%;
  margin: 0.5%;
  border-radius: 10px;
  cursor: pointer;
  border-bottom: 2px solid rgba(0, 0, 0, 0);
  border-top: 2px solid rgba(0, 0, 0, 0);
  border-left: 2px solid rgba(0, 0, 0, 0);
  border-right: 2px solid rgba(0, 0, 0, 0);
  transition: 0.5s ease-in-out;
}

.image_year{
  display: inline-block;
  align-items: center;
  width: 18%;
}

@media screen and (max-width: 850px) {
  .image{
    width: 29%;
    height: 125px; 
  }
  .image_image{
    height: 100px;
  }
  .image_year{
    width: 48%;
  }
}

@media screen and (max-width: 450px) {
  .image{
    width: 47%;
  }
}
.image:hover{
  border-radius: 10px;
  border-bottom: 2px solid var(--blue);
  border-top: 2px solid var(--blue);
  border-left: 2px solid var(--blue);
  border-right: 2px solid var(--blue);
  box-shadow: 0 0 30px 20px rgba(0,0,0,0.4);
  background-color: rgba(0,0,0,0.4);
}

.image h4{
  text-align: center;
  font-size: 30pt;
  color: var(--white);
}

@media only screen and (max-width: 850px) {

    .large-title{
      font-size: 40pt;
    }

    h1{
      font-size: 25pt;
    }

    .apropos hr{
      max-width: 300px;
    }

}

.title-hr {
  max-width: 200px;
}
.title-small-line{
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  width: 50%;
  max-width: 100px;
  border: 1px solid var(--blue);
}

section hr {
  max-width: 800px;
  border: 1px solid var(--third);
}

section div {
  flex-wrap: wrap;
  margin: auto;
  text-align: left;
}

h1 {
  color: var(--white);
  margin: 0;
  margin-top: 15px;
  margin-bottom: 15px;
  font-size: 40px;
}

</style>