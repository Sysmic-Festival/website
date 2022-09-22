<script setup>
import { reactive } from 'vue'

defineProps(["displayed"])
const emit = defineEmits(["displayedUpdated"])

const state = reactive({
    currentPlayer: "",
})

function backdropClicked(e) {
    state.currentPlayer = ""
    emit('displayedUpdated', false)
}

</script>

<template>
    <div>
        <Teleport to="body">
            <div id="modal-container" v-if="displayed">
                <div id="modal-backdrop" @click="backdropClicked"></div>
                <section id="modal">
                    <div id="top-row">
                        <div v-if="state.currentPlayer === 'soundclound-single'">
                            <iframe width="100%" height="160" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1117717057&color=%2300ff2a&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=true">
                            </iframe>
                        </div>
                        <div v-if="state.currentPlayer === 'spotify'">
                            <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3Rmd1w81IxjgWKMeFhgNEn?utm_source=generator" width="100%" height="160" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                        </div>
                        <div v-if="state.currentPlayer === 'soundcloud-playlist'">
                            <iframe width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/156877674&color=%23ff5500&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=true"></iframe>
                        </div>
                    </div>
                    <div id="bottom-row">
                        <div @click="state.currentPlayer = 'soundclound-single'" class="artistButton">
                            <div>pHOTO du DuDe</div>
                            <p>Soundcloud Single</p>
                        </div>
                        <div @click="state.currentPlayer = 'spotify'" class="artistButton">
                            <div>pHOTO du DuDe</div>
                            <p>Spotify</p>
                        </div>
                        <div @click="state.currentPlayer = 'soundcloud-playlist'" class="artistButton">
                            <div>pHOTO du DuDe</div>
                            <p>Soundcloud Playlist</p>
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
    z-index: 10000;
    background-color: grey;
    border: 2px solid white;

    max-width: 80vw;
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
    background-color: rgb(68, 68, 68);
}

.artistButton > div {
    height: 150px;
    width: 150px;
    background-color: lightgray;
}

.artistButton > p {
    text-align: center;
}
</style>