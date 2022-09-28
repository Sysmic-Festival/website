<script setup>

</script>

<template>
  <div>
    <div class="faq-div">
      <section>

        <hr class="title-hr">
        <h1>FAQ</h1>
        <hr class="title-hr">

        <h4>Infos utiles et réponses aux questions fréquemment posées</h4>
        <p style="color:red; text-align:center">Certaines informations peuvent être obsolète pour le festival à venir
          (21.10.2022) et peuvent donc être sujettes à changements, marquées d'un "&#9888"</p>
        <hr>

        <h2>Le festival</h2>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle"><span>Où</span> et <span>quand</span> se déroule le prochain festival ?</p>
          <p class="openableContent">Le prochain festival se déroulera le 21 octobre 2022, dans le bâtiment CE de
            l'EPFL. Entrées le long de l'avenue Piccard.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Y a-t-il un <span>vestiaire</span> ?</p>
          <p class="openableContent">Durant le festival, nous mettons a votre disposition un vestiaire gratuit. Nous
            déclinons toutefois toute responsabilité en cas de perte ou de vol.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Existe-il des <span>navettes</span> pour le retour ? <span
              style="color:red "><b>&#9888</b></span></p>
          <p class="openableContent">Oui! En plus des transports en commun normaux, il y aura des navettes spéciales.
            <br>
            Elles partiront à 02:15 et 03:15 de l'arrêt Piccard (directement à la sortie du festival) et passant par
            Renens-Gare, Malley et Lausanne-Flon ainsi que tous les principaux arrêts de bus sur le chemin.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Les <span>sacs</span> sont-ils autorisés ?</p>
          <p class="openableContent">Malheureusement, pour des raisons de sécurité, nous n'acceptons pas les sacs lors
            de la manifestation. Nous vous prions de venir sans sac à dos.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Comment puis-je obtenir des <span>prélocations</span> ? <span
              style="color:red "><b>&#9888</b></span></p>
          <p class="openableContent">Les prélocations seront mises en vente sur l'esplanade lors de la semaine précédent
            le festival, de 12:00 à 13:15, le mercredi et le jeudi</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Quelles sont les mesures concernant le <span>Coronavirus</span> ? <span
              style="color:red "><b>&#9888</b></span></p>
          <p class="openableContent">1. L'accès au festival <span>n'est plus</span> réservé aux personnes possédant un
            certificat COVID valable.<br>
            2. Il est tout de même interdit de venir à la manifestation en cas de symptômes d'une infection. <br>
            3. Du gel hydroalcoolique sera mis à disposition à l'extérieur et dans le festival. Les surfaces fréquemment
            utilisées (bar, etc.) seront désinfectées régulièrement.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Puis-je venir au festival <span>sans prélocation</span> ? <span
              style="color:red "><b>&#9888</b></span></p>
          <p class="openableContent">Évidemment ! Nous vendons également plus de 100 places de plus le soir même du
            festival, il n'y a pas de raison de ne pas venir à Sysmic ! <br><br>
            Nous conseillons toutefois de posséder une prélocation, afin d'éviter du temps d'attente.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Puis-je <span>manger</span> sur place ? <span style="color:red "><b>&#9888</b></span>
          </p>
          <p class="openableContent">Bien sûr ! Notre festival accueillera un foodtruck servant de la nourriture de
            qualité à prix étudiant.</p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Quelles <span>activités</span> sont prévues durant la soirée ?</p>
          <p class="openableContent">En plus des concerts, des bars et du foodtruck, nos proposons deux escape games
            spécialement conçues par notre comité dans le thème de la soirée. Nous mettons également en place un espace
            "Just Dance".</p>
        </div>


        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg">
          <img class="plus" src="@/assets/images/utilitaries/plus.svg">
          <p class="openableTitle">Le festival est-il accessible aux personnes à <span>mobilité réduite</span> ?</p>
          <p class="openableContent">L'ensemble du festival n'est pas accessible aux personnes à mobilité réduite. <br>
            Comme nous traitons chaque cas séparément, merci de nous contacter à <a
              href="mailto:contact@sysmic.ch">contact@sysmic.ch</a></p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Quels <span>bâtiments seront fermés</span> durant le festival ?</p>
          <p class="openableContent">Les bâtiments CE, CM, CO, BM et BP seront impactés par le festival. Des affiches
            seront placées à l'entrée de ces bâtiments pour annoncer les heures exactes de fermeture.</p>
        </div>
        <hr>

        <h2>Pour les micros</h2>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Comment se déroule la soirée avec une <span>prélocation pour microtechnicien</span> ?
            <span style="color:red "><b>&#9888</b></span></p>
          <p class="openableContent">18:00 - Début de l'apéritif (emplacement bientôt annoncé) <br> 19:00 - Début du
            repas au Native (ex Vinci, même sas d'entrée que Satellite) <br> 21:00 - Spectacle en CE6 <br> 22:00 -
            Entrée dans le festival 🎉</p>
        </div>
        <hr>

        <h2>L'association</h2>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Comment nous <span>contacter</span> ?</p>
          <p class="openableContent">
            Par mail, de préférence, à l'adresse suivante : <a href="mailto:contact@sysmic.ch">contact@sysmic.ch</a>
            <span style="display:block ; margin-bottom:0.4em"></span>
            En cas de problème de source informatique (par exemple sur le site), vous pouvez nous contacter directement
            à l'adresse suivante : <a href="mailto:webmaster@sysmic.ch">webmaster@sysmic.ch</a>
            <span style="display:block ; margin-bottom:0.4em"></span>
            Tu peux aussi nous contacter via nos réseaux sociaux principaux <a
              href="https://www.facebook.com/sysmic2021/">Facebook</a> et <a
              href="https://www.instagram.com/festival_sysmic/">Instagram</a>
            <span style="display:block ; margin-bottom:0.4em"></span>
            Nous possédons également une case postale : <b>Sysmic, EPFL-STI-BM, Station 17, 1015 Lausanne</b>
          </p>
        </div>

        <div class="container" @click="togglePuce(this)">
          <img class="minus" src="@/assets/images/utilitaries/minus.svg" />
          <img class="plus" src="@/assets/images/utilitaries/plus.svg" />
          <p class="openableTitle">Comment faire partie de <span style="color:var(--second-light);">Sysmic</span> ?</p>
          <p class="openableContent">
            Chaque année, quelques temps après le festival, un communiqué passe sur <a
              href="https://www.facebook.com/sysmic2021/">Facebook</a> pour annoncer une assemblée générale durant
            laquelle les postes à pourvoir seront annoncés, et tu pourras te présenter.<br>
            Nous envoyons également un mail à tous les étudiants au même moment.
          </p>
        </div>

      </section>
    </div>
  </div>

</template>

<style scoped>
h1 {
  color: var(--white);
  margin: 0;
}

h2 {
  color: var(--secondary);
  text-align: center;
}

h4 {
  color: var(--secondary);
}

.title-hr {
  max-width: 200px;
}

.faq-div {
  margin: auto;
  margin-top: calc(2*var(--global-margin) + var(--navbar-height));
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

section hr {
  max-width: 800px;
  border: 1px solid var(--third);
}

.plus {
  display: inline-block;
}

.minus {
  display: none;
}

.openableContent {
  max-height: 0;
  padding-bottom: 0px;
  transform-origin: top;
  overflow: hidden;
  padding-left: 55px;
  transition: max-height 0.8s, padding-bottom 0.8s;
}

.opened {
  max-height: 200px;
  padding-bottom: 30px;
}

section div:hover img {
  fill: var(--second);
}

.openableTitle {
  padding-bottom: 20px;
}

.openableTitle:hover,
.openableTitle:hover span {
  color: var(--secondary);
}


span {
  color: var(--secondary);
}

.openableTitle:hover span {
  color: var(--third);
}


@media only screen and (max-width: 800px) {

  .openableTitle,
  .openableContent {
    font-size: 3.6vw;
    width: 85%;
  }

  .cacheBlack {
    width: 10%;
  }

  .opened {
    max-height: 500px;
    padding-bottom: 30px;
  }
}
</style>