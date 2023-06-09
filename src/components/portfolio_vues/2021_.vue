<script setup>
</script>

<template>
    <div class="portfolio">
        <section>
            <div class="title-small-line"></div>
            <hr class="title-hr">
            <h1>Année 2021</h1>
            <hr class="title-hr">
            <div class="title-small-line"></div>
        </section>
    </div>
</template>

<style scoped>

.portfolio{
    margin: 10px;
    margin-top: calc(2*var(--global-margin) + var(--navbar-height));
}

h1 {
  color: var(--white);
  margin: 0;
}

section hr {
  max-width: 800px;
  border: 1px solid var(--blue);
}

section div {
  flex-wrap: wrap;
  margin: auto;
  text-align: left;
}

section div p {
  text-align: left;
  display: inline-block;
}

section div img {
  position: relative;
  top: 17px;
  width: 25px;
  margin-right: 12px;
  height: 25px;
  fill: var(--primary);
}

.title-small-line{
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  width: 50%;
  max-width: 100px;
  border: 1px solid var(--third);
}

.title-hr {
  max-width: 200px;
}

</style>