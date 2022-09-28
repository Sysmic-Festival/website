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
                            <iframe class="player-ui" width="100%" height="160" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1117717057&color=%2300ff2a&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false">
                            </iframe>
                        </div>
                        <div v-if="state.currentPlayer === 'spotify'">
                            <iframe class="player-ui" src="https://open.spotify.com/embed/track/3Rmd1w81IxjgWKMeFhgNEn?utm_source=generator" width="100%" height="160" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                        </div>
                        <div v-if="state.currentPlayer === 'soundcloud-playlist'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/156877674&color=%23ff5500&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false"></iframe>
                        </div>
                        <div v-if="state.currentPlayer === 'spotify-playlist'">
                            <iframe class="player-ui" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/4XtQpWbRLKrxa3mbJDxSZD?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                        </div>

                    </div>
                    <div id="bottom-row">
                        <div @click="state.currentPlayer = 'soundclound-single'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Soundcloud Single</p>
                        </div>
                        <div @click="state.currentPlayer = 'spotify'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Spotify</p>
                        </div>
                        <div @click="state.currentPlayer = 'soundcloud-playlist'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Soundcloud Playlist</p>
                        </div>
                        <div @click="state.currentPlayer = 'spotify-playlist'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Spotify Playlist</p>
                        </div>
                    </div>
                    <div id="bottom-row">
                        <div @click="state.currentPlayer = 'soundclound-single'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Soundcloud Single</p>
                        </div>
                        <div @click="state.currentPlayer = 'soundclound-single'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Soundcloud Single</p>
                        </div>
                        <div @click="state.currentPlayer = 'spotify'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
                            <p>Spotify</p>
                        </div>
                        <div @click="state.currentPlayer = 'soundcloud-playlist'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/comite/absent.jpg"></div>
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
    align-self: center;
    padding: 25px;
    z-index: 10000;
    background-color: var(--secondary);
    box-shadow: 0px 0px 30px 20px rgba(0,0,0,.1);
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

.artistButton > div > img{
    height: 140px;
    width: 140px;
}

.artistButton > p {
    text-align: center;
    color: var(--primary);
    margin-top:0;
    margin-bottom:10px;
    
}

.player-ui{
    height:300px;
}


@media only screen and (max-width: 850px){

    #bottom-row{
        /* flex-direction: column; */
        flex-wrap: wrap;
    }

    .artistButton{
        flex-direction: row;
        width: 30%;
        padding-left: 0;
    }


    .artistButton > div > img{
        height: 40px;
        width: 40px;
        padding-right: 10px;

    }


}

</style>