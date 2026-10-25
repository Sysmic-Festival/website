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
      <video
        class="home-screen-bg"
        src="@/assets/images/PhotoGallery/slideshow/fonddeenhaut.mp4"
        autoplay
        muted
        loop
        playsinline
      ></video>
        <AnimatedLogo id="Logo" />
      <Timer />
      <div class="sponsors-bar">
        <div class="sponsors-row">
          <div class="sponsor-el">
            <a href="https://www.yuh.com/fr/">
              <img src="@/assets/images/sponsors/Yuh_Logo_Single_White_RGB.png" />
            </a>
          </div>
          <div class="sponsor-el">
            <a target="_BLANK" href="https://infomaniak.events/fr-ch">
              <img src="@/assets/images/sponsors/infomaniak-sa.png" />
            </a>
            </div>
          <div class="sponsor-el" id="agep">
            <a href="https://agepoly.ch/en/">
              <img src="@/assets/images/sponsors/AGEPoly.svg" />
            </a>
          </div>
          <div class="sponsor-el">
            <a target="_BLANK" href="https://focuswater.ch/fr/">
              <img src="@/assets/images/sponsors/FW_White_Red_RGB.png" />
            </a>
          </div>
          <div class="sponsor-el">
            <a target="_BLANK" href="https://www.impact-vision.ch/">
              <img src="@/assets/images/sponsors/ImpactV-W.png" />
            </a>
          </div>
        </div>
      </div>
    </div>
    <section id="lineup" class="line-up">
    <div class="lu-row lu-head">
    <div class="lu-label lu-title">Line-up</div>
    <div class="lu-hours">
      <span style="--h:0">20h00</span>
      <span style="--h:1">21h00</span>
      <span style="--h:2">22h00</span>
      <span style="--h:3">23h00</span>
      <span style="--h:4">00h00</span>
      <span style="--h:5">01h00</span>
      <span style="--h:6">02h00</span>
      <span style="--h:7">03h00</span>
    </div>
  </div>

  <div class="lu-row">
    <div class="lu-label">main nexus</div>
    <div class="lu-track">
      <div class="lu-set" style="--s:45;--e:105"><b>TiBolt</b><small>20h45 - 21h45</small></div>
      <div class="lu-set" style="--s:135;--e:195"><b>RICCIO</b><small>22h15 - 23h15</small></div>
      <div class="lu-set" style="--s:240;--e:280"><b>kissed</b><small>00h00 - 00h40</small></div>
      <div class="lu-set" style="--s:325;--e:405"><b>DJ.ALF</b><small>01h25 - 02h45</small></div>
    </div>
  </div>

  <div class="lu-row">
    <div class="lu-label">hit block</div>
    <div class="lu-track">
      <div class="lu-set" style="--s:105;--e:165"><b>Fréquence banane</b><small>21h45 - 22h45</small></div>
      <div class="lu-set" style="--s:195;--e:255"><b>Fréquence banane</b><small>23h15 - 00h15</small></div>
      <div class="lu-set" style="--s:280;--e:345"><b>Fréquence banane</b><small>00h40 - 01h45</small></div>
    </div>
  </div>

  <div class="lu-row">
    <div class="lu-label">tek bunk'r</div>
    <div class="lu-track">
      <div class="lu-set" style="--s:30;--e:90"><b>Michaël Kornbeck</b><small>20h30 - 21h30</small></div>
      <div class="lu-set" style="--s:120;--e:180"><b>Rys</b><small>22h00 - 23h00</small></div>
      <div class="lu-set" style="--s:210;--e:270"><b>Klud</b><small>23h30 - 00h30</small></div>
      <div class="lu-set" style="--s:300;--e:360"><b>Plyometrics</b><small>01h00 - 02h00</small></div>
    </div>
  </div>
