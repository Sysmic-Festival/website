<script setup>
import NavBar from "../components/NavBar.vue";
import Timer from "../components/Timer.vue";
import Slideshow from "../components/Slideshow.vue";
import AnimatedLogo from "../components/AnimatedLogo.vue";
import FAQRow from "../components/FAQRow.vue";
</script>

<template>
  <div>
    <div class="home-screen">
      <div class="home-screen-bg"></div>
      <AnimatedLogo id="Logo" />
      <!-- <div class="sponsors-bar">
                <div class="sponsors-row">
                    <div class="sponsor-el">
                        <a href="https://www.makita.fr/">
                            <img src="@/assets/images/sponsors/makita.jpg">
                        </a>
                    </div>
                    <div class="sponsor-el" id="agep">
                        <a href="https://agepoly.ch/en/">
                            <img src="@/assets/images/sponsors/AGEPoly.svg">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a target="_BLANK" href="https://www.enzo-location.ch/">
                            <img src="@/assets/images/sponsors/enzoloc.jpg">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a target="_BLANK" href="https://www.ypsomed.com/en/">
                            <img src="@/assets/images/sponsors/ypsomed.png">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a target="_BLANK" href="https://www.walo.ch/fr-ch/home">
                            <img style="transform: scale(0.6);" src="@/assets/images/sponsors/walo.jpg">
                        </a>
                    </div>
                </div>
            </div> -->
      <!-- <Timer /> -->
    </div>
    <div id="coming-soon" class="coming-soon">
      <h1 class="h1-primary-background"><br />Coming soon</h1>
      <div id="infos-container" class="container">
        <section>
          <h2 class="h2-primary-background">Tremplin 2025</h2>
          <p>
            On se réjouit de te revoir cette année encore ! Pour bien débuter le
            semestre, Sysmic te propose de te retrouver au Tremplin.
            <br /><br />
            Le tremplin, c'est notre évènement de rentrée que nous organisons
            chaque année depuis 2022. Il s'agît en fait d'une soirée organisée
            en partenariat avec le bar Satellite.
            <br /><br />
            Tu peux venir assister aux shows d'artistes de la région, qui
            n'attendent que toi pour te démontrer leur talent, et ensuite voter
            pour l'artiste que tu préfères.
            <br /><br />
            L'artiste que le public plébiscite gagnera ensuite un slot sur scène
            lors de notre festival en novembre !
            <br /><br />
            On se réjouit donc de te voir le mercredi
            <b>24 septembre à 20:00 au Bar Satellite</b> (entrée libre).
          </p>
          <h2 class="h2-primary-background">Festival</h2>
          <p>
            Et il y aura biensur le festival le 7 novembre prochain !
            <br /><br />
            Les infos arriveront prochainement, alors n'oublie pas de nous
            suivre sur les reseaux pour être au courant ! On est sur
            <a href="https://instagram.com/festival_sysmic">Instagram</a>
          </p>
        </section>
      </div>

      <div class="slider">
        <div class="slide">
          <img class="band" src="@/assets/images/utilitaries/long-band.svg" />
        </div>
      </div>
    </div>
    <!-- <div id="magsys" class="magsys">
            <h1 class="h1-primary-background"><br>MSYS 2025</h1>
            <div id="infos-container" class="container">
                <section style="">
                    <h2 class="h2-primary-background">Billetterie </h2>
                    <p  >
                        Achat sur la billetterie en ligne : <span class="higlight-text">CHF 9</span>
                        <br><br>
                        Vente sur place le soir même : <span class="higlight-text">CHF 15</span>
                        <br><br>
                        Ouverture de la billetterie en ligne : <span class= "higlight-text"> 31 mars 2025</span> à <span class="higlight-text">12:00</span>.
                        <br><br>
                        Paiement en carte de crédit/débit ou Twint.
                    </p>
                    <div class="billetterie-button">
                        <button class="main-page-button" onclick="window.location.href = 'https://infomaniak.events/fr-ch/shop/sysmic-G7BDEEVBZ4';" >ACHETER UN BILLET</button>
                    </div>
                </section>
                <hr class="info-section-hr" id="date-hr">
                <section style="">
                    <h2 class="h2-primary-background">Date</h2>
                    <p>
                        <span class="higlight-text">8 avril 2025</span>
                         <br><br>
                        Horaires : <span class="higlight-text">22:30 - 5:00</span>
                        <br><br>
                        Lieu : <span class="higlight-text">D! Club</span> <br>Place centrale 1<br>1001 Lausanne
                    </p>
                </section>
            </div>

            <div class="slider">
                <div class="slide">
                    <img class="band" src="@/assets/images/utilitaries/long-band.svg">
                </div>
            </div>
        </div> -->
    <div id="line-up" class="line-up">
      <h1 class="h1-third-background" id="line-up-title">Line-up</h1>
      <div class="line-up-zone">
        <div class="line-up-container">
          <h2 class="line-up-stagename">AquaBass</h2>
          <div class="line-up-box-1" id="jardin">
            <div class="line-up-artist">
              <div class="line-up-time">08:30</div>
              <div class="line-up-name">HowsMax</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">08:30</div>
              <div class="line-up-name">Kodaman</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">08:30</div>
              <div class="line-up-name">Ahöra</div>
            </div>
          </div>
          <h2 class="line-up-stagename">Bikini Bottom</h2>
          <div class="line-up-box-1" id="wonder">
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Femme fatale</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">FAUSTINE</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Hypsign</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Blaame</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Quentin Austin</div>
            </div>
          </div>
          <h2 class="line-up-stagename">La fosse des Mariannes</h2>
          <div class="line-up-box-1" id="wonder">
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Femme fatale</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">FAUSTINE</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Hypsign</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Blaame</div>
            </div>
            <div class="line-up-artist">
              <div class="line-up-time">87:30</div>
              <div class="line-up-name">Quentin Austin</div>
            </div>
          </div>
        </div>
      </div>

      <section class="button-section">
        <a
          class="main-page-button"
          href="https://spotify.link/CEAKTpWMDXb"
          target="_blank"
        >
          Playlist du Festival →
        </a>
      </section>
    </div>

    <div class="photo-gallery">
      <Slideshow />
    </div>

    <!-- <div id="infos" class="infos">
            <h1 class="h1-primary-background">Infos Pratiques 2024</h1>
            <div id="infos-container" class="container">
                <section style="">
                    <h2 class="h2-primary-background">Billeterie</h2>
                    <p  >
                        Billet: <span class="higlight-text">15CHF</span>
                        <br><br>
                        Vente du <span class="higlight-text">29 au 30 octobre</span> sur l'Esplanade à <span class="higlight-text">12H00</span>
                        <br>
                        Paiement en Camipro ou en cash
                        <br><br>
                        Le soir même: <span class="higlight-text">20CHF</span>
                    </p>
                </section>
                <hr class="info-section-hr" id="date-hr">
                <section style="">
                    <h2 class="h2-primary-background">Date</h2>
                    <p>
                        <span class="higlight-text">1 novembre 2024</span>
                         <br><br>
                        Début: <span class="higlight-text">20h</span>
                        <br>
                        Début des concerts: <span class="higlight-text">20h30</span>
                        <br>
                        Fin: <span class="higlight-text">03H00</span>
                    </p>
                </section>
            </div>
            <hr class="mt-hr" style="max-width:150px">
            <hr class="mt-hr" style="max-width:200px">
            <hr class="mt-hr-blue">
            <div class=" container" style="flex-direction:column;align-items: center;font-weight: 900;"><p>Plus d'infos sur la partie <span style="color:var(--third)">MT</span> <RouterLink to="/faq#micros" style="color:var(--white); text-decoration: underline;">ici</RouterLink> !</p></div>
            <hr class="mt-hr-blue">
            <hr class="mt-hr" style="max-width:200px">
            <hr class="mt-hr" style="max-width:150px">
            <br>
            <section style="display:flex; flex-direction:column;align-items:center">
                
        <FAQRow title="Y a-t-il un vestiaire ?">
            Oui ! Un vestiaire est disponible gratuitement, cependant nous déclinons toute responsabilité en cas de perte ou vol.
        </FAQRow>

        <FAQRow title="Existe-il des navettes pour le retour ?">
            Oui ! En plus des transports en commun normaux, il y aura des navettes gratuites.
            Elles partiront à 01:30, 02:30 et 03:15 de l'arrêt Piccard (directement à la sortie du festival).<br>
            <br>
            Les navettes desserviront :<br>
            Renens, Malley, le Flon.
        </FAQRow>
        
        <FAQRow title="Les sacs sont-ils autorisés ?">
            Non ! Malheureusement, pour des raisons de sécurité, nous n'acceptons pas les sacs dans l’enceinte de la manifestation.
            Nous vous prions de venir sans sac à dos.
        </FAQRow>

        <FAQRow title="Comment puis-je obtenir un Ticket?">
            Les tickets seront mis en vente sur l'esplanade de l’EPFL durant la semaine précédant le festival, à 12:00, le mardi et mercredi.
        </FAQRow>
            </section>
            <section class="button-section">
                <router-link to="/faq">
                    <button class="main-page-button">FAQ →</button>
                </router-link>
            </section>
            <hr class="comite-section-hr">
            <div class="slider">
                <div class="slide">
                    <img class="band" src="@/assets/images/utilitaries/long-band.svg">
                </div>
            </div>
            <div class="container-large" style="margin-bottom:25px">
                <section style="flex:1">
                    <h2 class="h2-primary-background" id="plan-title">Accès</h2>
                    <p id="plan-para">
                        Le festival a lieu dans le batiment CE à L’EPFL dans la commune d’Ecublens. 
                        Il est accessible en transports en commun par le métro M1 (arrêt EPFL ou UNIL SORGE), le bus 701,31,705 (arrêt Argand, Paqueret ou Piccard) 
                        et se situe près de l’autoroute A1 (sortie EPFL-UNIL).

                    </p>
                </section>
                <section id="plan-image" style="flex:1">
                    <a href="https://www.google.com/maps/d/u/0/edit?mid=1CXFmGv1zlrAQgA84q9ZXzxnXD0qu938&usp=sharing" target="_blank">
                        <img class="img-responsive" src="@/assets/images/utilitaries/plan_acces.png">
                    </a>
                </section>
            </div>
            <section class="button-section">
                <a class="main-page-button" href="/images/plan_interieur.png" target="_blank">Plan du Festival →</a>
            </section>
        </div> -->

    <!-- <div id="sponsors" class="sponsors">
            <h1 class="h1-third-background">Sponsors 2024</h1>
            <section class="sponsors-line">
                <div>
                    <a target="_BLANK" href="https://infomaniak.events/fr-ch">
                        <img src="@/assets/images/sponsors/infomaniak-sa.png">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.walo.ch/fr-ch/home">
                        <img style="transform: scale(0.6);" src="@/assets/images/sponsors/walo.jpg">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.enzo-location.ch/">
                        <img style="transform: scale(0.6);" src="@/assets/images/sponsors/enzoloc.jpg">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.makita.fr/">
                        <img id="makita" style="transform: scale(0.6);" src="@/assets/images/sponsors/makita.jpg">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.ypsomed.com/en/">
                        <img style="transform: scale(1.4);" src="@/assets/images/sponsors/ypsomed.png">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://agepoly.ch/">
                        <img id="agepo" src="@/assets/images/sponsors/AGEPoly.svg">
                    </a>
                </div>
            </section>
        <section class="button-section" >
            <a href="https://sysmic.ch/dossier_sponso_sysmic_2024" target="_blank">
                <button class="main-page-button">Dossier Sponsoring →</button>
            </a>
        </section>
        </div> -->

    <!-- <div id="recrutement">
            <hr class="mt-hr" style="max-width:250px">
            <hr class="mt-hr" style="max-width:350px">
            <hr class="mt-hr" style="max-width:450px">
                <div class="" style="font-weight: 900;"><p style="text-align: center;">Vous cherchez à faire partie des <span style="color:var(--third)">Sponsors 2023</span> ? Cela se passe <a href="https://sysmic.ch/dossier_sponsoring_2023_FR.pdf" target="_blank" style="text-decoration: underline;color:var(--third);">ici</a> !</p></div>
            <hr class="mt-hr" style="max-width:450px">
            <hr class="mt-hr" style="max-width:350px">
            <hr class="mt-hr" style="max-width:250px">
            <br>
        </div> -->

    <div id="association" class="association">
      <h1 class="h1-primary-background">Qui sommes-nous ?</h1>
      <div class="container container-vertical-phone">
        <section style="flex: 3; padding-top: 0">
          <p>
            Sysmic est constitué d’un comité de 30 personnes de toutes années et
            sections confondues. Nous travaillons tout au long de l’année afin
            d’offrir aux élèves de l’EPFL un festival de musique d’une soirée au
            sein même du campus.
            <br /><br />
            Originellement, l’association est dédiée à la section de
            Microtechnique pour laquelle nous organisons, en parallèle du
            festival, un apéro suivi d’un repas et un Spectacle !
            <br /><br />
            Notre plus grande qualité se trouve dans notre détermination à faire
            de Sysmic l’un des meilleurs festivals estudiantins du campus.
            <br /><br />
            Le comité Sysmic est cette année prêt à tout donner pour t’assurer
            la meilleure expérience possible !
          </p>
        </section>
        <section id="qsn-img" style="flex: 2">
          <img
            src="@/assets/images/PhotoGallery/qui-sommes-nous-img.jpg"
            style="width: 105%"
          />
        </section>
      </div>
      <div class="container">
        <section>
          <p style="text-align: center">
            Si tu veux en savoir plus à propos de l'association, jette un oeil à
            la page
            <span
              ><router-link
                style="color: var(--white); text-decoration: underline"
                to="/about-us"
                >À propos</router-link
              ></span
            >
            !
          </p>
        </section>
      </div>
      <!-- <hr class="comite-section-hr"> -->
      <div class="slider">
        <div class="reverse-slide">
          <img class="band" src="@/assets/images/utilitaries/long-band.svg" />
        </div>
      </div>
    </div>
    <div id="comite" class="comite">
      <h1 class="h1-primary-background comite-title">Comité 2025</h1>
      <h2 class="h2-primary-background comite-title">Présidence</h2>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Mathieu Bénard</h4>
            <p>Président</p>
            <img class="comite-img" src="@/assets/images/comite/matthieu.jpg" />
          </div>
        </section>
      </div>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Roman Paccaud</h4>
            <p>VP Logistique</p>
            <img class="comite-img" src="@/assets/images/comite/roman_2.jpg" />
          </div>
          <div class="comite-member">
            <h4>Talia Meyer</h4>
            <p>VP Communication</p>
            <img class="comite-img" src="@/assets/images/comite/talia.jpg" />
          </div>
          <div class="comite-member">
            <h4>Salomé Grouzinoff</h4>
            <p>VP Animation</p>
            <img class="comite-img" src="@/assets/images/comite/salome.jpg" />
          </div>
          <div class="comite-member">
            <h4>Hector Mir</h4>
            <p>Trésorier</p>
            <img
              class="comite-img"
              src="@/assets/images/comite/hector_old.jpg"
            />
          </div>
        </section>
      </div>

      <hr class="comite-section-hr" />
      <h2 class="h2-primary-background comite-title">Logistique</h2>

      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Antoine Eisinger</h4>
            <p>Matériel</p>
            <img
              class="comite-img"
              src="@/assets/images/comite/antoine_matos.jpg"
            />
          </div>
          <div class="comite-member">
            <h4>Sophie Beuret</h4>
            <p>Sécurité</p>
            <img class="comite-img" src="@/assets/images/comite/sophie.jpg" />
          </div>
          <div class="comite-member">
            <h4>Matej Soumillion</h4>
            <p>Sécurité</p>
            <img class="comite-img" src="@/assets/images/comite/absent.png" />
          </div>
        </section>
      </div>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Roman Ostrowsky</h4>
            <p>Élec/Light</p>
            <img
              class="comite-img"
              src="@/assets/images/comite/roman_autre.jpg"
            />
          </div>
          <div class="comite-member">
            <h4>Maria Kyramarios</h4>
            <p>Décoration</p>
            <img class="comite-img" src="@/assets/images/comite/maria.jpg" />
          </div>
          <div class="comite-member">
            <h4>May Dubuy</h4>
            <p>Décoration</p>
            <img class="comite-img" src="@/assets/images/comite/may.jpg" />
          </div>
        </section>
      </div>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Jonas Blanc</h4>
            <p>Adjoint à la technique de scène</p>
            <img class="comite-img" src="@/assets/images/comite/absent.png" />
          </div>
          <div class="comite-member">
            <h4>Hadrien Canches</h4>
            <p>Technique de scène</p>
            <img class="comite-img" src="@/assets/images/comite/hadrien.jpg" />
          </div>
          <div class="comite-member">
            <h4>Maxime Coeytaux</h4>
            <p>RH</p>
            <img class="comite-img" src="@/assets/images/comite/maxime.jpg" />
          </div>
        </section>
      </div>

      <hr class="comite-section-hr" />
      <h2 class="h2-primary-background comite-title">Communication</h2>

      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Noam Lévy</h4>
            <p>Community Manager</p>
            <img class="comite-img" src="@/assets/images/comite/noam.jpg" />
          </div>
          <div class="comite-member">
            <h4>Romain Klein</h4>
            <p>Vidéaste</p>
            <img class="comite-img" src="@/assets/images/comite/romain.jpg" />
          </div>
          <div class="comite-member">
            <h4>Léa Mahfouf</h4>
            <p>Graphisme</p>
            <img class="comite-img" src="@/assets/images/comite/absent.png" />
          </div>
        </section>
      </div>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Daniel Krief</h4>
            <p>IT/Webmaster</p>
            <img class="comite-img" src="@/assets/images/comite/daniel.jpg" />
          </div>
          <div class="comite-member">
            <h4>Ulysse Zbinden</h4>
            <p>Prévention/Durabilité</p>
            <img class="comite-img" src="@/assets/images/comite/ulysse.jpg" />
          </div>
          <div class="comite-member">
            <h4>Mélodie Serreau</h4>
            <p>Spectacle</p>
            <img class="comite-img" src="@/assets/images/comite/melodie.jpg" />
          </div>
        </section>
      </div>

      <hr class="comite-section-hr" />
      <h2 class="h2-primary-background comite-title">Animation</h2>

      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Grégoire Gimenez</h4>
            <p>Bar</p>
            <img class="comite-img" src="@/assets/images/comite/gregoire.jpg" />
          </div>
          <div class="comite-member">
            <h4>Alexis Zuber</h4>
            <p>Bar</p>
            <img class="comite-img" src="@/assets/images/comite/alexis.jpg" />
          </div>
          <div class="comite-member">
            <h4>Olivia Robles</h4>
            <p>Programmation</p>
            <img class="comite-img" src="@/assets/images/comite/olivia.jpg" />
          </div>
          <div class="comite-member">
            <h4>Marc Simon</h4>
            <p>Programmation</p>
            <img class="comite-img" src="@/assets/images/comite/marc.jpg" />
          </div>

          <div class="comite-member">
            <h4>Dina Azoulay</h4>
            <p>Catering</p>
            <img class="comite-img" src="@/assets/images/comite/dina.jpg" />
          </div>
          <div class="comite-member">
            <h4>Antoine Reynaud</h4>
            <p>Catering</p>
            <img
              class="comite-img"
              src="@/assets/images/comite/antoine_cat.jpg"
            />
          </div>
          <div class="comite-member">
            <h4>Marie van Rossum</h4>
            <p>Escape Game</p>
            <img class="comite-img" src="@/assets/images/comite/marie.jpg" />
          </div>
          <div class="comite-member">
            <h4>Anouck Fazio</h4>
            <p>Escape Game</p>
            <img class="comite-img" src="@/assets/images/comite/anouck.jpg" />
          </div>
        </section>
      </div>

      <hr class="comite-section-hr" />
      <h2 class="h2-primary-background comite-title">Aide à la Trésorerie</h2>

      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Felix Elsässer</h4>
            <p>Sponsoring</p>
            <img class="comite-img" src="@/assets/images/comite/felix.jpg" />
          </div>
          <div class="comite-member">
            <h4>Marina Perez Barrera</h4>
            <p>Sponsoring</p>
            <img class="comite-img" src="@/assets/images/comite/marina.jpg" />
          </div>
        </section>
      </div>

      <!-- <hr class="comite-section-hr"> -->
      <!-- <h2 class="h2-primary-background comite-title">Membres de soutien</h2> -->

      <!-- <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Paloma Garcia Moron</h4>
                        <p>Membre de Soutien</p>
                        <img class="comite-img" src="@/assets/images/comite/paloma.jpg">
                    </div>
                    <div class="comite-member">
                        <h4>Raphaël Pittet</h4>
                        <p>Membre de Soutien</p>
                        <img class="comite-img" src="@/assets/images/comite/raphael.jpg">
                    </div>  
                    <div class="comite-member">
                        <h4>Eleonore Salin</h4>
                        <p>Membre de Soutien</p>
                        <img class="comite-img" src="@/assets/images/comite/eleonore.jpg">
                    </div> 
                    <div class="comite-member">
                        <h4>Sébastien Devaud</h4>
                        <p>Membre de Soutien</p>
                        <img class="comite-img" src="@/assets/images/comite/seby.png">
                    </div> 
                </section>
            </div> -->
    </div>
  </div>
