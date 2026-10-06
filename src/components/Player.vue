<script setup>
import { reactive } from "vue";

defineProps(["displayed"]);
const emit = defineEmits(["displayedUpdated"]);

const state = reactive({
  currentPlayer: "",
});

function backdropClicked(e) {
  state.currentPlayer = "";
  emit("displayedUpdated", false);
}
</script>

<template>
  <div>
    <Teleport to="body">
      <div id="modal-container" v-if="displayed">
        <div id="modal-backdrop" @click="backdropClicked"></div>
        <section id="modal">
          <div id="top-row">
            <div v-if="state.currentPlayer === 'player1'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/playlist/37i9dQZF1E4xmFTrdt6YVF?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>
            <div v-if="state.currentPlayer === 'player2'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO097phG?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>
            <div v-if="state.currentPlayer === 'player3'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO3UtSB2?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>
            <div v-if="state.currentPlayer === 'player4'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/album/7INLeFGVmRkHQcukM4nuKt?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>

            <div v-if="state.currentPlayer === 'player5'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/playlist/37i9dQZF1E4v9UkbXR0w6B?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>
            <div v-if="state.currentPlayer === 'player6'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/playlist/37i9dQZF1E4vdp4avdwNly?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>
            <div v-if="state.currentPlayer === 'player7'">
              <iframe
                style="border-radius: 12px"
                src="https://open.spotify.com/embed/playlist/37i9dQZF1E4z053PtoHKGK?utm_source=generator"
                width="100%"
                height="352"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
              ></iframe>
            </div>
          </div>
          <div id="bottom-row">
            <div @click="state.currentPlayer = 'player1'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/parsimony.jpg"
                />
              </div>
              <p>Parsimony</p>
            </div>
            <div @click="state.currentPlayer = 'player2'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/sheng.jpg"
                />
              </div>
              <p>Sheng</p>
            </div>
            <div @click="state.currentPlayer = 'player3'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/lebard.webp"
                />
              </div>
              <p>Le Bard</p>
            </div>
            <div @click="state.currentPlayer = 'player4'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/lakeouaaah.png"
                />
              </div>
              <p style="font-size: 10pt">Lake & OUAAHH</p>
            </div>
          </div>
          <div id="bottom-row">
            <div @click="state.currentPlayer = 'player5'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/neuns.jpg"
                />
              </div>
              <p>Neun's</p>
            </div>
            <div @click="state.currentPlayer = 'player6'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/yenkov.jpg"
                />
              </div>
              <p>Yenkov</p>
            </div>
            <div @click="state.currentPlayer = 'player7'" class="artistButton">
              <div>
                <img
                  class="artist-img"
                  src="@/assets/images/artists/dinaMDN.jpg"
                />
              </div>
              <p>Dina MDN</p>
            </div>
          </div>
        </section>
      </div>
    </Teleport>
  </div>
</template>

<style scoped>
#modal-container {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100vw;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#modal-backdrop {
  position: absolute;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100vw;
  background-color: rgba(0, 0, 0, 0.517);
  z-index: 1000;
}

#modal {
  align-self: center;
  padding: 15px;
  z-index: 10000;
  background-color: var(--secondary);
  box-shadow: 0px 0px 30px 20px rgba(0, 0, 0, 0.1);
  max-width: 80vw;
  border-radius: 20px;
}

#bottom-row {
  display: flex;
  justify-content: space-around;
}

.artistButton {
  cursor: pointer;
  padding: 3px;
  padding-left: 30px;
  padding-right: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.artistButton:hover {
  opacity: 0.8;
}

.artistButton > div > img {
  height: 140px;
  width: 140px;
}

.artistButton > p {
  text-align: center;
  color: var(--grey-white);
  margin-top: 0;
  margin-bottom: 10px;
  max-width: 150px;
}

.player-ui {
  height: 285px;
}

#top-row {
  padding-bottom: 15px;
}

@media only screen and (max-height: 700px) {
  #bottom-row {
    /* flex-direction: column; */
    flex-wrap: wrap;
  }

  .artistButton {
    flex-direction: row;
    width: 38%;
    padding-left: 0;
  }

  .artistButton > div > img {
    height: 40px;
    width: 40px;
    padding-right: 10px;
  }

  .artistButton > p {
    text-align: left;
  }
}

@media only screen and (max-width: 850px) {
  #bottom-row {
    /* flex-direction: column; */
    flex-wrap: wrap;
  }

  .artistButton {
    flex-direction: row;
    width: 38%;
    padding-left: 0;
  }

  .artistButton > div > img {
    height: 40px;
    width: 40px;
    padding-right: 10px;
  }

  .artistButton > p {
    text-align: left;
  }
}
</style>
