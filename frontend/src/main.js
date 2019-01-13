import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueAnalytics from 'vue-analytics'
import VueRaven from 'vue-raven'
import App from '@/App.vue'
import Vuelidate from 'vuelidate'
import './registerServiceWorker'
import 'bootstrap'
import moment from 'moment'
import {ServerTable, ClientTable, Event} from 'vue-tables-2'
Vue.use(ServerTable, {}, false, 'bulma');

Vue.prototype.$moment = moment

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
window.axios = require('axios');
Vue.use(VueAxios, axios)
Vue.use(Vuelidate)

Vue.config.productionTip = false

window.$ = require('jquery')
window.JQuery = require('jquery')

// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production') {
  Vue.use(VueRaven, { dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN })
}

// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})

Vue.filter('formatSize', function (size) {
  if (size > 1024 * 1024 * 1024 * 1024) {
    return (size / 1024 / 1024 / 1024 / 1024).toFixed(2) + ' TB'
  } else if (size > 1024 * 1024 * 1024) {
    return (size / 1024 / 1024 / 1024).toFixed(2) + ' GB'
  } else if (size > 1024 * 1024) {
    return (size / 1024 / 1024).toFixed(2) + ' MB'
  } else if (size > 1024) {
    return (size / 1024).toFixed(2) + ' KB'
  }
  return size.toString() + ' B'
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