</template>

<style scoped>
.button-section {
  width: 100%;
  padding-left: 0;
  padding-right: 0;
}

section {
  padding: 25px;
}

h1,
h2,
h3 {
  font-weight: 800;
}

#plan-title {
  text-align: center;
}

#plan-para {
  height: 100%;
  margin-right: 50px;
}

.comite-title {
  text-align: center;
  margin-bottom: 0;
}

#plan-image {
  padding-right: 0;
  padding-left: 0;
  padding-bottom: 0;
  text-align: center;
  margin: auto;
}

.main-page-button {
  margin: 10px;
  padding: 15px;
  font-weight: bold;
  color: var(--primary);
  background-color: var(--white);
  cursor: pointer;
  border-radius: 10px;
  border: 0;
}

.info-section-hr {
  border: 1px solid var(--blue);
  border-radius: 50px;
  max-width: 1300px;
  margin-top: 25px;
  margin-bottom: 25px;
}

#date-hr {
  margin-right: 25px;
  margin-left: 25px;
}

.comite-section-hr {
  max-width: 1000px;
  border: 1px solid var(--blue);
}

span {
  color: var(--secondary);
}

#recrutement {
  max-width: 100%;
  padding: var(--global-margin);
  padding-top: calc(var(--navbar-height) + var(--global-margin));
  padding-bottom: 0;
  align-items: center;
  justify-content: space-around;
  background-color: var(--secondary);
  box-shadow: 0 8px 30px -4px black;
}

