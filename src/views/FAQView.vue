<script setup>
import FAQRow from "../components/FAQRow.vue";
</script>

<template>
  <div>
    <div class="faq-div">
      <section>
        <h1 class="faq-title-box">FAQ</h1>
        <h4 class="faq-subtitle">
          Infos utiles et réponses aux questions fréquemment posées
        </h4>

        <h2 class="pole-title">Le festival</h2>

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
          venir sans sac.
        </FAQRow>

        <FAQRow title="Comment puis-je obtenir un Ticket?">
          Les tickets seront mis en vente sur la place Ada Lovelace de l’EPFL
          durant la semaine précédant le festival.
        </FAQRow>

        <FAQRow title="Puis-je venir au festival sans prélocation?">
          Oui ! Nous vendons environ 100 tickets le soir du festival. Nous vous
          conseillons toutefois d’acheter un ticket durant les préventes, afin
          d'éviter toute attente ou déception.
        </FAQRow>

        <FAQRow title="Puis-je manger sur place ?">
          Oui ! Vous trouverez dans le festival deux stands de nourriture à prix
          étudiant.
        </FAQRow>

        <FAQRow title="Quelles activités sont prévues durant la soirée ?">
          En plus des concerts, des bars et des stands de nourriture, vous
          pourrez profiter d'escape games dans le thème de la soirée, ainsi que
          d'une salle d'arcade, de stands de craft, maquillage et de flocage. De
          plus, un espace dédié à "Just Dance" sera également à votre
          disposition.
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

        <h2 id="micros" class="pole-title">Pour les micros</h2>

        <FAQRow
          title="Comment se déroule la soirée avec une prélocation pour MT ?"
        >
          18:00 - Apéro dinatoire avec tes profs préférés (n'oublie pas ta
          camipro) <br />
          21h - Fin de l'apéro et direction le festival 🎉
        </FAQRow>

        <FAQRow
          title="Jusqu'à quelle heure puis-je entrer pour assister à la partie MT ?"
        >
          Il est possible d'entrer pour assister à la partie MT jusqu'à 19h. Au
          delà de cette heure, tu pourras rentrer uniquement via l'entrée
          principale et selon les conditions d'entrée correspondantes.
        </FAQRow>

        <h2 class="pole-title">L'association</h2>

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
          de Direction. N'hésite pas à venir, car c'est ouvert à tous.tes. Par
          la suite, le recrutement du comité est annoncé par mail et sur nos
          réseaux sociaux.
        </FAQRow>
      </section>
    </div>
  </div>
</template>

<style scoped>
.faq-div {
  margin: calc(2 * var(--global-margin) + var(--navbar-height)) auto 0;
  padding-bottom: 60px;
}

.faq-div section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* white title block */
.faq-title-box {
  width: fit-content;
  margin: 0 0 20px;
  padding: 8px 40px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  letter-spacing: -0.02em;
}

/* subtitle: blue block */
.faq-subtitle {
  width: fit-content;
  max-width: 90%;
  margin: 0 0 20px;
  padding: 10px 20px;
  background: #0037ff;
  color: #fff;
  text-align: center;
  font-size: 1.2rem;
}

/* section titles: blue blocks, same as the committee */
.pole-title {
  width: fit-content;
  margin: 50px 0 20px;
  padding: 6px 26px;
  background: #0037ff;
  color: #fff;
  border-radius: 0;
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  text-align: center;
  scroll-margin-top: calc(var(--navbar-height) + 20px);
}

/* disaligned rows (offset only, no tilt) */
.faq-div section > div:nth-of-type(odd) {
  transform: translateX(-30px);
}
.faq-div section > div:nth-of-type(even) {
  transform: translateX(30px);
}

@media only screen and (max-width: 800px) {
  .pole-title {
    font-size: 1.5rem;
    margin-top: 36px;
  }
  .faq-subtitle {
    font-size: 1rem;
  }
  .faq-div section > div:nth-of-type(odd) {
    transform: translateX(-8px);
  }
  .faq-div section > div:nth-of-type(even) {
    transform: translateX(8px);
  }
}
</style>