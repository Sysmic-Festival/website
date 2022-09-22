<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Timer from './components/Timer.vue';
import Footer from './components/Footer.vue';
import Sidemenu from './components/Sidemenu.vue';
</script>

<template>

  <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Nunito" />
  <div>
    <div class = "home-screen">
      <Timer />
    </div>
    <NavBar />
   
    <div class="line-up">
      <img class="img-responsive" src = "@/assets/images/PhotoGallery/1.jpg" />
      <button class="main-page-button">Programmation complète →</button>
    </div>

    <div class="photo-gallery">

    </div>
    
    <div class="infos">
      <h1 class="h1-primary-background">Infos Pratiques</h1>
      <div class="container">
        <section style="flex: 2">
          <h2 class="h2-primary-background">Billeterie</h2>
          <p>
            Prélocation: 12CHF 
            <br>
            Vente du XX au XX octobre à l'Esplanade à 12H00 
            <br>
            Payement en Camipro ou en cash 
            <br>
            Le soir même: 15CHF
          </p>
        </section>
        <hr class = "info-section-hr" id="date-hr">
        <section style="flex: 1">
          <h2 class="h2-primary-background">Date</h2>
          <p>
            21 Octobre 2022 <br><br>
            Début: 19H45
            <br>
            Fin: 03H00
          </p>
        </section>
      </div>
      <br>
      <section>
        <button class="main-page-button">FAQ →</button>
      </section>     
      <hr class="info-section-hr">
      <div class="container-large">
        <section style="flex:1">
          <h2 class="h2-primary-background" id="plan-title">Accès</h2>
          <p id="plan-para">
            Le festival se déroule dans le batiment CE sur le site de L’EPFL  situé sur la commune d’Ecublens. Il est accessible en transports en commun par le métro M1 et se situe près de l’autoroute A1 (sortie EPFL-UNIL).
            Prenez le métro M1 jusqu’à l’arrêt EPFL ou UNIL SORGE.
          </p>
        </section>
        <section id="plan-image" style="flex:1">
          <img class="img-responsive" src="@/assets/images/plan-tempo.png">
        </section>
      </div>
      <section>
        <button class="main-page-button">Plan du Festival →</button>
      </section>
    </div>


    <div class="sponsors">
      <h1 class="h1-third-background">Nos Sponsors</h1>
      <section class="sponsors-line">
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/swisstech_village.svg">
          </a >
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/swisstech_village.svg">
          </a>
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/swisstech_village.svg">
          </a>
        </section>
      <section class="sponsors-line">
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/swisstech_village.svg">
          </a>
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/swisstech_village.svg">
          </a>
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/swisstech_village.svg">
          </a>
      </section>
    </div>


    <div class="association">
        <h1 class="h1-primary-background">Qui sommes-nous?</h1>
        <div class="container">
          <section style="flex:1">   
            <p>
              Nous sommes un groupe composé d’une vingtaine d’étudiants motivés et dynamiques.
              <br><br>
              Nous appartenons à plusieurs sections différentes de l'EPFL et travaillons pour la section de Microtechnique.
            </p>
            <br>
            <p>
              Notre plus grande qualité se trouve dans notre détermination à faire de Sysmic l’un des meilleurs festivals estudiantins du campus.
              <br><br>
              Le comité Sysmic est cette année prêt à tout donner pour t’assurer la meilleure expérience possible !
            </p>
          </section>
          <section style="flex:1">
            <img src="@/assets/images/PhotoGallery/qui-sommes-nous-img.jpg" style="width: 100%;">
          </section>
        </div>
        <p style="text-align: center;">Si tu veux en savoir plus à propos de l'association, jettes un oeil à la page <span><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"> à propos </a></span> !</p>

        <hr class="comite-section-hr">
        <h1 class="h1-primary-background comite-title">Le Comité</h1>

        <h2 class="h2-primary-background comite-title">Présidence</h2>
        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Anouk Paulino</h4>
              <p>Présidente</p>
              <img class="comite-img" src="@/assets/images/comite/anouk.jpg">
            </div>
          </section>
        </div>
        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Davia Trannoy</h4>
              <p>VP Communication</p>
              <img class="comite-img" src="@/assets/images/comite/absent.jpg">
            </div>
            <div class="comite-member">
              <h4>Ludovic Mareemootoo</h4>
              <p>VP Logistique</p>
              <img class="comite-img" src="@/assets/images/comite/absent.jpg">
            </div>
            <div class="comite-member">
              <h4>Nicolas Termote</h4>
              <p>VP Animation</p>
              <img class="comite-img" src="@/assets/images/comite/termote.jpg">
            </div>
            <div class="comite-member">
              <h4>Raphaël Pittet</h4>
              <p>Trésorier</p>
              <img class="comite-img" src="@/assets/images/comite/raph.jpg">
            </div>
          </section>
        </div>

        <hr class="comite-section-hr">
        <h2 class="h2-primary-background comite-title">Logistique</h2>

        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Amélie Senaud</h4>
              <p>Sécurité</p>
              <img class="comite-img" src="@/assets/images/comite/absent.jpg">
            </div>
            <div class="comite-member">
              <h4>Louis Le Guillouzic</h4>
              <p>Matériel</p>
              <img class="comite-img" src="@/assets/images/comite/louis.jpg">
            </div>
            <div class="comite-member">
              <h4>Ambroise Borbély</h4>
              <p>Élec/Light</p>
              <img class="comite-img" src="@/assets/images/comite/absent.jpg">
            </div>
            <div class="comite-member">
              <h4>Raphaël Charozé</h4>
              <p>Technique de scène</p>
              <img class="comite-img" src="@/assets/images/comite/charo.jpg">
            </div>
          </section>
        </div>

        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Flore Mueth</h4>
              <p>Décoration</p>
              <img class="comite-img" src="@/assets/images/comite/flore.jpg">
            </div>
            <div class="comite-member">
              <h4>Daphné Prenot</h4>
              <p>Décoration</p>
              <img class="comite-img" src="@/assets/images/comite/daphne.jpg">
            </div>
          </section>
        </div>

        <hr class="comite-section-hr">
        <h2 class="h2-primary-background comite-title">Communication</h2>

        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Lucile Moulin</h4>
              <p>RH</p>
              <img class="comite-img" src="@/assets/images/comite/lucile.jpg">
            </div>
            <div class="comite-member">
              <h4>Johanne Pinnel</h4>
              <p>Spectacle</p>
              <img class="comite-img" src="@/assets/images/comite/djo.jpg">
            </div>
            <div class="comite-member">
              <h4>Maxime Teuber</h4>
              <p>IT/Webmaster</p>
              <img class="comite-img" src="@/assets/images/comite/max.jpg">
            </div>
            <div class="comite-member">
              <h4>Daoud Hakim</h4>
              <p>Graphisme</p>
              <img class="comite-img" src="@/assets/images/comite/daoud.jpg">
            </div>
          </section>
        </div>

        <hr class="comite-section-hr">
        <h2 class="h2-primary-background comite-title">Animation</h2>

        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Matthieu Tonneau</h4>
              <p>Bar</p>
              <img class="comite-img" src="@/assets/images/comite/matthieu.jpg">
            </div>
            <div class="comite-member">
              <h4>Manon Landrieux</h4>
              <p>Bar</p>
              <img class="comite-img" src="@/assets/images/comite/manon.jpg">
            </div>
            <div class="comite-member">
              <h4>Thomas Cirillo</h4>
              <p>Programmation/Loges</p>
              <img class="comite-img" src="@/assets/images/comite/thomas-c.jpg">
            </div>
            <div class="comite-member">
              <h4>Elena Thomas</h4>
              <p>Programmation/Loges</p>
              <img class="comite-img" src="@/assets/images/comite/elena.jpg">
            </div>
          </section>
        </div>

        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Thomas Artru</h4>
              <p>Catering</p>
              <img class="comite-img" src="@/assets/images/comite/thomas-a.jpg">
            </div>
            <div class="comite-member">
              <h4>Aude-Line Fleury</h4>
              <p>Escape Game</p>
              <img class="comite-img" src="@/assets/images/comite/absent.jpg">
            </div>
          </section>
        </div>

        <hr class="comite-section-hr">
        <h2 class="h2-primary-background comite-title">Aide à la Trésorerie</h2>

        <div class="container-comite">
          <section class="comite-line">
            <div class="comite-member">
              <h4>Amandine Nicolle</h4>
              <p>Sponsoring</p>
              <img class="comite-img" src="@/assets/images/comite/amandine.jpg">
            </div>
            <div class="comite-member">
              <h4>Sébastien Dévaud</h4>
              <p>Sponsoring</p>
              <img class="comite-img" src="@/assets/images/comite/seby.jpg">
            </div>
          </section>
        </div>

    </div>

    <Footer></Footer>

  </div>
      

      <!-- <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav> -->
  <!-- <RouterView /> -->