.line-up {
  max-width: 100%;
  padding: 20px;
  padding-top: calc(var(--navbar-height) + var(--global-margin));
  align-items: center;
  justify-content: space-around;
  display: flex;
  flex-direction: column;
  background-color: var(--secondary);

  box-shadow: 0 8px 30px -4px black;
}

.line-up img {
  width: 1000px;
  margin-left: auto;
  margin-right: auto;
}

.line-up-zone {
  width: 150%;
  max-width: 1000px;
  height: 750px;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: row;
  margin-bottom: 50px;
  justify-content: center;
}

.line-up-container {
  width: 50%;
  min-width: 250px;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-left: 20px;
  padding-right: 20px;
  margin-bottom: 40px;
}

.line-up-box-1 {
  height: 100%;
  width: 100%;
  border-radius: 20px;
  background-color: var(--primary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  border: solid 2px var(--blue);
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.5);
  /* margin-bottom: 25px; */
}

.line-up-box-2 {
  height: 100%;
  width: 100%;
  border-radius: 20px;
  background-color: var(--primary);
  border: solid 2px var(--blue);
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.5);
  display: flex-wrap;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  padding: 8px;

  /* margin-bottom: 5px; */
}

.line-up-stagename {
  color: white;
  text-align: center;
  font-size: 1.65em;
}
.line-up-artist-big {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.line-up-artist {
  display: inline-block;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  width: 90%;
}

#loudjack {
  position: relative;
  height: 90px;
  top: -33px;
}

