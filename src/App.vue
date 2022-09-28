<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Timer from './components/Timer.vue';
import Footer from './components/Footer.vue';
import Sidemenu from './components/Sidemenu.vue';
import Slideshow from './components/Slideshow.vue';
import AnimatedLogo from './components/AnimatedLogo.vue';


</script>

<template>
  <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet'>

  <div>
    <div class="home-screen">
      <AnimatedLogo/>
      <Timer/>
    </div>
    <NavBar />
   
    <div ref="line-up" class="line-up">
      <img class="img-responsive" src = "@/assets/images/utilitaries/placeholder-img.png" />
      <button class="main-page-button">Programmation complète →</button>
    </div>

    <div class="photo-gallery">
      <Slideshow />
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
      <section class="button-section">
        <a href="./faq.html">
          <button class="main-page-button">FAQ →</button>
        </a>
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
      <section class="button-section">
        <button class="main-page-button">Plan du Festival →</button>
      </section>
    </div>


    <div class="sponsors">
      <h1 class="h1-third-background">Nos Sponsors</h1>
      <section class="sponsors-line">
        <div>
          <a href="https://www.logitech.com/de-ch">
            <img src="@/assets/images/sponsors/logitech-logo.svg">
          </a >
        </div>
        <div style="display:block">
          <a href="https://fr.brio-mate.com/">
            <img src="@/assets/images/sponsors/Brio-H-blanc-logo.svg">
          </a>
        </div>
        <div>
          <a href="https://www.visilab.ch/fr/">
            <img src="@/assets/images/sponsors/Visilab-couleur-logo.png">
          </a>
        </div>
        <div>
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <img src="@/assets/images/sponsors/Rivella-logo.svg">
          </a>
        </div>
        <div>
          <a href="https://www.forum-epfl.ch/">
            <img src="@/assets/images/sponsors/Forum-epfl-logo.png">
          </a>
        </div>
        <div>
          <a href="https://fastree3d.com/">
            <img src="@/assets/images/sponsors/fastree3d-logo.png">
          </a>
        </div>
        <div id="sponsor-space-filler"></div>
        <div>
          <a href="https://www.l-dudu.ch/">
            <img src="@/assets/images/sponsors/L-DuDu-logo.png">
          </a>
        </div>
        </section>
    </div>


    <div class="association">
        <h1 class="h1-primary-background">Qui sommes-nous?</h1>
        <div class="container container-vertical-phone">
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
        <div class="container">
          <section>
            <p style="text-align: center;">Si tu veux en savoir plus à propos de l'association, jettes un oeil à la page <span><a href="./a-propos.html"> à propos </a></span> !</p>
          </section>
        </div>
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
              <h4>Matej Soumillon</h4>
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
            <div class="comite-member">
              <h4>Raphaël Charozé</h4>
              <p>Technique de scène</p>
            <img class="comite-img" src="@/assets/images/comite/charo.jpg">
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
            <div class="comite-member">
              <h4>Tifaine Mezencev</h4>
              <p>Escape Game</p>
              <img class="comite-img" src="@/assets/images/comite/Tifaine.jpg">
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

  .button-section{
    width: 100%; 
    padding-top: 25px;
    padding-bottom: 25px;
    padding-left: 0;
    padding-right: 0;
  }
  section {
    padding: 25px;
  }

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
    margin-top:25px;
    margin-bottom:25px;
  }

  #date-hr{
    margin-right: 25px;
    margin-left: 25px;
  }

  .comite-section-hr{
    max-width: 1000px;
    border: 1px solid var(--third) ;
  }

  span{
    color: var(--secondary);
  }

  .line-up{
    height: 100vh;
    max-width: 100%;
    padding: 20px;
    padding-top: calc(var(--navbar-height) + var(--global-margin));
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
    /* height: 60vh; */
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
    display: flex;
    flex-wrap: wrap;
    margin:auto;
    width: 66%;
    padding: 0;
  }

  .sponsors section div{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 33%;
    transition-duration: 0.4s;
  }

  .sponsors section img{
    transform: scale(0.95);
    width: 100%;
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
    display: inline-block;
    width: 100%;
  }

  .comite-member{
          display: inline-block;

    align-items: center;
    width: 25%;
  }

  .comite-member p{
    text-align: center;
    margin:0;
    display: flex;
    flex-direction: column;
  }

  .comite-img{
    width: 80%;
  }

  .home-screen{
    height: calc(100vh - var(--navbar-height) - var(--global-margin));;
    background-color: var(--primary);
    display: flex;
    flex-direction: column;
    padding-bottom: 20px; 
  }

  @media screen and (max-width: 850px) {

    .info-section-hr{
      max-width: 300px;
      border: 2px solid var(--third);
    }

    .main-page-button{
      width: 40%;
      height: 30px;
      font-weight: bold;
      font-size: 2.5vw; 
      color: var((--primary));
      background-color: var(--white);
      cursor: pointer;
      border-radius: 5px;
      border: 0;
    }

    .sponsors-line{
      width: 90% !important;
    }

    .sponsors section div{
      width: 49%;
    }

    #sponsor-space-filler{
      width: 25%;
    }

    .comite-line {
      width: 100% !important;
    }

    .comite-member{
      width: 49% !important;
    }

  }
</style>
