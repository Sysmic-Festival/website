<script setup>
    import { RouterLink, RouterView } from 'vue-router'
    import NavBar from './components/NavBar.vue'
    import Timer from './components/Timer.vue';
    import Footer from './components/Footer.vue';
    import Sidemenu from './components/Sidemenu.vue';
    import Slideshow from './components/Slideshow.vue';
    import AnimatedLogo from './components/AnimatedLogo.vue';

    function togglePuce(that){
        console.log("CLICKED")
        var plus = that.children[0];
        var minus = that.children[1];

        var content = that.children[3];

        content.classList.toggle("opened");

        if(content.clientHeight < content.scrollHeight){

          plus.style.display = "none";
          minus.style.display = "inline-block";

        }else{

          minus.style.display = "none";
          plus.style.display = "inline-block";

    }

}

</script>

<template>
    <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet'>
    <div>
        <NavBar />
        <br><br><br><br>
        <p>je suis le portfoio</p>
    </div>

</template>


<style >

    .bar-menu li{
        display: none;
    }

    #navbar{
        position: fixed !important;
        top: 0 !important;
    }

</style>

<style scoped>

</style>