</section>
<!--
  <section class="button-section">
    <a
     class="main-page-button"
     href="https://infomaniak.events/fr-ch/festivals/sysmic-30th-edition/bbee9152-0dfc-4a2e-bc33-658d91e4a538/event/1664799"
     target="_blank"
     rel="noopener noreferrer"
    >
      ticketerie →
    </a>
  </section>
  -->
          <div class="slider">
        <div class="reverse-slide">
          <img class="band" src="@/assets/images/utilitaries/long-band-newlogo.svg" />
        </div>
      </div>

    <div class="photo-gallery">
      <Slideshow />
    </div>

    <div id="infos" class="infos">
<h1 class="h1-primary-background">Infos pratiques</h1>

<div id="infos-container" class="info-board">
  <div class="info-group">
    <h2 class="info-label" style="--x:0px;  --r:-2deg">Billetterie</h2>
    <p class="info-box" style="--x:40px;  --r:1.5deg">Billet : 15 CHF</p>
    <p class="info-box" style="--x:-10px; --r:-1deg">Vente le 27 et 28 Octobre<br />sur la place Ada Lovelace</p>
    <p class="info-box" style="--x:70px;  --r:2deg">Paiement en Camipro, cash, carte ou Twint</p>
    <p class="info-box" style="--x:15px;  --r:-2deg">Le soir même : 20 CHF</p>
  </div>

  <div class="info-group">
    <h2 class="info-label" style="--x:50px; --r:2deg">Date</h2>
    <p class="info-box" style="--x:-20px; --r:-1.5deg">30 octobre 2026</p>
    <p class="info-box" style="--x:60px;  --r:1deg">Début des entrées : 20h</p>
    <p class="info-box" style="--x:10px;  --r:-2deg">Début des concerts : 20h30</p>
    <p class="info-box" style="--x:80px;  --r:1.5deg">Fin : 03h00</p>
  </div>
</div>
      <div class="more-info">
  <p class="info-box" style="--x:-25px; --r:-1.5deg">
    Plus d'infos sur la partie MT
    <RouterLink to="/faq#micros" class="more-info-link">ici →</RouterLink>
  </p>
