<script setup>

    import {onMounted} from 'vue'
    onMounted(() => {
        animLogo(1);
    })


    function animLogo(id){
      try {
        id += Math.round((Math.random()))+1;
        document.getElementById("layer"+id).classList.toggle("invaderShow");
        setTimeout(animLogo, 200, id%18);
      } catch (error) {}
    }
    
</script>


<template>
  <section class="invaderSection">
    <!-- <div id="invaderDiv"> -->
      <!-- <img class="layer" id="layer1"  src="@/assets/images/layers/01.svg"/>
      <img class="layer" id="layer2"  src="@/assets/images/layers/02.svg"/>
      <img class="layer" id="layer3"  src="@/assets/images/layers/03.svg"/>
      <img class="layer" id="layer4"  src="@/assets/images/layers/04.svg"/>
      <img class="layer" id="layer5"  src="@/assets/images/layers/05.svg"/>
      <img class="layer" id="layer6"  src="@/assets/images/layers/06.svg"/>
      <img class="layer" id="layer7"  src="@/assets/images/layers/07.svg"/>
      <img class="layer" id="layer8"  src="@/assets/images/layers/08.svg"/>
      <img class="layer" id="layer9"  src="@/assets/images/layers/09.svg"/>
      <img class="layer" id="layer10" src="@/assets/images/layers/10.svg"/>
      <img class="layer" id="layer11" src="@/assets/images/layers/11.svg"/>
      <img class="layer" id="layer12" src="@/assets/images/layers/12.svg"/>
      <img class="layer" id="layer13" src="@/assets/images/layers/13.svg"/>
      <img class="layer" id="layer14" src="@/assets/images/layers/14.svg"/>
      <img class="layer" id="layer15" src="@/assets/images/layers/15.svg"/>
      <img class="layer" id="layer16" src="@/assets/images/layers/16.svg"/>
      <img class="layer" id="layer17" src="@/assets/images/layers/17.svg"/>
      <img class="layer" id="layer18" src="@/assets/images/layers/18.svg"/>
      <img class="layer" id="layer19" src="@/assets/images/layers/19.svg"/> -->
      <img class="layer"  src="@/assets/images/utilitaries/new-logo.svg"/>
    <div class="titleBox">
      <h1>SYSMIC<br>FESTIVAL</h1>
      <div id="title-date">
        <h2>1.11.24</h2>
      </div>
    </div>
  </section>
</template>


<style scoped>

h1, h2 {
    position: relative;
    bottom: -70px;
    margin: 0px;
    font-weight: extra;
}

.invaderSection {
  z-index: 1;
  flex-grow: 1;
  display: flex;
  justify-content: center;
  height: 50%;
}
.layer{
  position: absolute;
  filter: invert(100%) sepia(100%) saturate(1%) hue-rotate(226deg) brightness(105%) contrast(102%);
  top: calc(15% - 5vw);
  left: calc(20vw - 100px);
  height: 23vw;
  max-height: 60vh;
  max-width: 100%;
}

#invaderDiv{
  overflow:visible;
  position: absolute;
  left: 50%;
  transform: translateX(-80%);
  height: 50%;
  width: 800px;
}


#invaderDiv img{
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  transition: opacity, 1s;
  opacity: 0;
  height: 100%;
  max-width: 100%;
}
.titleBox {

  font-family: "Montserrat";
  line-height: 90pt;
  text-align: left;
  height: 200px;
  position: absolute;
  left: calc(50% - 50px);
  top: calc(30vh - 175px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
  margin-top: 30px;
  z-index: 1;
}

#title-date{
  transform: translateY(-30px);
}

.titleBox > h1{
  font-size: calc(60pt + 2vw);
  font-weight: 900;
  color: var(--white);
  /* font-family: Raleway-Light; */
}

.titleBox > div > h2 {
  display: ruby-text;
  font-size: 18pt;
  font-weight: 700;
  color: var(--white);
  background-color: transparent;
  text-align: center;
  vertical-align: top;
  position:relative;
  right: -0px;
}

.invaderShow{
  opacity: 1 !important;
}

@media only screen and (max-width: 850px){
  
  .invaderSection {
    flex-direction: column;
    align-items: center;
  }

  #invaderDiv {
    position: relative;
    transform: none;
    left: 0;
  }
  .layer{
  position: absolute;
  top:5%;
  left: calc(50% - 20.625vw);
  height: 30vw;
}

  .titleBox {
    line-height: 60pt;
    align-items: center;
    margin-left: 0; 
    height: auto;
    position: absolute;
    width: 60%;
    left: 20%;
    top: 32%;
  }

  h1,h2 {
    text-align: center;
    bottom: 0px;
  }

  .titleBox > h1{
    font-size: calc(6vh + 5vw);
    line-height: calc(8vh + 5vw);
  }

  .titleBox > div > h2 {
    font-size: 15pt;
    position:relative;
    right:0px;
    top: -20px;
  }

  #title-date{
    transform: translateY(0px);
  }

}
@media only screen and (max-width: 600px){
  .layer{
  left: calc(50% - 25vw);
  height: 40vw;
  }

}

@media only screen and (max-width: 450px){
  .layer{
  left: calc(50% - 30.1vw);
  height: 45vw;
  }


}

</style>