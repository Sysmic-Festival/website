<script setup>

</script>

<template>
  <div>
    <div class="apropos">

      <h1 class="large-title">Sysmic Festival</h1>

      <hr>

      <h1 class="h1-primary-background">Qui sommes-nous?</h1>
      <div class="container container-vertical-phone">
        <section style="flex:1">
          <p>
            Nous sommes un groupe composé d’une vingtaine d’étudiants motivés et dynamiques.
            <br><br>
            Nous appartenons à plusieurs sections différentes de l'EPFL et travaillons pour la section de
            Microtechnique.
          </p>
          <br>
          <p>
            Notre plus grande qualité se trouve dans notre détermination à faire de Sysmic l’un des meilleurs festivals
            estudiantins du campus.
            <br><br>
            Le comité Sysmic est cette année prêt à tout donner pour t’assurer la meilleure expérience possible !
          </p>
        </section>
        <section style="flex:1">
          <img src="@/assets/images/PhotoGallery/qui-sommes-nous-img.jpg" style="width: 100%;">
        </section>
      </div>

      <hr>

      <h1 class="h1-primary-background">Que faisons nous?</h1>
      <div class="container container-vertical-phone">
        <section style="flex:1; padding-right:0">
          <img src="@/assets/images/PhotoGallery/que-faisons-nous.jpg" style="height: 335px;">
        </section>
        <section>
          <p>
            Nous sommes un groupe composé d’une vingtaine d’étudiants motivés et dynamiques.
            <br><br>
            Nous appartenons à plusieurs sections différentes de l'EPFL et travaillons pour la section de
            Microtechnique.
          </p>
          <br>
          <p>
            Notre plus grande qualité se trouve dans notre détermination à faire de Sysmic l’un des meilleurs festivals
            estudiantins du campus.
            <br><br>
            Le comité Sysmic est cette année prêt à tout donner pour t’assurer la meilleure expérience possible !
          </p>
        </section>
      </div>

      <hr>

      <h1 class="h1-primary-background">Comment nous rejoindre?</h1>
      <div class="container container-vertical-phone" style="flex-direction: column">
        <section style="padding-bottom:0">
          <p>
            Nous sommes un groupe composé d’une vingtaine d’étudiants motivés et dynamiques.
            <br><br>
            Nous appartenons à plusieurs sections différentes de l'EPFL et travaillons pour la section de
            Microtechnique.
          </p>
          <br>
          <p>
            Notre plus grande qualité se trouve dans notre détermination à faire de Sysmic l’un des meilleurs festivals
            estudiantins du campus.
            <br><br>
            Le comité Sysmic est cette année prêt à tout donner pour t’assurer la meilleure expérience possible !
          </p>
        </section>
        <section style="flex:1; padding-top:0">
          <img src="@/assets/images/PhotoGallery/comment-nous-rejoindre.jpg" style="width: 100%; ">
        </section>

        <hr>

        <h1 class="h1-primary-background">Statuts</h1>
        <p>Si tu aimes la lecture, nos statuts sont disponibles <a href="@/assets/text/SYSMIC_Statuts_2022.pdf"
            style="text-decoration:underline">ici</a></p>

      </div>


    </div>
  </div>

</template>

<style scoped>
section {
  padding: 25px;
}

.apropos {
  margin: auto;
  margin-top: calc(2*var(--global-margin) + var(--navbar-height));
  display: inline-block;
}

.large-title {
  font-size: 90pt;
  color: var(--white);
}

.apropos hr {
  max-width: 800px;
  border: 1px solid var(--third);
}
</style>