</div>
      <section class="faq-list" style="display: flex; flex-direction: column; align-items: center">

        <FAQRow title="Y a-t-il un vestiaire ?">
          Oui! Un vestiaire est disponible gratuitement, cependant nous
          déclinons toute responsabilité en cas de perte ou vol.
        </FAQRow>

        <FAQRow title="Existe-il des navettes pour le retour ?">
          Oui! En plus des transports en commun normaux, il y aura des navettes
          gratuites. Elles partiront à 01:30, 02:30 et 03:15 de l'arrêt Piccard
          (directement à la sortie du festival).<br />
          <br />
          Les navettes desserviront :<br />
          Renens, Malley, St-François et les arrêts entre.
        </FAQRow>

        <FAQRow title="Les sacs sont-ils autorisés ?">
          Non! Malheureusement, pour des raisons de sécurité, nous n'acceptons
          pas les sacs dans l’enceinte de la manifestation. Nous vous prions de
          venir sans sac à dos.
        </FAQRow>

        <FAQRow title="Comment puis-je obtenir un Ticket?">
          Les tickets seront mis en vente sur la place Ada Lovelace de l’EPFL durant la
          semaine précédant le festival.
        </FAQRow>
      </section>
      <section class="button-section">
        <router-link to="/faq">
          <button class="main-page-button">FAQ →</button>
        </router-link>
      </section>
      <div class="slider">
        <div class="slide">
          <img class="band" src="@/assets/images/utilitaries/long-band-newlogo.svg" />
        </div>
      </div>
      <!-- <div class="container-large" style="margin-bottom: 25px"> 
        <section style="flex: 1">
          <h2 class="h2-primary-background" id="plan-title">Accès</h2>
          <p id="plan-para">
            Le festival a lieu dans le batiment CE à L’EPFL dans la commune
            d’Ecublens. Il est accessible en transports en commun par le métro
            M1 (arrêt EPFL ou UNIL SORGE), les bus 701, 31, 705 (arrêt Argand,
            Paqueret ou Piccard) et se situe près de l’autoroute A1 (sortie
            EPFL-UNIL).
          </p>
        </section>
        <section id="plan-image" style="flex: 1">
          <a
            href="https://www.google.com/maps/d/u/0/edit?mid=1CXFmGv1zlrAQgA84q9ZXzxnXD0qu938&usp=sharing"
            target="_blank"
          >
            <img
              class="img-responsive"
              src="@/assets/images/utilitaries/plan_acces.png"
            />
          </a>
        </section>
      </div> 
      <section class="button-section">
        <a
          class="main-page-button"
          href="/images/plan_interieur.png"
          target="_blank"
          >Plan du Festival →</a
        >
      </section> -->
    </div>

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
     <h1 class="h1-primary-background">L'association</h1>
      <div class="container container-vertical-phone">
        <section style="flex: 3; padding-top: 0; color: aliceblue">
          <p>
            Sysmic est constitué d’un comité de 31 personnes de toutes années et
            sections confondues. Nous travaillons tout au long de l’année afin
            d’offrir aux élèves de l’EPFL un festival de musique d’une soirée au
            sein même du campus.
            <br /><br />
            Originellement, l’association est dédiée à la section de
            Microtechnique pour laquelle nous organisons, en parallèle du
            festival, un apéro dinatoire!
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
        <div class="more-info">
    <p class="info-box" style="--r:1.5deg">
      Plus d'infos sur l'association
      <router-link to="/about-us" class="more-info-link">À propos →</router-link>
    </p>
  </div>
      </div>
      <div class="slider">
        <div class="reverse-slide">
          <img class="band" src="@/assets/images/utilitaries/long-band-newlogo.svg" />
        </div>
      </div>
    </div>
    <div id="comite" class="comite">
      <h1 class="h1-primary-background comite-title">Comité 2026</h1>
      <h2 class="pole-title">Présidence</h2>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>May Dubuy</h4>
            <p>Présidente</p>
            <img class="comite-img" src="@/assets/images/comite/may.jpg" />
          </div>
        </section>
      </div>
      <div class="container-comite">
        <section class="comite-line">
          <div class="comite-member">
            <h4>Antoine Eisinger</h4>
            <p>VP Logistique</p>
            <img class="comite-img" src="@/assets/images/comite/antoine.jpg" />
          </div>
          <div class="comite-member">
            <h4>Anthony Magnin</h4>
            <p>VP Communication</p>
            <img class="comite-img" src="@/assets/images/comite/anto.jpg" />
          </div>
          <div class="comite-member">
            <h4>Anouck Fazio</h4>
            <p>VP Animation</p>
            <img class="comite-img" src="@/assets/images/comite/Anouck_2.jpg" />
          </div>
          <div class="comite-member">
            <h4>Philippe Logoz</h4>
            <p>Trésorier</p>
            <img
              class="comite-img"
              src="@/assets/images/comite/philippe.jpg"
            />
          </div>
        </section>
      </div>

      
      <h2 class="pole-title">Logistique</h2>
      <div class="container-comite">
          <div class="comite-member">
            <h4>Taos Drouet</h4>
            <p>Décoration</p>
            <img class="comite-img" src="@/assets/images/comite/taos.jpg" />
          </div>
          <div class="comite-member">
            <h4>Katarina Licina</h4>
            <p>Décoration</p>
            <img class="comite-img" src="@/assets/images/comite/kata.jpg" />
          </div>
          <div class="comite-member">
            <h4>Léa Françoise</h4>
            <p>Sécurité</p>
            <img class="comite-img" src="@/assets/images/comite/lea.jpg" />
          </div>
          <div class="comite-member">
            <h4>Adrien Lievre</h4>
            <p>Sécurité</p>
            <img class="comite-img" src="@/assets/images/comite/adrien_l.jpg" />
          </div>
          <div class="comite-member">
            <h4>Arthur Busseret</h4>
            <p>Technique de scène</p>
            <img class="comite-img" src="@/assets/images/comite/arthur.jpg" />
          </div>
          <div class="comite-member">
            <h4>Mélodie Serreau</h4>
            <p>Adjointe au technique de scène</p>
            <img class="comite-img" src="@/assets/images/comite/melodie_2.jpg" />
          </div>
          <div class="comite-member">
            <h4>Edgar Wolff</h4>
            <p>Élec/Light</p>
            <img class="comite-img" src="@/assets/images/comite/edgar.jpg"
            />
          </div>
          <div class="comite-member">
            <h4>Marìa Mulet</h4>
            <p>Matériel</p>
            <img
              class="comite-img" src="@/assets/images/comite/maria.jpg" />
          </div>
          <div class="comite-member">
            <h4>Enesa Mazrekaj</h4>
            <p>RH</p>
            <img class="comite-img" src="@/assets/images/comite/enesa.jpeg" />
          </div>

      </div>

      
      <h2 class="pole-title">Communication</h2>

      <div class="container-comite">
          <div class="comite-member">
            <h4>Solène Dumond</h4>
            <p>Community Manager</p>
            <img class="comite-img" src="@/assets/images/comite/solene.jpg" />
          </div>
          <div class="comite-member">
            <h4>Adrien Barmaz</h4>
            <p>Vidéaste</p>
            <img class="comite-img" src="@/assets/images/comite/adrien.b.jpg" />
          </div>
          <div class="comite-member">
            <h4>Evan Agullo</h4>
            <p>Graphisme</p>
            <img class="comite-img" src="@/assets/images/comite/evan.jpeg" />
          </div>
          <div class="comite-member">
            <h4>Audrey Huang</h4>
            <p>Graphisme</p>
            <img class="comite-img" src="@/assets/images/comite/audrey.jpeg" />
          </div>
          <div class="comite-member">
            <h4>Thomas Clement</h4>
            <p>Prévention/Durabilité</p>
            <img class="comite-img" src="@/assets/images/comite/thomas.jpeg" />
          </div>

      </div>

      <h2 class="pole-title">Animation</h2>

      <div class="container-comite">
          <div class="comite-member">
            <h4>Lea Mahfouf</h4>
            <p>Bar</p>
            <img class="comite-img" src="@/assets/images/comite/lea-old.jpg" />
          </div>
          <div class="comite-member">
            <h4>Antoine Reynaud</h4>
            <p>Bar</p>
            <img class="comite-img" src="@/assets/images/comite/antoine_cat.jpg" />
          </div>
          <div class="comite-member">
            <h4>Solvene De Foucauld</h4>
            <p>Programmation</p>
            <img class="comite-img" src="@/assets/images/comite/solvene.jpg" />
          </div>
          <div class="comite-member">
            <h4>Isak Okanovic</h4>
            <p>Programmation</p>
            <img class="comite-img" src="@/assets/images/comite/isak.jpg" />
          </div>

          <div class="comite-member">
            <h4>Paolo Festa</h4>
            <p>Catering</p>
            <img class="comite-img" src="@/assets/images/comite/paolo_2.jpg" />
          </div>
          <div class="comite-member">
            <h4>Floriane Baudin</h4>
            <p>Catering</p>
            <img class="comite-img" src="@/assets/images/comite/florianne.jpg"/>
          </div>
          <div class="comite-member">
            <h4>Maxime Coeytaux</h4>
            <p>Escape Game</p>
            <img class="comite-img" src="@/assets/images/comite/maxime.pasd.jpg" />
          </div>
          <div class="comite-member">
            <h4>Ulysse Zbinden</h4>
            <p>Escape Game</p>
            <img class="comite-img" src="@/assets/images/comite/ulysse.jpg" />
          </div>

      </div>

      
        <h2 class="pole-title">Aide à la Trésorerie</h2>
        <div class="container-comite">
          <div class="comite-member">
            <h4>Alice Trignon</h4>
            <p>Sponsoring</p>
            <img class="comite-img" src="@/assets/images/comite/alice.jpg" />
          </div>
          <div class="comite-member">
            <h4>Maxime Dominguez</h4>
            <p>IT/Ticketing</p>
            <img class="comite-img" src="@/assets/images/comite/maxime.d_2.jpg" />
          </div>
      </div>

      
      <h2 class="pole-title">Membres de soutien</h2>

      <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Romain Klein</h4>
                        <p>Membre de Soutien</p>
                        <img class="comite-img" src="@/assets/images/comite/romain.jpg">
                    </div>
                    <div class="comite-member">
                        <h4>Matthieu Bénard</h4>
                        <p>Membre de Soutien</p>
                        <img class="comite-img" src="@/assets/images/comite/matthieu-old.jpg" />
                    </div>
                </section>
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
  display: inline-block;
  margin: 10px;
  padding: 22px 48px;
  font-size: 1.4rem;
  font-weight: bold;
  color: #000;
  background-color: #fff;
  border: 2px solid #000;
  border-radius: 0;
  cursor: pointer;
  text-decoration: none;

  /* squashed text */
  transform: scaleY(0.75);
  letter-spacing: -0.02em;
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
  scroll-margin-top: calc(var(--navbar-height) + var(--global-margin));
  padding-top: calc(var(--navbar-height) + 60px);
  background:
      linear-gradient(rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.35)),
      url("@/assets/images/utilitaries/final_logo.png") center / cover no-repeat;
  --total: 420;           
  --blue: #0037ff;
  --label-w: 260px;
  display: flex;
  flex-direction: column;
  gap: 24px;
  overflow-x: auto;   
  box-shadow: none;
}

