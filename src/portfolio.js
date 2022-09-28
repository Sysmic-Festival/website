import { createApp } from 'vue'
import Portfolio from './Portfolio.vue'
import router from './router'

import './assets/css/main.css'
import './assets/css/aqua.min.css'

const portfolio = createApp(Portfolio)

portfolio.use(router)
portfolio.mount('#portfolio')

