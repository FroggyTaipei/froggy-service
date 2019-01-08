import Vue from 'vue'
import store from '@/store'
import router from '@/router'

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios)

import VueAnalytics from 'vue-analytics'

// import VueRaven from 'vue-raven'

import App from '@/App.vue'
import './registerServiceWorker'

import 'bootstrap'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

import 'axios'

// import VueFullPage from 'vue-fullpage.js'
// Vue.use(VueFullPage);

Vue.config.productionTip = false

window.$ = require('jquery')
window.JQuery = require('jquery')

// Sentry for logging frontend errors
// if (process.env.NODE_ENV === 'production') {
//   Vue.use(VueRaven, { dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN })
// }

// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
