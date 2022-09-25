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

            <h1 class="overInvaderH1">Sysmic</h1>
			<br>
			<h2 class="overInvaderH2">Festival de la Microtechnique</h2>
			<br>
			<h2 class="overInvaderH2">21.10.22</h2>
        </div>
    </section>

</template>


<style scoped>

.invaderShow{
  opacity: 1 !important;
}

#invaderDiv{
  position: relative;
  height: 450px;
  left: 0;
  margin-top: -35px;
}

#invaderDiv img{
  position: absolute;
  top:0;
  left:7%;
  transition: opacity, 1s;
  opacity : 0;
  width:65%;
}

.overInvaderH1{
  position: relative;
  display:inline-block;
  top: 70px;
  left: 290px;
  margin:0;
  font-size: 90pt;
  font-family: Raleway-Light;
  transition: text-shadow, 1s;
}
.overInvaderH1:hover{
  color: var(--primary-light);
}
.overInvaderH2{
  position: relative;
  display:inline-block;
  top: 70px;
  left: 320px;
  font-size: 18pt;
  color: var(--third);
  transition: text-shadow, 1s;
  background-color: transparent;
}
.overInvaderH2:hover{
  color: var(--third-light);
}

@media only screen and (max-width: 850px){
  #invaderDiv{
    left:0;
    margin-bottom: calc(-435px + 81vw);
    margin-top:0;
  }
  #invaderDiv img{
      left:50%;
      top:100px;
      transform: translateX(-50%);
      width:85vw;
  }

  .overInvaderH1{
      top:0;
      left:0;
      font-size: calc(17pt + 15vw);
  }
  .overInvaderH2{
      top:0;
      left:32px;
      font-size: calc(1pt + 3.4vw);
  }

}

.invaderSection{
    position: absolute;
    height: 80%;
}

</style>