import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'

import App from './App.vue'

axios.defaults.baseURL= 'http://127.0.0.1:5000/'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.mount('#app')