#jardin,
#jardin2 {
  height: 60%;
}

.line-up-time {
  background-color: var(--third);
  color: var(--white);
  font-family: "Roboto";
  font-size: 1.7em;
  font-weight: bold;
  border-radius: 10px;
  height: 45px;
  width: 100px;
  display: flex;
  margin: auto;
  align-items: center;
  justify-content: space-evenly;
}
.line-up-artist-big .line-up-time {
  background-color: var(--third);
  color: var(--white);
  font-family: "Roboto";
  font-size: 1.7em;
  font-weight: bold;
  border-radius: 10px;
  height: 55px;
  width: 150px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

.line-up-name {
  font-family: "Roboto";
  font-size: 1.7em;
  font-weight: 800;
  color: grey;
  margin-top: 10px;
}
.line-up-artist-big .line-up-name {
  font-family: "Roboto";
  font-size: 1.7em;
  font-weight: 800;
  color: grey;
  margin-top: 15px;
}

@media screen and (max-width: 1180px) {
  .line-up-stagename {
    font-size: 1.5em;
  }
}

/* .band{
    max-height: 5px;
    width: 100%;
    display:none;
} */

/* .slider {
  width: 100%;
  overflow: hidden;
} */

.slide {
  width: 200%;
  height: auto;
  background-size: contain;
  background-repeat: repeat-x;
  animation: slide 20s linear infinite;
  /* background-color: rgba(0,0,0,0.2);
    box-shadow: 0 -2px 10px 5px rgba(0, 0, 0, 0.2); */
  margin-top: 20px;
  margin-bottom: 20px;
}
.reverse-slide {
  width: 200%;
  height: auto;
  background-size: contain;
  background-repeat: repeat-x;
  animation: reverse-slide 20s linear infinite;
  /* background-color: rgba(0,0,0,0.2); */
  /* box-shadow: 0 -2px 10px 5px rgba(0, 0, 0, 0.2); */
  margin-top: 20px;
  margin-bottom: 20px;
}

@keyframes slide {
  0% {
    transform: translateX(-50%);
  }
  100% {
    transform: translateX(
      0%
    ); /* Adjust the percentage based on the width of your image */
  }
}

@keyframes reverse-slide {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(
      -50%
    ); /* Adjust the percentage based on the width of your image */
  }
}

