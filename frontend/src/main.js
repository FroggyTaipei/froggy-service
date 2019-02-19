import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import UUID from 'vue-uuid'
import VueAnalytics from 'vue-analytics'
import VueRaven from 'vue-raven'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/zh-TW'
import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/theme-chalk/display.css'
import App from '@/App.vue'
import moment from 'moment'
import VueLazyload from 'vue-lazyload'
import { ServerTable } from 'vue-tables-2'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faAngleDoubleDown, faHome, faVolumeUp, faVolumeOff } from '@fortawesome/free-solid-svg-icons'
import { faGithub } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
window.axios = require('axios')

Vue.config.productionTip = false
Vue.prototype.$moment = moment

library.add([faAngleDoubleDown, faGithub, faHome, faVolumeUp, faVolumeOff])
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueAxios, axios)
Vue.use(UUID)
Vue.use(ServerTable)
Vue.use(ElementUI, { locale })

Vue.use(VueLazyload, {
  preLoad: 1.3,
  // error: 'https://cdn0.iconfinder.com/data/icons/shift-free/32/Error-128.png',
  loading: require('@/assets/images/loading.gif'),
  attempt: 1
})

// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production' && process.env.VUE_APP_SENTRY_PUBLIC_DSN) {
  Vue.use(VueRaven, { dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN })
}

// more info: https://github.com/MatteoGabriele/vue-analytics
if (process.env.NODE_ENV === 'production' && process.env.VUE_APP_GOOGLE_ANALYTICS) {
  Vue.use(VueAnalytics, {
    id: process.env.VUE_APP_GOOGLE_ANALYTICS,
    router
  })
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
