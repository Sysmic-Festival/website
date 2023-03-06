<script setup>
</script>

<template>
    <div>
        <div class="portfolio">
            <br>
            <h1 class="large-title">Page en construction</h1>
        
            <h3>En attendant, nous vous invitons à consulter l'ancien portfolio 
                <a href="https://dev.sysmic.ch/portfolio.php" target="_BLANK"><span style="color:var(--third); text-decoration:underline">ici</span></a>
            </h3>
        </div>
    </div>

</template>

<style scoped>

.portfolio{
    margin: 10px;
    margin-top: calc(2*var(--global-margin) + var(--navbar-height));
}
.large-title {
  font-size: 90pt;
  font-weight: bold;
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

</style>