.photo-gallery {
  /* height: 60vh; */
  background-color: var(--primary);
}

.infos {
  margin-bottom: 25px;
  display: block;
  width: 100%;
  background-color: var(--primary);
}

.infos section {
  display: inline-block;
  margin: 0;
}

.mt-hr {
  border: 1px solid var(--third);
  max-width: 300px;
}
.mt-hr-blue {
  border: 1px solid var(--blue);
  max-width: 300px;
}

.sponsors {
  display: inline-block;
  width: 100%;
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.5);
  /* box-shadow: 0 0 40px 20px rgba(255, 255, 255, 0.07); */
  background-color: var(--secondary);
}
.sponsors-bar {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-evenly;
  position: absolute;
  top: calc(5vw + 42vh);
  left: 20%;
  height: 8%;
  z-index: 101;
  max-width: 70%;
  margin: auto;
  margin-bottom: calc(230px - 10vw);
}

.sponsors .sponsors-line {
  display: flex;
  flex-wrap: wrap;
  margin: auto;
  justify-content: space-evenly;
  width: 66%;
  padding: 0;
}

.sponsors section div {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 33%;
  transition-duration: 0.4s;
}

.sponsors section img {
  transform: scale(0.95);
  width: 100%;
  transition-duration: 0.4s;
}

