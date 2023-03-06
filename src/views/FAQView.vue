<script setup>
import FAQRow from '../components/FAQRow.vue';



</script>

<template>
  <div>
    <div class="faq-div">
      <section>

        <hr class="title-hr">
        <h1>FAQ</h1>
        <hr class="title-hr">

        <h4>Infos utiles et réponses aux questions fréquemment posées</h4>


        <h2>Le festival</h2>

        <FAQRow title="Y a-t-il un vestiaire ?">
          Durant le festival, nous mettons à votre disposition un vestiaire gratuit. Nous
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

        <FAQRow title="Puis-je venir au festival sans prélocation?">
          Évidemment ! Nous vendons également plus de 100 places de plus le soir même du
          festival, il n'y a pas de raison de ne pas venir à Sysmic ! <br><br>
          Nous conseillons toutefois de posséder une prélocation, afin d'éviter du temps d'attente.
        </FAQRow> 

        <FAQRow title="Puis-je manger sur place ?">
          Bien sûr ! Notre festival accueillera un foodtruck et un stand de nourriture servant de la nourriture de
          qualité à prix étudiant.
        </FAQRow> 

        <FAQRow title="Quelles activités sont prévues durant la soirée ?">
          En plus des concerts, des bars et du foodtruck, nos proposons deux escape games
          spécialement conçus par notre comité dans le thème de la soirée. Nous mettons également en place un espace
          "Just Dance".
        </FAQRow> 

        <FAQRow title="Le festival est-il accessible aux personnes à mobilité réduite?">
          L'ensemble du festival n'est pas accessible aux personnes à mobilité réduite. <br>
          Comme nous traitons chaque cas séparément, merci de nous contacter à <a
          href="mailto:contact@sysmic.ch">contact@sysmic.ch</a>
        </FAQRow> 

        <FAQRow title="Quels bâtiments seront fermés durant le festival ?">
          Les bâtiments CH, BS, CE, CM, CO, BM et BP seront impactés par le festival. Des affiches
          seront placées à l'entrée de ces bâtiments pour annoncer les heures exactes de fermeture.
        </FAQRow> 

        <hr>

        <h2 id="micros">Pour les micros</h2> 

        <FAQRow title="Comment se déroule la soirée avec une prélocation pour microtechnicien?">
          18:00 - Début de l'apéritif en CM 1 120 <br> 19:00 - Début du
          repas à l'Alpine
           <br> 21:00 - Spectacle en CE6 <br> 22:00 -
          Entrée dans le festival 🎉
          
        </FAQRow> 

        <FAQRow title="Quelles sont les horaires de ventes pour microtechnicien?">
         Dernières ventes, toutes années confondues : vendredi 14 dès 12h devant la salle Polyvalente, toute l'après-midi.
         <br><br>
         Prix: 30.- <br>
         Payement par cash uniquement, camipro obligatoire lors du règlement. Une personne peut prendre une place pour une autre en nous communiquant sont sciper et en payant pour elle.
        </FAQRow> 

        <hr>

        <h2>L'association</h2>

        <FAQRow title="Comment nous contacter ?">
          Par mail, de préférence, à l'adresse suivante : <a href="mailto:contact@sysmic.ch">contact@sysmic.ch</a>
          <span style="display:block ; margin-bottom:0.4em"></span>
          En cas de problème de source informatique (par exemple sur le site), tu peux nous contacter directement
          à l'adresse suivante : <a href="mailto:webmaster@sysmic.ch">webmaster@sysmic.ch</a>
          <span style="display:block ; margin-bottom:0.4em"></span>
          Tu peux aussi nous contacter via nos réseaux sociaux principaux <a
          href="https://www.facebook.com/sysmic2021/">Facebook</a> et <a
          href="https://www.instagram.com/festival_sysmic/">Instagram</a>
          <span style="display:block ; margin-bottom:0.4em"></span>
          Nous possédons également une case postale : <b>Sysmic, EPFL-STI-BM, Station 17, 1015 Lausanne</b>
        </FAQRow> 

        <FAQRow title="Comment faire partie de Sysmic ?">
          Si tu veux nous aider à l’élaboration du Festival tu peux venir staffer chaque années pendant la semaine de montage du festival, et pendant la soirée! !
            <br><br>
            Si tu as envie de plus t’impliquer, chaque année après le festival a lieu notre Assemblée Générale où nous élisons le nouveau Comité de Direction. Cette année ce sera le dimanche 27 novembre à 18h, n’hésite pas à venir c’est ouvert à tous.te.s. Suite à ça le recrutement du comité est annoncé par mail et sur nos réseaux sociaux.
            <br><br>
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

.mail-link :hover{
  text-decoration: underline;
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

  .faq-div section{
    margin: 10px;
  }

  .title-hr{
    max-width: 250px
  }

  section hr{
    max-width: 320px;
  }

}

</style>