<script setup></script>

<template>
  <div>
    <div class="apropos">
      <h1 class="large-title">Sysmic Festival</h1>

      <!-- Qui sommes-nous -->
      <h2 class="section-title">Qui sommes-nous ?</h2>
      <div class="board">
        <div class="texts">
          <p class="info-box" style="--x:-20px; --r:-1deg">
            Sysmic est constitué d’un comité de 31 personnes de toutes années et
            sections confondues. Nous travaillons tout au long de l’année afin
            d’offrir aux élèves de l’EPFL un festival de musique d’une soirée au
            sein même du campus.
          </p>
          <p class="info-box" style="--x:40px; --r:1.2deg">
            Originellement, l’association est dédiée à la section de
            Microtechnique pour laquelle nous organisons, en parallèle du
            festival, un apéro !
          </p>
          <p class="info-box" style="--x:0px; --r:-1.5deg">
            Notre plus grande qualité se trouve dans notre détermination à faire
            de Sysmic l’un des meilleurs festivals estudiantins du campus.
          </p>
          <p class="info-box" style="--x:30px; --r:1deg">
            Le comité Sysmic est cette année prêt à tout donner pour t’assurer
            la meilleure expérience possible !
          </p>
        </div>
        <img
          class="photo"
          src="@/assets/images/PhotoGallery/qui-sommes-nous-img.jpg"
        />
      </div>

      <!-- Que faisons-nous -->
      <h2 class="section-title">Que faisons nous ?</h2>
      <div class="board board-reverse">
        <div class="texts">
          <p class="info-box" style="--x:25px; --r:1deg">
            Sysmic est un festival annuel qui se déroule vers le début du mois
            de novembre, marquant la dernière étape du premier semestre. Nous
            proposons plusieurs scènes, des bars, des stands de nourriture, mais
            ce qui nous distingue avant tout des autres festivals sur le campus,
            c'est la présence de salles d'Escape Game !
          </p>
          <p class="info-box" style="--x:-30px; --r:-1.2deg">
            De plus, tu as également la possibilité de nous retrouver lors
            d'autres événements tout au long de l'année. En effet, nous tenons
            régulièrement des stands à Balélec, Vivapoly, etc. En 2022, nous
            avons même organisé un tremplin pour la première fois, offrant ainsi
            de nouvelles opportunités.
          </p>
        </div>
        <img
          class="photo"
          src="@/assets/images/PhotoGallery/que-faisons-nous.jpg"
        />
      </div>

      <!-- Prévention -->
      <h2 class="section-title">Prévention</h2>
      <div class="board">
        <div class="texts">
          <p class="info-box" style="--x:-15px; --r:-1deg">
            Nous cherchons continuellement à améliorer notre festival pour ses
            participant.es.
          </p>
          <p class="info-box" style="--x:35px; --r:1.2deg">
            Afin de s’assurer de leur bien-être en milieu festif nous avons
            décidé de prendre des mesures de prévention (sexualité, alcool,
            drogues) et adhérons désormais à la Charte Festiplus. Un stand de
            l’association Nightlife sera aussi présent sur notre site si tu as
            envie de discuter ou t’informer sur ces thématiques durant ta soirée
            !
          </p>
        </div>
        <img
          class="photo"
          src="@/assets/images/PhotoGallery/prevee.jpg"
        />
      </div>

      <!-- Recrutement -->
      <h2 class="section-title" id="recrutement">Comment nous rejoindre ?</h2>
      <div class="board board-reverse">
        <div class="texts">
          <p class="info-box" style="--x:20px; --r:1deg">
            Si tu veux nous aider à l’élaboration du Festival tu peux venir
            staffer chaque année pendant la semaine de montage du festival, et
            pendant la soirée !
          </p>
          <p class="info-box" style="--x:-25px; --r:-1.5deg">
            Si tu as envie de plus t’impliquer, chaque année après le festival a
            lieu notre Assemblée Générale où nous élisons le nouveau Comité de
            Direction. Cette année ce sera le dimanche 27 novembre à 18h,
            n’hésite pas à venir c’est ouvert à tous.te.s. Suite à ça le
            recrutement du comité est annoncé par mail et sur nos réseaux
            sociaux.
          </p>
        </div>
        <img
          class="photo"
          src="@/assets/images/PhotoGallery/comment-nous-rejoindre.jpg"
        />
      </div>

      <!-- Statuts -->
      <h2 class="section-title">Statuts</h2>
      <div class="board">
        <p class="info-box" style="--x:0px; --r:1deg">
          Si tu aimes la lecture, nos statuts sont disponibles
          <a
            class="link-box"
            href="/text/SYSMIC_Statuts_2022.pdf"
            target="_blank"
            >ici →</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.apropos {
  width: 100%;
  margin-top: calc(var(--navbar-height) + var(--global-margin));
  padding-bottom: 80px;
}

/* big title: white block */
.large-title {
  display: block;
  width: fit-content;
  max-width: 90%;
  margin: 0 auto 60px;
  padding: 10px 40px;
  background: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  font-size: 5rem;
  font-weight: bold;
  letter-spacing: -0.02em;
  text-align: center;
}

/* section titles: blue blocks */
.section-title {
  display: block;
  width: fit-content;
  max-width: 90%;
  margin: 70px auto 30px;
  padding: 6px 26px;
  background: #0037ff;
  color: #fff;
  border-radius: 0;
  font-size: 2.2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  text-align: center;
  scroll-margin-top: calc(var(--navbar-height) + 20px);
}

/* text + photo always side by side on desktop */
.board {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  align-items: center;
  gap: 2rem 3rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 25px;
  box-sizing: border-box;
}

/* photo on the left instead of the right */
.board-reverse {
  grid-template-columns: 1fr 1.3fr;
}
.board-reverse .photo {
  order: -1;
}

.texts {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  min-width: 0;
}

.photo {
  width: 100%;
  height: auto;
  border: 2px solid #000;
  border-radius: 0;
}

/* blue text boxes: offset, tilted, squashed */
.info-box {
  margin: 0;
  padding: 14px 22px;
  background: #0037ff;
  color: #fff;
  border-radius: 0;
  font-size: 1.2rem;
  line-height: 1.5;
  text-align: left;
  text-justify: auto;
  letter-spacing: -0.02em;
  transform: translateX(var(--x, 0)) rotate(var(--r, 0deg)) scaleY(0.8);
}


/* link as a small white block inside the blue one */
.link-box {
  display: inline-block;
  margin-left: 10px;
  padding: 0 10px;
  background: #fff;
  color: #000;
  text-decoration: none;
}
.link-box:hover {
  background: #000;
  color: #fff;
}

@media only screen and (max-width: 850px) {
  .large-title {
    font-size: 2.6rem;
    padding: 8px 20px;
    margin-bottom: 40px;
  }
  .section-title {
    font-size: 1.6rem;
    margin-top: 50px;
  }
  .board,
  .board-reverse {
    flex-direction: column;
    padding: 0 15px;
  }
  .info-box {
    font-size: 1.05rem;
    padding: 10px 16px;
    transform: translateX(calc(var(--x) * 0.3)) rotate(var(--r)) scaleY(0.8);
  }
}
</style>