#ef {
  width: 20vw;
}
#infomaniak {
  width: 20vw;
}

#makita {
  transform: translateX(-60px);
}
#agep {
  transform: translateX(10px);
}

#cea {
  transform: translateX(4vw) translateY(2vw) scale(1.3);
}
#ceaaa {
  display: flex;
  flex-direction: column;
}
#efff {
  display: flex;
  flex-direction: column;
  transform: translateY(1vw);
}
#infomaniakk {
  display: flex;
  flex-direction: column;
  transform: translateY(1vw);
}
#tes {
  width: 20vw;
}
#tobler {
  width: 30vw;
}

#ceaaa p {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: calc(0.8em + 0.3vw);
  color: white;
  text-align: center;
  transform: translateX(4vw) translateY(2vw);
  margin-top: 30px;
  width: 120%;
}
#efff p {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: calc(0.6em + 0.5vw);
  color: white;
  text-align: center;
  transform: translateY(-1vw);
  margin-top: 30px;
  width: 110%;
}
#infomaniakk p {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: calc(0.6em + 0.5vw);
  color: white;
  text-align: center;
  transform: translateY(-1vw) translateX(65px);
  margin-top: 30px;
  width: 110%;
}
.sponsors section img:hover {
  opacity: 0.7;
}

.sponsors section .spacefiller-phone {
  width: 24%;
  display: none;
}

