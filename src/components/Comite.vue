<script setup>
    import { onMounted, reactive } from 'vue'
    
    const state = reactive({
      sticky: false,
      stickyPosition: 0,
      navbar: null,
      root: null
    })
    
    
    onMounted(() => {
      // When the user scrolls the page, execute myFunction
      window.onscroll = function() {onScroll()};
    
      // Get the navbar
      state.navbar = document.getElementById("comite-description");
      state.root = document.documentElement;
    
      // Get the offset position of the navbar
      state.stickyPosition = navbar.offsetTop;
    })
    
    // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
    // the minus part is so that the header sticks as soon as the top margin is reached, so it doesn't jump (removing the "px" from the margin)
    function onScroll() {
      if (state.navbar && window.pageYOffset >= state.stickyPosition) {
        state.sticky = true
      } else {
        state.sticky = false
      }
    }
    </script>

<template>

    <div id="comite-section">



    </div>

</template>