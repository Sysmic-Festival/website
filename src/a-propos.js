import { createApp } from 'vue'
import Apropos from './Apropos.vue'
import router from './router'

import './assets/css/main.css'
import './assets/css/aqua.min.css'

const apropos = createApp(Apropos)

apropos.use(router)
apropos.mount('#a-propos')

