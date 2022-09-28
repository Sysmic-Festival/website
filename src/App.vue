<script setup>
import { reactive } from 'vue';
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import NavBar from './components/NavBar.vue'

const router = useRouter();

const data = reactive({
  navBarFixed: false,
});

router.beforeEach(guard => {
  data.navBarFixed = guard.name !== 'home'
});

</script>

<template>
      <div>
        <NavBar :fixed="data.navBarFixed" />
        <RouterView></RouterView>
      </div>
</template>

<style scoped>

</style>
