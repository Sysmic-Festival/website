import { createApp } from 'vue'
import FAQ from './FAQ.vue'
import router from './router'

import './assets/css/main.css'
import './assets/css/aqua.min.css'

const faq = createApp(FAQ)

faq.use(router)
faq.mount('#faq')

