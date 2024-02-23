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
                        <div v-if="state.currentPlayer === 'Von Bikräv'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1506591934&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-170567008" title="Mismic22" target="_blank" style="color: #cccccc; text-decoration: none;">Mismic22</a> · <a href="https://soundcloud.com/user-170567008/sets/jewel-usain" title="Von Bikrav" target="_blank" style="color: #cccccc; text-decoration: none;">Von Bikrav</a></div>                        
                        </div>
                        <div v-if="state.currentPlayer === 'Fluffy Machine'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1506590581&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-170567008" title="Mismic22" target="_blank" style="color: #cccccc; text-decoration: none;">Mismic22</a> · <a href="https://soundcloud.com/user-170567008/sets/fluffy-machine" title="Fluffy Machine" target="_blank" style="color: #cccccc; text-decoration: none;">Fluffy Machine</a></div>                        
                        </div>
                        <div v-if="state.currentPlayer === 'MEL'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1510700551&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-170567008" title="Mismic22" target="_blank" style="color: #cccccc; text-decoration: none;">Mismic22</a> · <a href="https://soundcloud.com/user-170567008/sets/mel" title="MEL" target="_blank" style="color: #cccccc; text-decoration: none;">MEL</a></div>                        
                        </div>
                        <div v-if="state.currentPlayer === 'High Salute b2b Radikal Vibration'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1506584944&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-170567008" title="Mismic22" target="_blank" style="color: #cccccc; text-decoration: none;">Mismic22</a> · <a href="https://soundcloud.com/user-170567008/sets/high-salute-b2b-radikal" title="High Salute b2b Radikal Vibration" target="_blank" style="color: #cccccc; text-decoration: none;">High Salute b2b Radikal Vibration</a></div>                        
                        </div>

                        <div v-if="state.currentPlayer === 'Roots Zombie'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1506586531&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-170567008" title="Mismic22" target="_blank" style="color: #cccccc; text-decoration: none;">Mismic22</a> · <a href="https://soundcloud.com/user-170567008/sets/roots-zombie" title="Roots Zombie" target="_blank" style="color: #cccccc; text-decoration: none;">Roots Zombie</a></div>
                        </div>
                        <div v-if="state.currentPlayer === 'Loudjack'">
                            <iframe class="player-ui" width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1506593185&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-170567008" title="Mismic22" target="_blank" style="color: #cccccc; text-decoration: none;">Mismic22</a> · <a href="https://soundcloud.com/user-170567008/sets/tremplin" title="Loudjack" target="_blank" style="color: #cccccc; text-decoration: none;">Loudjack</a></div>                        
                        </div>
                        <div v-if="state.currentPlayer === 'PlanH150'">
                            <iframe class="player-ui" width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1510646521&color=%237f5af0&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/plan-h150" title="PLAN H150" target="_blank" style="color: #cccccc; text-decoration: none;">PLAN H150</a> · <a href="https://soundcloud.com/plan-h150/sets/live-swisstech-village-2022" title="Live @ Swisstech Village 2022 - Part 1" target="_blank" style="color: #cccccc; text-decoration: none;">Live @ Swisstech Village 2022 - Part 1</a></div>
                        </div>
                        <div v-if="state.currentPlayer === 'Jewel Usain'">
                            <iframe class="player-ui" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO1aKR0s?utm_source=generator&theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>                  
                        </div>

                    </div>
                    <div id="bottom-row">
                        <div @click="state.currentPlayer = 'Von Bikräv'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/von-bikrav.jpg"></div>
                            <p>Von Bikräv</p>
                        </div>
                        <div @click="state.currentPlayer = 'Fluffy Machine'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/fluffy-machine.jpg"></div>
                            <p>Fluffy Machine</p>
                        </div>
                        <div @click="state.currentPlayer = 'MEL'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/mel.jpg"></div>
                            <p>MEL</p>
                        </div>
                        <div @click="state.currentPlayer = 'High Salute b2b Radikal Vibration'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/hsb2brv.jpg"></div>
                            <p style="font-size:10pt">High Salute b2b Radikal Vibration</p>
                        </div>
                    </div>
                    <div id="bottom-row">
                        <div @click="state.currentPlayer = 'Roots Zombie'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/roots-zombie.jpg"></div>
                            <p>Roots Zombie</p>
                        </div>
                        <div @click="state.currentPlayer = 'Loudjack'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/loudjack.jpg"></div>
                            <p>Loudjack</p>
                        </div>
                        <div @click="state.currentPlayer = 'PlanH150'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/planh150.jpg"></div>
                            <p>PlanH150</p>
                        </div>
                        <div @click="state.currentPlayer = 'Jewel Usain'" class="artistButton">
                            <div><img class="artist-img" src="@/assets/images/artists/jewel-usain.jpg"></div>
                            <p>Jewel Usain</p>
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
    color: var(--grey-white);
    margin-top:0;
    margin-bottom:10px;
    max-width: 150px;
}

.player-ui{
    height:285px;
}

#top-row{
    padding-bottom: 15px;
}

@media only screen and (max-height: 700px){
    #bottom-row{
        /* flex-direction: column; */
        flex-wrap: wrap;
    }

    .artistButton{
        flex-direction: row;
        width: 38%;
        padding-left: 0;
    }


    .artistButton > div > img{
        height: 40px;
        width: 40px;
        padding-right: 10px;

    }

    .artistButton > p{
        text-align: left;
    }
}

@media only screen and (max-width: 850px){

    #bottom-row{
        /* flex-direction: column; */
        flex-wrap: wrap;
    }

    .artistButton{
        flex-direction: row;
        width: 38%;
        padding-left: 0;
    }


    .artistButton > div > img{
        height: 40px;
        width: 40px;
        padding-right: 10px;

    }

    .artistButton > p{
        text-align: left;
    }

}

</style>