.association {
  margin-top: 40px;
  display: inline-block;
  width: 100%;
  background-color: var(--primary);
}

.container-comite {
  display: flex;
  max-width: 1100px;
  margin: auto;
}

.comite-line {
  padding: 10px;
  display: inline-block;
  width: 100%;
  align-items: center;
}

.comite-member {
  display: inline-block;

  align-items: center;
  width: 25%;
  margin-bottom: 50px;
}

.comite-filler {
  width: 24.5;
}

.comite-member p {
  text-align: center;
  margin: 0;
  padding-bottom: 7px;
  display: flex;
  flex-direction: column;
}

.comite-img {
  width: 80%;
}

.home-screen {
  height: calc(100vh - var(--navbar-height) - var(--global-margin));
  display: flex;
  flex-direction: column;
  padding-bottom: 20px;
  overflow: hidden;
  background-color: var(--black);
}

.home-screen-bg {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 1;
  background-image: url("@/assets/images/PhotoGallery/slideshow/3.jpg");
  opacity: 0.4;
  /* background-image: url("@/assets/images/PhotoGallery/DSC_8927_final.jpg"); */
  /* background-color: var(--primary-darker); */
  background-size: cover;
  background-position: center;
  overflow: hidden;

  filter: blur(8px);
  /* -webkit-filter: blur(8px); */
}

.higlight-text {
  color: var(--third);
  font-weight: bolder;
}

.sponsors-bar {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-evenly;
  height: 100px;
  z-index: 5;
  max-width: 80%;
  margin: auto;
  margin-bottom: 40px;
}