.lu-row {
  display: grid;
  grid-template-columns: var(--label-w) minmax(900px, 1fr);
  align-items: center;
  min-width: 1200px;
}

.lu-label {
  justify-self: start;
  padding: 6px 18px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  font-size: 2rem;
  font-weight: bold;
  line-height: 1.1;
}
.lu-title { font-size: 3rem; }

.lu-hours {
  position: relative;
  height: 40px;
  background: #fff;
  border: 2px solid #000;
  box-sizing: border-box;
  margin: 0;                 
  overflow: hidden;          
}

.lu-hours span {
  position: absolute;
  top: 50%;
  left: calc(var(--h) * 60 / var(--total) * 100%);
  transform: translate(-50%, -50%);
  color: #000;
  font-style: italic;
  font-weight: bold;
  font-size: 1.5rem;
  white-space: nowrap;
}


.lu-hours span:first-child {
  transform: translate(8px, -50%);      
}
.lu-hours span:last-child {
  transform: translate(calc(-100% - 8px), -50%);  
}


.lu-track {
  position: relative;
  height: 150px;
  background:
    linear-gradient(var(--blue), var(--blue)) right / 4px 100% no-repeat,
    repeating-linear-gradient(
      to right,
      var(--blue) 0,
      var(--blue) 4px,
      transparent 4px,
      transparent calc(60 / var(--total) * 100%)
    );
}

