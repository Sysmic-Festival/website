<script setup>

import NavBar from '../components/NavBar.vue'
import Timer from '../components/Timer.vue';
import Slideshow from '../components/Slideshow.vue';
import AnimatedLogo from '../components/AnimatedLogo.vue';
import FAQRow from '../components/FAQRow.vue';

</script>

<template>
    <div>
        <div class="home-screen">
            <div class="home-screen-bg"></div>
            <AnimatedLogo id="Logo"/>
            <div id="sponsors-bar">
                <div class="sponsors-row">
                    <div class="sponsor-el">
                        <a href="https://www.forum-epfl.ch/">
                            <img src="@/assets/images/sponsors/Forum-epfl-logo.png">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a href="https://www.logitech.com/de-ch">
                            <img src="@/assets/images/sponsors/logitech-logo.svg">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a href="https://fr.brio-mate.com/">
                            <img src="@/assets/images/sponsors/Brio-H-blanc-logo.svg">
                        </a>
                    </div>
                </div>
                <div class="sponsors-row">
                    <div class="sponsor-el">
                        <a href="https://www.l-dudu.ch/">
                            <img src="@/assets/images/sponsors/L-DuDu-logo.png">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a href="https://www.visilab.ch/fr/">
                            <img src="@/assets/images/sponsors/Visilab-couleur-logo.png">
                        </a>
                    </div>
                    <div class="sponsor-el">
                        <a href="https://rivella.ch/fr/">
                            <img src="@/assets/images/sponsors/Rivella-logo.svg">
                        </a>
                    </div>
                </div>
            </div>
            <Timer />
        </div>
    
        <div id="line-up" class="line-up">
            <img class="img-responsive" src="@/assets/images/utilitaries/line-up.png" />
            <a class="main-page-button"  href="/images/timeline.png" target="_blank">Programmation 2022 complète →</a>
        </div>

        <div class="photo-gallery">
            <Slideshow />
        </div>

        <div id="infos" class="infos">
            <h1 class="h1-primary-background">Infos Pratiques</h1>
            <div id="infos-container" class="container">
                <section style="">
                    <h2 class="h2-primary-background">Billeterie</h2>
                    <p >
                        Prélocation: <span class="higlight-text">15CHF</span>
                        <br><br>
                        Vente du <span class="higlight-text"> 17 au 18 octobre </span> à l'Esplanade à <span class="higlight-text">12H00</span>
                        <br>
                        Payement en Camipro ou en cash
                        <br><br>
                        Le soir même: <span class="higlight-text">20CHF</span>
                    </p>
                </section>
                <hr class="info-section-hr" id="date-hr">
                <section style="">
                    <h2 class="h2-primary-background">Date</h2>
                    <p>
                        <span class="higlight-text">20 octobre 2023</span>
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
            <hr class="mt-hr">
            <div class=" container" style="flex-direction:column;align-items: center;font-weight: 900;"><p>Pour la partie <span style="color:var(--third)">MT</span>, ça se passe <RouterLink to="/faq#micros" style="color:var(--white); text-decoration: underline;">ici</RouterLink> !</p></div>
            <hr class="mt-hr">
            <hr class="mt-hr" style="max-width:200px">
            <hr class="mt-hr" style="max-width:150px">
            <br>
            <section style="display:flex; flex-direction:column;align-items:center">
                
        <FAQRow title="Y a-t-il un vestiaire ?">
          Durant le festival, nous mettons a votre disposition un vestiaire gratuit. Nous
            déclinons toutefois toute responsabilité en cas de perte ou de vol.
        </FAQRow>

        <FAQRow title="Existe-il des navettes pour le retour ?">
            Oui! En plus des transports en commun normaux, il y aura des navettes spéciales.<br />
          Elles partiront à 01:15, 02:15 et 03:15 de l'arrêt Piccard (directement à la sortie du festival) et passant par
          Renens-Gare, Malley et Lausanne-Flon ainsi que tous les principaux arrêts de bus sur le chemin.
          <br><br>
          Les bus passeront par : <br>
          UNIL-Sorge, Mouline, Berges, Chavannes-R, Plaine, Chavannes-R, Cèdres, Concorde,
          Planta,Chavannes-R, GlycineRenens, Gare Sud, 	Chêne, Rue du lac,  Longemalle,
          Malley nord,Galicien,Prélaz Les Rose, Couchirad, EPSIC, Port-Franc, Lausanne-Flon
        </FAQRow>
        
        <FAQRow title="Les sacs sont-ils autorisés ?">
          <p>Malheureusement, pour des raisons de sécurité, nous n'acceptons pas les sacs lors
            de la manifestation. Nous vous prions de venir sans sac à dos.</p>
        </FAQRow>

        <FAQRow title="Comment puis-je obtenir des prélocations?">
          Les prélocations seront mises en vente sur l'esplanade lors de la semaine précédant
          le festival, de 12:00 à 13:15, le mardi et le mercredi
        </FAQRow>
            </section>
            <section class="button-section">
                <router-link to="/faq">
                    <button class="main-page-button">FAQ →</button>
                </router-link>
            </section>
            <hr class="info-section-hr">
            <div class="container-large" style="margin-bottom:25px">
                <section style="flex:1">
                    <h2 class="h2-primary-background" id="plan-title">Accès</h2>
                    <p id="plan-para">
                        Le festival se déroule dans le batiment CE sur le site de L’EPFL situé sur la commune
                        d’Ecublens. Il est accessible en transports en commun par le métro M1 et se situe près de
                        l’autoroute A1 (sortie EPFL-UNIL).
                        Prenez le métro M1 jusqu’à l’arrêt EPFL ou UNIL SORGE.
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
        </div>


        <div id="sponsors" class="sponsors">
            <h1 class="h1-third-background">Sponsors 2022</h1>
            <section class="sponsors-line">
                <div>
                    <a target="_BLANK" href="https://www.logitech.com/de-ch">
                        <img src="@/assets/images/sponsors/logitech-logo.svg">
                    </a>
                </div>
                <div style="display:block">
                    <a target="_BLANK" href="https://fr.brio-mate.com/">
                        <img src="@/assets/images/sponsors/Brio-H-blanc-logo.svg">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.visilab.ch/fr/">
                        <img src="@/assets/images/sponsors/Visilab-couleur-logo.png">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://rivella.ch/fr/">
                        <img src="@/assets/images/sponsors/Rivella-logo.svg">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.forum-epfl.ch/">
                        <img src="@/assets/images/sponsors/Forum-epfl-logo.png">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://fastree3d.com/">
                        <img src="@/assets/images/sponsors/fastree3d-logo.png">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://agepoly.ch/">
                        <img src="@/assets/images/sponsors/AGEPoly.svg">
                    </a>
                </div>
                <div>
                    <a target="_BLANK" href="https://www.l-dudu.ch/">
                        <img src="@/assets/images/sponsors/L-DuDu-logo.png">
                    </a>
                </div>
                <div class="spacefiller-phone"></div>
                <div>
                    <a target="_BLANK" href="https://shop.morand.ch/fr/">
                        <img src="@/assets/images/sponsors/mrnd21.svg">
                    </a>
                </div>
            </section>
        </div>

        <div id="recrutement">
            <hr class="mt-hr" style="max-width:250px">
            <hr class="mt-hr" style="max-width:350px">
            <hr class="mt-hr" style="max-width:450px">
                <div class="" style="font-weight: 900;"><p style="text-align: center;">Vous cherchez à faire partie des <span style="color:var(--third)">Sponsors 2023</span> ? Cela se passe <a href="https://sysmic.ch/dossier_sponsoring_2023_FR.pdf" target="_blank" style="text-decoration: underline;color:var(--third);">ici</a> !</p></div>
            <hr class="mt-hr" style="max-width:450px">
            <hr class="mt-hr" style="max-width:350px">
            <hr class="mt-hr" style="max-width:250px">
            <br>
        </div>

        <div id="association" class="association">
            <h1 class="h1-primary-background">Qui sommes-nous ?</h1>
            <div class="container container-vertical-phone">
                <section style="flex:1 ; padding-top:0">
                    <p>
                        Sysmic est constitué d’un comité de 26 personnes de toutes années et sections confondues. Nous travaillons tout au long de l’année afin d’offrir aux élèves de l’EPFL un festival de musique d’une soirée au sein même du campus.
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
                <section id="qsn-img" style="flex:1">
                    <img src="@/assets/images/PhotoGallery/qui-sommes-nous-img.jpg" style="width: 105%;">
                </section>
            </div>
            <div class="container">
                <section>
                    <p style="text-align: center;">Si tu veux en savoir plus à propos de l'association, jettes un oeil à
                        la page <span ><router-link style="color:var(--white); text-decoration: underline;" to="/about-us">À propos</router-link></span>
                        !</p>
                </section>
            </div>
            <hr class="comite-section-hr">
            <h1 class="h1-primary-background comite-title">Comité</h1>

            <h2 class="h2-primary-background comite-title">Présidence</h2>
            <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Thomas Cirillo</h4>
                        <p>Président</p>
                        <img class="comite-img" src="@/assets/images/comite/cirillo-le-boss.png">
                    </div>
                </section>
            </div>
            <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Daoud Hakim</h4>
                        <p>VP Communication</p>
                        <img class="comite-img" src="@/assets/images/comite/dahood.png">
                    </div>
                    <div class="comite-member">
                        <h4>Raphaël Charozé</h4>
                        <p>VP Logistique</p>
                        <img class="comite-img" src="@/assets/images/comite/charooo.png">
                    </div>
                    <div class="comite-member">
                        <h4>Thomas Artru</h4>
                        <p>VP Animation</p>
                        <img class="comite-img" src="@/assets/images/comite/artru.png">
                    </div>
                    <div class="comite-member">
                        <h4>Sébastien Dévaud</h4>
                        <p>Trésorier</p>
                        <img class="comite-img" src="@/assets/images/comite/seby.png">
                    </div>
                </section>
            </div>

            <hr class="comite-section-hr">
            <h2 class="h2-primary-background comite-title">Logistique</h2>

            <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Adame Biruk</h4>
                        <p>Sécurité</p>
                        <img class="comite-img" src="@/assets/images/comite/adam.png">
                    </div>
                    <div class="comite-member">
                        <h4>Claire Lopez</h4>
                        <p>Sécurité</p>
                        <img class="comite-img" src="@/assets/images/comite/claire.png">
                    </div>
                    <div class="comite-member">
                        <h4>Nada AlAhmadi</h4>
                        <p>Matériel</p>
                        <img class="comite-img" src="@/assets/images/comite/absent.jpg">
                    </div>
                    <div class="comite-member">
                        <h4>Ghali Laraki</h4>
                        <p>Élec/Light</p>
                        <img class="comite-img" src="@/assets/images/comite/ghali.png">
                    </div>
                    <div class="comite-member">
                        <h4>Audrey Kasas</h4>
                        <p>Décoration</p>
                        <img class="comite-img" src="@/assets/images/comite/audrey.png">
                    </div>
                    <div class="comite-member">
                        <h4>Ieva Kvedarauskaite</h4>
                        <p>Décoration</p>
                        <img class="comite-img" src="@/assets/images/comite/ieva-avec-un-i.png">
                    </div>
                    <div class="comite-member">
                        <h4>Raphaël Pittet</h4>
                        <p>Technique de scène</p>
                        <img class="comite-img" src="@/assets/images/comite/pittet.png">
                    </div>
                    <div class="comite-member">
                        <h4>Ludovic Mareemootoo</h4>
                        <p>RH</p>
                        <img class="comite-img" src="@/assets/images/comite/ludo.jpg">
                    </div>
                </section>
            </div>

            <hr class="comite-section-hr">
            <h2 class="h2-primary-background comite-title">Communication</h2>
            <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Jeremy Serillon</h4>
                        <p>Spectacle</p>
                        <img class="comite-img" src="@/assets/images/comite/dj-rem.png">
                    </div>
                    <div class="comite-member">
                        <h4>Mathieu Benard</h4>
                        <p>IT/Webmaster</p>
                        <img class="comite-img" src="@/assets/images/comite/xxmatbenxx.png">
                    </div>
                    <div class="comite-member">
                        <h4>Maxime Teuber</h4>
                        <p>Graphisme</p>
                        <img class="comite-img" src="@/assets/images/comite/maxime-premier.png">
                    </div>
                    <div class="comite-member">
                        <h4>Paloma Garcia Moron</h4>
                        <p>Community Manager</p>
                        <img class="comite-img" src="@/assets/images/comite/paloma.png">
                    </div>
                    <div class="comite-member">
                        <h4>Maxime Schwartz</h4>
                        <p>Prévention/Durabilité</p>
                        <img class="comite-img" src="@/assets/images/comite/maxime-second.png">
                    </div>
                </section>
            </div>

            <hr class="comite-section-hr">
            <h2 class="h2-primary-background comite-title">Animation</h2>

            <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Eléonore Salin</h4>
                        <p>Bar</p>
                        <img class="comite-img" src="@/assets/images/comite/eleooo.png">
                    </div>
                    <div class="comite-member">
                        <h4>Anton Schenkel</h4>
                        <p>Programmation/Loges</p>
                        <img class="comite-img" src="@/assets/images/comite/anton.png">
                    </div>
                    <div class="comite-member">
                        <h4>Ella Neike</h4>
                        <p>Programmation/Loges</p>
                        <img class="comite-img" src="@/assets/images/comite/ella.jpg">
                    </div>

                    <div class="comite-member">
                        <h4>Basile Thiercelin</h4>
                        <p>Catering</p>
                        <img class="comite-img" src="@/assets/images/comite/basile-le-s.png">
                    </div>
                    <div class="comite-member">
                        <h4>Alice Reymond</h4>
                        <p>Escape Game</p>
                        <img class="comite-img" src="@/assets/images/comite/alice.png">
                    </div>
                    <div class="comite-member">
                        <h4>Lorie Xu</h4>
                        <p>Escape Game</p>
                        <img class="comite-img" src="@/assets/images/comite/lorie.png">
                    </div>
                </section>
            </div>

            <hr class="comite-section-hr">
            <h2 class="h2-primary-background comite-title">Aide à la Trésorerie</h2>

            <div class="container-comite">
                <section class="comite-line">
                    <div class="comite-member">
                        <h4>Aude-line Fleury</h4>
                        <p>Sponsoring</p>
                        <img class="comite-img" src="@/assets/images/comite/aude-line.png">
                    </div>
                    <div class="comite-member">
                        <h4>Rayan Rami</h4>
                        <p>Sponsoring</p>
                        <img class="comite-img" src="@/assets/images/comite/rayou.png">
                    </div>
                </section>
            </div>

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
    margin:10px;
    padding: 15px;
    font-weight: bold;
    color: var(--primary);
    background-color: var(--white);
    cursor: pointer;
    border-radius: 10px;
    border: 0;
}



