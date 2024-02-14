<script setup>
</script>

<template>
    <div class="portfolio">
        <section>
            <div class="title-small-line"></div>
            <hr class="title-hr">
            <hr class="title-hr">
            <div class="title-small-line"></div>
        </section>
        <div class="images_list">
          <section class="images_line">
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