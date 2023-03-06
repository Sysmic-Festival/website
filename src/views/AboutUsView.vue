<script setup>

</script>

<template>
  <div>
    <div class="apropos">

      <h1 class="large-title">Sysmic Festival</h1>

      <hr>

      <h1 class="h1-primary-background">Qui sommes-nous  ?</h1>
      <div class="container container-vertical-phone">
        <section style="flex:1 ; padding-bottom: 0;">
          <p style="margin-top:0">
                        Sysmic est constitué d’un comité de 25 personnes de toutes années et sections confondues. Nous travaillons tout au long de l’année afin d’offrir aux élèves de l’EPFL un festival de musique d’une soirée au sein même du campus.
                        <br><br>
                        Originellement l’association est dédiée à la section de Microtechnique, pour laquelle nous organisons en parallèle du festival chaque année un apéro suivi d’un repas et d’un Spectacle !
                    </p>
                    <br>
                    <p>
                        Notre plus grande qualité se trouve dans notre détermination à faire de Sysmic l’un des
                        meilleurs festivals estudiantins du campus.
                        <br><br>
                        Le comité Sysmic est cette année prêt à tout donner pour t’assurer la meilleure expérience
                        possible !
                    </p>
        </section>
        <section style="flex:1">
          <img src="@/assets/images/PhotoGallery/qui-sommes-nous-img.jpg" style="width: 105%;">
        </section>
      </div>

      <hr>

      <h1 class="h1-primary-background">Que faisons nous  ?</h1>
      <div class="container container-vertical-phone">
        <section style="flex:1; padding-top:0; padding-bottom:0">
          <img src="@/assets/images/PhotoGallery/que-faisons-nous.jpg" style="height: 275px;">
        </section>
        <section>
          <p style="margin-top: 0;">
            Sysmic est le dernier festival du premier semestre, et a lieu chaque année vers la fin octobre.
            Nous avons plusieurs scènes et bars, des stands de nourriture, mais nous sommes le seul festival du campus avec un Just Dance et des salles d’Escape Game !
            <br><br>
            Tu peux aussi nous retrouver lors d’autres évènements tout au long de l’année car nous tenons fréquemment des stands à Balélec, Vivapoly etc.. en 2022 nous avons même organisé un tremplin pour la première fois !
          </p>
          <br>

        </section>
      </div>

      <hr>

      <h1 class="h1-primary-background">Prévention</h1>
      <div class="container container-vertical-phone" style="flex-direction: column">
        <section style="padding-bottom:0 ; margin-top: 0;">
          <p style="margin:0;margin-bottom: 25px;">
            Nous cherchons continuellement à améliorer notre festival pour ses participant.es.            <br><br>
            Afin de s’assurer de leur bien-être en milieu festif nous avons décidé de prendre des mesures de prévention (sexualité, alcool, drogues) et adhérons désormais à la <a href="https://www.festiplus.ch/" target="_BLANK">Charte Festiplus</a>. Sera aussi présent sur notre site un stand de l’association Nightlife si tu as envie de discuter ou t’informer sur ces thématiques durant ta soirée !          </p>
        </section>
      </div>

      <hr>

      <h1 class="h1-primary-background" id="recrutement">Comment nous rejoindre  ?</h1>
      <div class="container container-vertical-phone" style="flex-direction: column">
        <section style="padding-bottom:0 ; margin-top: 0;">
          <p style="margin:0;margin-bottom: 25px;">
            Si tu veux nous aider à l’élaboration du Festival tu peux venir staffer chaque années pendant la semaine de montage du festival, et pendant la soirée! !
            <br><br>
            Si tu as envie de plus t’impliquer, chaque année après le festival a lieu notre Assemblée Générale où nous élisons le nouveau Comité de Direction. Cette année ce sera le dimanche 27 novembre à 18h, n’hésite pas à venir c’est ouvert à tous.te.s. Suite à ça le recrutement du comité est annoncé par mail et sur nos réseaux sociaux.
            <br><br>
            <!-- Le form de recrutement pour les posts à pourvoir est disponible <a href="/presentation posts.pdf" target="_blank" style="text-decoration: underline;">ici</a> ! -->
          </p>
        </section>
        <section style="flex:1; padding-top:0 ;padding-bottom: 0;">
          <img src="@/assets/images/PhotoGallery/comment-nous-rejoindre.jpg" style="width: 100%; ">
        </section>
      </div>

      <hr>
      
      <h1 class="h1-primary-background">Statuts</h1>
      <div class="container">
        <section style="padding-top: 0;">
          <p>Si tu aimes la lecture, nos statuts sont disponibles <a href="/text/SYSMIC_Statuts_2022.pdf" target="_blank"
          style="text-decoration:underline; color:var(--white)">ici</a></p>
        </section>

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
  margin-top: var(--global-margin);
  display: inline-block;
}

.large-title {
  font-size: 90pt;
  font-weight: bold;
  color: var(--white);
}

.apropos hr {
  max-width: 800px;
  border: 1px solid var(--third);
}

  @media only screen and (max-width: 850px) {

    .large-title{
      font-size: 60pt;
    }

    h1{
      font-size: 25pt;
    }

    .apropos hr{
      max-width: 300px;
    }

  }

</style>