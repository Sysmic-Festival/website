import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomeView,
      name: 'home'
    },
    {
      path: '/about-us',
      component: () => import('../views/AboutUsView.vue')
    },
    {
      path: '/portfolio',
      component: () => import('../views/PortfolioView.vue')
    },
    {
      path: '/faq',
      component: () => import('../views/FAQView.vue')
    },
    {
      path: "/:pathMatch(.*)*",
      redirect: '/'
    }
  ],
  scrollBehavior: function (to) {
    if (to.hash && to.hash !== '#') {
      return {
        el: to.hash,
        top: to.hash === '#line-up' ? 0 : 100, // offset
        behavior: "smooth"
      }
    } else {
      return { top: 0 }
    }
  },
})

export default router