.lu-hours { margin: 0 2px; }  

.lu-set {
  position: absolute;
  top: 12px;
  bottom: 12px;
  left: calc(var(--s) / var(--total) * 100%);
  width: calc((var(--e) - var(--s)) / var(--total) * 100%);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 8px 10px;
  box-sizing: border-box;
  background: var(--blue);
  color: #fff;
  border-radius: 0;
}
.lu-set b { font-size: 1.6rem; font-weight: normal; line-height: 1.1; }
.lu-set small { font-size: 1.1rem; }

@media screen and (max-width: 850px) {
  .line-up {
    padding: calc(var(--navbar-height) + 30px) 15px 20px;
    gap: 28px;
    overflow-x: visible;
  }

  .lu-row {
    display: block;
    min-width: 0;
  }

  .lu-hours { display: none; }

  /* stage names: smaller boxes, no longer full width */
  .lu-label {
    display: inline-block;
    width: auto;
    margin-bottom: 12px;
    padding: 4px 12px;
    font-size: 1.3rem;
  }
  .lu-title { font-size: 2rem; }
  .lu-row:nth-of-type(odd) .lu-label  { margin-left: 8%; }
  .lu-row:nth-of-type(even) .lu-label { margin-left: 25%; }

  .lu-track {
    height: auto;
    background: none;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }

  .lu-set {
    position: static;
    width: 58%;
    min-height: 0;
    padding: 6px 8px;
    gap: 6px;
  }
  .lu-set b     { font-size: 1.1rem; }
  .lu-set small { font-size: 0.85rem; }

  .lu-set:nth-child(4n + 1) { margin-left: 0; }
  .lu-set:nth-child(4n + 2) { margin-left: 38%; }
  .lu-set:nth-child(4n + 3) { margin-left: 12%; }
  .lu-set:nth-child(4n + 4) { margin-left: 30%; }
}

