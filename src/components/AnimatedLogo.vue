<script setup>

    import {onMounted} from 'vue'
    onMounted(() => {
        animLogo(1);
    })


    function animLogo(id){
      id += Math.round((Math.random()))+1;
      document.getElementById("layer"+id).classList.toggle("invaderShow");
      setTimeout(animLogo, 200, id%18);
    }
    
</script>


<template>
  <section class="invaderSection">
    <div id="invaderDiv">
      <img id="layer1"  src="@/assets/images/layers/01.svg"/>
      <img id="layer2"  src="@/assets/images/layers/02.svg"/>
      <img id="layer3"  src="@/assets/images/layers/03.svg"/>
      <img id="layer4"  src="@/assets/images/layers/04.svg"/>
      <img id="layer5"  src="@/assets/images/layers/05.svg"/>
      <img id="layer6"  src="@/assets/images/layers/06.svg"/>
      <img id="layer7"  src="@/assets/images/layers/07.svg"/>
      <img id="layer8"  src="@/assets/images/layers/08.svg"/>
      <img id="layer9"  src="@/assets/images/layers/09.svg"/>
      <img id="layer10" src="@/assets/images/layers/10.svg"/>
      <img id="layer11" src="@/assets/images/layers/11.svg"/>
      <img id="layer12" src="@/assets/images/layers/12.svg"/>
      <img id="layer13" src="@/assets/images/layers/13.svg"/>
      <img id="layer14" src="@/assets/images/layers/14.svg"/>
      <img id="layer15" src="@/assets/images/layers/15.svg"/>
      <img id="layer16" src="@/assets/images/layers/16.svg"/>
      <img id="layer17" src="@/assets/images/layers/17.svg"/>
      <img id="layer18" src="@/assets/images/layers/18.svg"/>
      <img id="layer19" src="@/assets/images/layers/19.svg"/>
    </div>
    <div class="titleBox">
      <h1>Sysmic</h1>
      <div>
        <h2>Festival de la Microtechnique</h2>
        <h2>21.10.22</h2>
      </div>
    </div>
  </section>
</template>


<style scoped>

h1, h2 {
  margin: 0;
}

.invaderSection {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

#invaderDiv{
  position: absolute;
  left: 50%;
  transform: translateX(-80%);
  height: 50%;
  width: 500px;
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
  position: absolute;
  left: calc(50% - 40px);
  top: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
}

.titleBox > h1{
  font-size: 90pt;
  color: var(--third);
  /* font-family: Raleway-Light; */
}

.titleBox > div > h2 {
  font-size: 18pt;
  color: var(--third);
  background-color: transparent;
  text-align: center;
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

  .titleBox {
    position: static;
    align-items: center;
    margin-left: 0;
  }

  h1,h2 {
    text-align: center;
  }

  .titleBox > h1{
    font-size: 60pt;
  }

  .titleBox > div > h2 {
    font-size: 15pt;
  }

}

</style>