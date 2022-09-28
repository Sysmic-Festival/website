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
    <div id="invaderDiv">
      <img class="layer" id="layer1"  src="@/assets/images/layers/01.svg"/>
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
      <img class="layer" id="layer19" src="@/assets/images/layers/19.svg"/>
    </div>
    <div class="titleBox">
      <h1>Sysmic <br>&nbsp Festival</h1>
      <div style="vertical-align:top">
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
  overflow:visible;
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
  
  line-height: 90pt;
  text-align: left;
  position: absolute;
  left: calc(50% - 50px);
  top: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
}

.titleBox > h1{
  font-size: 82pt;
  color: var(--white);
  /* font-family: Raleway-Light; */
}

.titleBox > div > h2 {
  display: ruby-text;
  font-size: 18pt;
  color: var(--white);
  background-color: transparent;
  text-align: center;
  vertical-align: top;
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
    line-height: 60pt;
    position: static;
    align-items: center;
    margin-left: 0; 
  }

  h1,h2 {
    text-align: left;
  }

  .titleBox > h1{
    font-size: 55pt;
  }

  .titleBox > div > h2 {
    font-size: 15pt;
  }

}

</style>