.slide {
  width: 200%;
  height: auto;
  background-size: contain;
  background-repeat: repeat-x;
  animation: slide 20s linear infinite;
  margin-top: 20px;
  margin-bottom: 20px;
}
.reverse-slide {
  width: 200%;
  height: auto;
  background-size: contain;
  background-repeat: repeat-x;
  animation: reverse-slide 20s linear infinite;
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
    ); 
  }
}

@keyframes reverse-slide {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(
      -50%
    ); 
  }
}

.photo-gallery {
  background-color: var(--primary);
}

.infos {
  padding-top: 10px;        
}

.info-group {
  align-items: center;       
  flex: 1 1 380px;
  max-width: 480px;
}

.info-label,
.info-box {
  text-align: center;
}

.infos .h1-primary-background {
  display: block;
  width: fit-content;
  margin: 0 auto 10px;
  padding: 8px 28px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  letter-spacing: -0.02em;
}

.info-board {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;  
  align-items: flex-start;
  gap: 2rem 5rem;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 25px;
  box-sizing: border-box;
}

.info-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  flex: 0 0 480px;          
  max-width: 100%;
}

.info-label,
.info-box {
  margin: 0;
  transform: translateX(var(--x, 0)) rotate(var(--r, 0deg)) scaleY(0.75);
  letter-spacing: -0.02em;
  text-align: left;
  text-justify: auto;
  border-radius: 0;
}

.info-label {
  padding: 8px 26px;
  font-size: 2.2rem;
  background: #fff;
  color: #000;
  border: 2px solid #000;
}

.info-box {
  padding: 14px 22px;
  font-size: 1.5rem;
  line-height: 1.3;
  background: #0037ff;
  color: #fff;
  font-weight: bold;
}
@media screen and (max-width: 850px) {
.infos {
  padding-top: 50px;
}

#infos-container.info-board {
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  padding: 0 15px;
}

.info-group {
  width: 100%;
  max-width: 420px;
  align-items: center;
}

.info-label,
.info-box {
  width: fit-content;
  max-width: 100%;
  text-align: center !important;
  transform: translateX(calc(var(--x) * 0.3)) rotate(var(--r)) scaleY(0.75);
}
}

.more-info {
  display: flex;
  justify-content: center;
  margin: 50px 0 40px;
}

.more-info .info-box {
  text-align: center;
}

.more-info-link {
  display: inline-block;
  margin-left: 10px;
  padding: 0 10px;
  background: #fff;
  color: #000;
  text-decoration: none;
  letter-spacing: -0.02em;
}
.more-info-link:hover {
  background: #000;
  color: #fff;
}

.faq-list > :nth-child(odd)  { transform: translateX(-30px) rotate(-0.8deg); }
.faq-list > :nth-child(even) { transform: translateX(30px)  rotate(0.8deg); }

@media screen and (max-width: 850px) {
  .faq-list > :nth-child(odd)  { transform: translateX(-8px); }
  .faq-list > :nth-child(even) { transform: translateX(8px); }
}