</template>

<style scoped>



  h1, h2, h3{
    font-weight: 800;
  }
  
  #plan-title{
    text-align: center;
  }

  #plan-para{
    height: 100%;
  }

  .comite-title{
    text-align: center;
    margin-bottom: 0;
  }

  #plan-image{
    padding-right: 0;
    padding-left: 0;
    padding-bottom: 0;
    text-align: center;
    margin: auto;
  }

  .main-page-button{
    width: 20%;
    height: 50px;
    font-weight: bold;
    font-size: 1.5vw;
    color: var((--primary));
    background-color: var(--white);
    cursor:pointer;
    border-radius: 10px;
    border: 0;
  }


  .info-section-hr{
    border: 4px solid var(--third) ;
    border-radius: 50px;
    max-width: 1300px;
  }

  .comite-section-hr{
    max-width: 1000px;
    border: 1px solid var(--third) ;
  }

  span{
    color: var(--secondary);
  }

  .container{
    display: flex;
    max-width: 800px;
    margin: auto;
  }

  .container-large{
    display: flex;
    max-width: 1200px;
    margin: auto;
  }

  @media screen and (max-width: 1200px){
    .container-large{
      display: block;
      max-width: 1200px;
      margin: auto;
    }

    .container-large *{
      padding: 0;
      display:inline-block;
      text-align: center;
      max-width: 800px;
    }
  }

  .line-up{
    height: 100vh;
    width: 100%;
    padding: 20px;
    align-items: center;
    justify-content: space-between;
    display: flex;
    flex-direction: column;
    background-color: var(--secondary);
  }

  .line-up img{
    height: 85vh;
    margin-left: auto;
    margin-right: auto;
  }

  .photo-gallery{
    height: 60vh;
    background-color: var(--third);
  }

  .infos{
    display:block;
    width: 100%;
    background-color: var(--primary);
  }

  .infos section{
    display: inline-block;
    margin: 0;
  }

  .sponsors{
    display: inline-block;
    width: 100%;
    background-color: var(--third);
  }

  .sponsors .sponsors-line{
    width: 66%;
    padding: 0;
  }

  .sponsors section img{
    width: 33%;
    transition-duration: 0.4s;
  }

  .sponsors section img:hover{
    opacity: 0.80;
  }

  .association{
    display: inline-block;
    width: 100%;
    background-color: var(--primary);
  }

  
  .container-comite{
    display: flex;
    max-width: 1100px;
    margin: auto;
  }
  
  .comite-line{
    padding: 10px;
    display: flex;
    justify-content: center;
  }

  .comite-member{
    align-items: center;
    width: 25%;
  }

  .comite-member p{
    text-align: center;
    margin:0;
  }

  .comite-img{
    width: 80%;
  }

  .home-screen{
    display: flex;
    height: 100vh;
    background-color: var(--primary)
  }


  @media screen and (min-width: 1600px){
    .container{
      margin:auto;
      max-width: 80%;
      width:80vw;
    }  
  }

</style>
