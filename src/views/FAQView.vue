<script setup>
import FAQRow from "../components/FAQRow.vue";
</script>

<template>
  <div>
    <div class="faq-div">
      <section>
        <div class="title-small-line"></div>
        <hr class="title-hr" />
        <h1>FAQ</h1>
        <hr class="title-hr" />
        <div class="title-small-line"></div>

        <h4>Infos utiles et réponses aux questions fréquemment posées</h4>

        <h2>Le festival</h2>

        <FAQRow title="Y a-t-il un vestiaire ?">
          Oui ! Un vestiaire est disponible gratuitement, cependant nous
          déclinons toute responsabilité en cas de perte ou vol.
        </FAQRow>

        <FAQRow title="Existe-il des navettes pour le retour ?">
          Oui ! En plus des transports en commun normaux, il y aura des navettes
          gratuites. Elles partiront à 01:30, 02:30 et 03:15 de l'arrêt Piccard
          (directement à la sortie du festival).<br />
          <br />
          Les navettes desserviront :<br />
          Renens, Malley, le Flon.
        </FAQRow>

        <FAQRow title="Les sacs sont-ils autorisés ?">
          Non ! Malheureusement, pour des raisons de sécurité, nous n'acceptons
          pas les sacs dans l’enceinte de la manifestation. Nous vous prions de
          venir sans sac.
        </FAQRow>

        <FAQRow title="Comment puis-je obtenir un Ticket?">
          Les tickets seront mis en vente sur la place Ada Lovelace de l’EPFL durant la
          semaine précédant le festival, le mardi 4 novembre à 12:00.
        </FAQRow>

        <FAQRow title="Puis-je venir au festival sans prélocation?">
          Oui ! Nous vendons environ 100 tickets le soir du festival. Nous vous
          conseillons toutefois d’acheter un ticket durant les préventes, afin
          d'éviter toute attente ou déception.
        </FAQRow>

        <FAQRow title="Puis-je manger sur place ?">
          Oui ! Vous trouverez dans le festival deux stands de
          nourriture à prix étudiant.
        </FAQRow>

        <FAQRow title="Quelles activités sont prévues durant la soirée ?">
          En plus des concerts, des bars et des stands de nourriture, vous pourrez profiter
          d'un escape game dans le thème de la soirée, ainsi que d'une salle d'arcade et d'un stand de flocage. De plus, un espace
          dédié à "Just Dance" sera également à votre disposition.
        </FAQRow>

        <FAQRow
          title="Le festival est-il accessible aux personnes à mobilité réduite?"
        >
          Le festival n'est pas entièrement accessible aux personnes à mobilité
          réduite. Pour prendre en compte les besoins spécifiques de chaque
          personne, veuillez nous contacter à l'adresse
          <a href="mailto:contact@sysmic.ch">contact@sysmic.ch</a>
        </FAQRow>

        <FAQRow title="Quels bâtiments seront fermés durant le festival ?">
          Les bâtiments CH, BS, CE, CM, CO, BM et BP seront impactés par le
          festival. Des affiches vous informeront des horaires précises de
          fermeture et réouverture.
        </FAQRow>

        <div class="small-line"></div>
        <hr />

        <h2 id="micros">Pour les micros</h2>

        <FAQRow
          title="Comment se déroule la soirée avec une prélocation pour MT ?"
        >
          18:00 - Apéro dinatoire avec tes profs préférés (n'oublie pas ta
          camipro) <br />
          20h - Début du spectacle <br />
          21h - Fin du spectacle et direction le festival 🎉
        </FAQRow>

                <FAQRow
          title="Jusqu'à quelle heure puis-je entrer pour assister à la partie MT ?"
        >
          Il est possible d'entrer pour assister à la partie MT jusqu'à 19h. Au delà de cette heure, tu pourras rentrer uniquement via l'entrée principale et selon les conditions d'entrée correspondantes.
        </FAQRow>
        <!-- <FAQRow
          title="Quelles sont les horaires de ventes pour microtechnicien?"
        >
          BA1 : Mercredi 16 à 14h devant le CE16<br />
          BA3 : Jeudi 17 à 16h devant le CO1<br />
          BA5 : Vendredi 18 à 12h devant le CM13<br />
          Masters & retardataires : Vendredi 18 à 14h devant le local Sysmic
          CM0118
          <br /><br />
          Prix: 23.- <br />
          Payement par cash ou camipro, camipro obligatoire lors du règlement.
        </FAQRow> -->

        <hr />
        <div class="small-line"></div>

        <h2>L'association</h2>

        <FAQRow title="Comment nous contacter ?">
          Par mail, à l'adresse suivante :
          <a href="mailto:contact@sysmic.ch">contact@sysmic.ch</a> .<br />
          Sur Instagram @festival_sysmic .<br />
          Ou par courrier : Sysmic, EPFL-STI-BM, Station 17, 1015 Lausanne .
        </FAQRow>

        <FAQRow title="Comment faire partie de Sysmic ?">
          Si tu souhaites contribuer à l'organisation du Festival, tu as la
          possibilité de participer en tant que staff pendant la semaine de
          montage et/ou durant la soirée !<br />
          <br />
          Si tu as envie de t'impliquer davantage, notre Assemblée Générale a
          lieu chaque année après le festival, où nous élisons le nouveau Comité
          de Direction. Cette année, elle se tiendra le dimanche 27 novembre à
          18h. N'hésite pas à venir, car c'est ouvert à tous.tes. Par la suite,
          le recrutement du comité est annoncé par mail et sur nos réseaux
          sociaux.

          <!-- Le form de recrutement pour les posts à pourvoir est disponible <a href="/presentation posts.pdf" target="_blank" style="text-decoration: underline;">ici</a> ! -->
        </FAQRow>
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
  color: var(--white);
  text-align: center;
}

h4 {
  color: var(--grey-white);
}

.title-hr {
  max-width: 200px;
  border: 1px solid var(--blue);
}
.title-small-line {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  width: 50%;
  max-width: 100px;
  border: 1px solid var(--third);
}

.faq-div {
  margin: auto;
  margin-top: calc(2 * var(--global-margin) + var(--navbar-height));
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
  border: 1px solid var(--blue);
}
.small-line {
  margin-top: 15px;
  margin-bottom: 15px;
  margin-left: auto;
  width: 33%;
  border: 1px solid var(--third);
}

.plus {
  display: inline-block;
}

.minus {
  display: none;
}

.mail-link :hover {
  text-decoration: underline;
}

.openableContent {
  max-height: 0;
  padding-bottom: 0px;
  transform-origin: top;
  overflow: hidden;
  padding-left: 55px;
  transition:
    max-height 0.8s,
    padding-bottom 0.8s;
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
    font-size: 10p;
    width: 85%;
  }

  .cacheBlack {
    width: 10%;
  }

  .opened {
    max-height: 500px;
    padding-bottom: 30px;
  }

  .faq-div section {
    margin: 10px;
  }

  .title-hr {
    max-width: 250px;
  }

  section hr {
    max-width: 320px;
  }
}
</style>