.association .h1-primary-background {
  display: block;
  width: fit-content;
  margin: 0 auto 30px;
  padding: 8px 28px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  letter-spacing: -0.02em;
}
.more-info {
  display: flex;
  justify-content: center;
  width: 100%;
  margin: 50px 0 40px;
}
  .association p {
    color: #fff;
  }
  .more-info .info-box {
  text-align: center;
  width: fit-content;
  max-width: 90%;
}

.sponsors {
  display: inline-block;
  width: 100%;
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.5);
  background-color: var(--secondary);
}
.sponsors-bar {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  position: relative;
  max-width: 60%;
  max-height:20%;
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
  background-color: var(--secondary);
}

/* "Comité 2026": white block like the other section titles */
.comite .h1-primary-background {
  display: block;
  width: fit-content;
  margin: 0 auto 30px;
  padding: 8px 28px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  letter-spacing: -0.02em;
}

/* blue pole titles */
.pole-title {
  display: block;
  width: fit-content;
  margin: 50px auto 10px;
  padding: 6px 26px;
  background: #0037ff;
  color: #fff;
  border-radius: 0;
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  text-align: center;
}

.container-comite {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: center;
  gap: 30px 20px;
  max-width: 1100px;
  margin: 10px auto 0;
}

.comite-line {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px 20px;
  width: 100%;
  padding: 10px;
}

.comite-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 22%;
  margin-bottom: 20px;
}

.comite-member h4 {
  margin: 0;
  padding: 4px 12px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  font-size: 1.1rem;
  text-align: center;
  letter-spacing: -0.02em;
}

.comite-member p {
  margin: -2px 0 10px;
  padding: 2px 12px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  font-size: 0.95rem;
  text-align: center;
}

.comite-img {
  width: 80%;
  border: 2px solid #000;
  border-radius: 0;
}

.home-screen {
  position: relative;   
  overflow: hidden;    
  height: calc(100vh - var(--navbar-height) - var(--global-margin));
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-bottom: 20px;
  background-color: var(--black);
  justify-content: space-around;
}

.home-screen-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  object-fit: cover;
  object-position: center;
  opacity: 0.4;
  filter: blur(8px);
  transform: scale(1.05); /* hides the soft blurred edges */
}

/* keep the content above the video */
.home-screen > :not(.home-screen-bg) {
  position: relative;
  z-index: 1;
}

.higlight-text {
  color: var(--third);
  font-weight: bolder;
}

/* .sponsors-bar {
  display: flex;
  flex-direction: row;
  position: absolute;
  justify-content: space-evenly;
  height: 100px;
  z-index: 5;
  max-width: 80%;
  margin: auto;
  margin-bottom: 40px;
} */

.sponsors-row {
  display: flex;
  flex-direction: row;
  gap: 5%;
  max-width: 100%;
} 

.sponsor-el {
  /* background-color: chartreuse; */
  flex-grow: 1;
  z-index: 5000;
  max-width: 200px;
  max-height: 100px;
  width: 20%;
  height: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  /* transform: translateY(10px); */
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

/* @media only screen and (max-height: 700px) {
  #sponsors-bar {
    height: 50px;
  }
} */

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
  /* .sponsors-bar {
    width: 95vw;
    position: absolute;
    top: 80vh;
    left: 2.5vw;
  } */
  .sponsors-row {
    width: 100%;
  } 

  .sponsor-el {
    width: 40vw;
  }
}

.coming-soon {
  text-align: center;
  font-size: 2rem;
  font-weight: bold;
  color: var(--white);
  padding: 40px 0;
}

@media screen and (max-width: 500px) {
  .line-up-container {
    padding-left: 10px;
    padding-right: 10px;
    flex-direction: column;
  }
  .line-up-stage {
    width: 90%;
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
    max-width: 90%;
    /* position: absolute;
    top: 65vh;
    left: 10%; */
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
