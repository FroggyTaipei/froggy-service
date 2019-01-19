import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import UUID from 'vue-uuid'
import VueAnalytics from 'vue-analytics'
import VueRaven from 'vue-raven'
import ElementUI from 'element-ui'
import zh from 'element-ui/lib/locale/lang/zh-TW'
import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/theme-chalk/display.css'
import App from '@/App.vue'
import './registerServiceWorker'
import moment from 'moment'
import { ServerTable } from 'vue-tables-2'

Vue.use(ServerTable)
Vue.use(ElementUI, { zh })
Vue.use(UUID)

Vue.prototype.$moment = moment

Vue.config.productionTip = false

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
window.axios = require('axios')
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

// window.$ = require('jquery')
// window.JQuery = require('jquery')

// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production') {
  Vue.use(VueRaven, { dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN })
}

// more info: https://github.com/MatteoGabriele/vue-analytics
// Vue.use(VueAnalytics, {
//   id: process.env.VUE_APP_GOOGLE_ANALYTICS,
//   router
// })

document.getCookie = function (name) {
  var nameEQ = name + '='
  var ca = document.cookie.split(';')
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i]
    while (c.charAt(0) === ' ') c = c.substring(1, c.length)
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length)
  }
  return null
}

document.eraseCookie = function (name) {
  document.cookie = name + '=; Max-Age=-99999999;'
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