.sponsors-row {
  display: flex;
  flex-direction: row;
  gap: 2vw;
}

.sponsor-el {
  /* background-color: chartreuse; */
  flex-grow: 1;
  z-index: 10000;
  max-width: 200px;
  max-height: 250px;
  width: 11vw;
  display: flex;
  justify-content: center;
  flex-direction: column;
  transform: translateY(10px);
  transition: opacity ease-in-out 0.2s;
}
#agep {
  position: relative;
  left: -1vw;
}

.sponsor-el img {
  max-width: 100%;
  max-height: 100%;
}

.sponsor-el:hover {
  opacity: 0.7;
}

.sponsor-el * {
  max-width: 100%;
  max-height: 100%;
}

@media only screen and (max-height: 700px) {
  #sponsors-bar {
    height: 50px;
  }
}

/* @media screen and (max-width: 650px) {
    .sponsors-bar {
        flex-direction: column;
    }
    .sponsor-el {
        flex-wrap: wrap;
        width: 20vw;
    }
} */

@media screen and (max-width: 340px) {
  #jardin {
    height: 32%;
  }
}

@media (max-height: 700px) {
  .sponsor-el {
    transform: scale(0.8);
  }
  .sponsors-row {
    top: calc(20vw + 30vh);
  }
}

@media screen and (max-width: 500px) {
  .sponsors-bar {
    width: 95vw;
    position: absolute;
    top: 80vh;
    left: 2.5vw;
  }
  .sponsors-row {
    width: 100%;
  }

  .sponsor-el {
    width: 40vw;
  }
}

@media screen and (max-width: 500px) {
  .line-up-container {
    padding-left: 10px;
    padding-right: 10px;
  }
  .line-up-time {
    height: 25px;
    width: 50px;
    font-size: 1em;
  }
  .line-up-artist .line-up-time {
    height: 30px;
    width: 65px;
  }
}

@media screen and (max-width: 850px) {
  @media (max-height: 80vw) {
    .rotate-phone {
      display: flex;
      flex-direction: column;
    }
  }

  .sponsors-bar {
    width: 100%;
    position: absolute;
    top: 65vh;
    left: 10%;
  }
  #ef {
    width: 40vw;
  }
  #ceaaa {
    transform: translateX(-3vw) translateY(50px) scale(0.8);
  }
  #makita {
    transform: translateX(-10px);
  }
  #agepo {
    transform: translateX(10px);
  }
  #tes {
    width: 35vw;
    position: relative;
    left: -10vw;
  }
  #tobler {
    width: 30vw;
  }

  .line-up-zone {
    width: 100%;
    height: 700px;
  }
  .line-up-time,
  .line-up-name {
    font-size: 1.15em;
  }
  .line-up-artist-big .line-up-time,
  .line-up-artist-big .line-up-name {
    font-size: 1.35em;
  }
  #loudjack {
    position: relative;
    height: 70px;
    top: -22px;
  }
  .line-up-stagename {
    font-size: 1.35em;
  }
  .line-up-time {
    height: 35px;
    width: 75px;
  }
  .line-up-artist-big .line-up-time {
    height: 45px;
    width: 100px;
  }
  .line-up-container {
    min-width: 130px;
  }
  .line-up-box-2 {
    padding-left: 2px;
    padding-right: 2px;
  }

  .reverse-slide,
  .slide {
    width: 400%;
    /* height: 50px; */
  }

  .info-section-hr {
    display: none;
  }

  #plan-para {
    margin-right: 0px;
  }

  #date-hr {
    margin-left: 0;
    margin-right: 0;
  }

  .main-page-button {
    font-weight: bold;
    color: var((--primary));
    background-color: var(--white);
    cursor: pointer;
    border-radius: 5px;
    border: 0;
  }

  .sponsors-line {
    width: 90% !important;
  }

  .sponsors section div {
    width: 49%;
  }

  #sponsor-space-filler {
    width: 25%;
  }

  .sponsors section .spacefiller-phone {
    display: flex;
  }

  #qsn-img {
    padding: 0;
  }

  .comite-line {
    width: 100% !important;
  }

  .comite-section-hr {
    max-width: 330px;
  }

  .comite-member {
    width: 49% !important;
  }

  .comite-member p {
    padding-bottom: 4px;
  }

  .home-screen-bg {
    background-position: 45% 10%;
  }

  #infos-container {
    display: flex;
    flex-direction: column;
  }

  #infos-container * {
    text-align: center;
  }
}
</style>
