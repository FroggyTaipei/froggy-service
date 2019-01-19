import Vue from 'vue'
import VueRouter from 'vue-router'

// import ExampleComponent from '@/components/ExampleComponent.vue'
import Home from '@/views/Home.vue'
import CaseListPage from '@/views/CaseListPage.vue'
import AboutPage from '@/views/AboutPage.vue'

const routes = [
  { path: '*', component: Home },
  { path: '/cases', component: CaseListPage },
  { path: '/about', component: AboutPage }
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
