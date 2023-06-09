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
      path: '/portfolio/2022',
      component: () => import('../components/portfolio_vues/2022.vue')
    },
    {
      path: '/portfolio/2021',
      component: () => import('../components/portfolio_vues/2021.vue')
    },
    {
      path: '/portfolio/2019',
      component: () => import('../components/portfolio_vues/2019.vue')
    },
    {
      path: '/portfolio/2018',
      component: () => import('../components/portfolio_vues/2018.vue')
    },
    {
      path: '/portfolio/2017',
      component: () => import('../components/portfolio_vues/2017.vue')
    },
    {
      path: '/portfolio/2016',
      component: () => import('../components/portfolio_vues/2016.vue')
    },
    {
      path: '/portfolio/2015',
      component: () => import('../components/portfolio_vues/2015.vue')
    },
    {
      path: '/portfolio/2014',
      component: () => import('../components/portfolio_vues/2014.vue')
    },
    {
      path: '/portfolio/2013',
      component: () => import('../components/portfolio_vues/2013.vue')
    },
    {
      path: '/portfolio/2012',
      component: () => import('../components/portfolio_vues/2012.vue')
    },
    {
      path: '/portfolio/2011',
      component: () => import('../components/portfolio_vues/2011.vue')
    },
    {
      path: '/portfolio/2010',
      component: () => import('../components/portfolio_vues/2010.vue')
    },
    {
      path: '/portfolio/2009',
      component: () => import('../components/portfolio_vues/2009.vue')
    },
    {
      path: '/portfolio/2008',
      component: () => import('../components/portfolio_vues/2008.vue')
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