.info-section-hr {
    border: 1px solid var(--third);
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
    border: 1px solid var(--third);
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

.mt-hr{
    border: 1px solid var(--third);
    max-width: 300px;
}

.sponsors {
    display: inline-block;
    width: 100%;
    background-color: var(--secondary);
}

.sponsors .sponsors-line {
    display: flex;
    flex-wrap: wrap;
    margin: auto;
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

.sponsors section img:hover {
    opacity: 0.70;
}

.sponsors section .spacefiller-phone{
    width: 24%;
    display: none;
}

.association {
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
}

.comite-filler{
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

}

.home-screen-bg{
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 1;

    background-image: url("@/assets/images/PhotoGallery/DSC_8927_final.jpg");
    background-size: cover;
    background-position: center;

    /* filter: blur(8px);
    -webkit-filter: blur(8px); */
}

.higlight-text{
    color: var(--third);
    font-weight: bolder;
}

#sponsors-bar {
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-evenly;
    height: 100px;
    z-index: 5;
    max-width: 70%;
    margin: auto;
    margin-bottom: 40px;
}

.sponsors-row {
    display: flex;
    flex-direction: row;
    gap: 10px;
}

.sponsor-el {
    /* background-color: chartreuse; */
    flex-grow: 1;
    z-index: 10000;
    max-width: 180px;
    max-height: 250px;
    width: 11vw;
    display: flex;
    justify-content: center;
    flex-direction: column;
    transform: translateY(10px);
}

.sponsor-el:hover{
    opacity: 0.7;
}

.sponsor-el * {
    max-width: 100%;
    max-height: 100%;
}

@media only screen and (max-height: 700px){
        #sponsors-bar{
            height:50px;
        }
    }

@media screen and (max-width: 650px) {
    #sponsors-bar {
        flex-direction: column;
    }

    .sponsor-el {
        flex-wrap: wrap;
        width: 20vw;
    }
}

@media screen and (max-width: 850px) {

    #sponsors-bar{
        height: 100px;
    }

    .info-section-hr {
        display: none;
    }

    #plan-para {
    margin-right: 0px;
}

    #date-hr{
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

    .sponsors section .spacefiller-phone{
        display:flex
    }

    #qsn-img{
        padding: 0;
    }

    .comite-line {
        width: 100% !important;
    }

    .comite-section-hr{
        max-width: 330px;
    }

    .comite-member {
        width: 49% !important;
    }

    .comite-member p {
        padding-bottom: 4px;
}

    .home-screen-bg{
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