import Vue from 'vue'
import VueRouter from 'vue-router'

// import ExampleComponent from '@/components/ExampleComponent.vue'
import Home from '@/views/Home.vue'
import CaseListPage from '@/views/CaseListPage.vue'
import AboutPage from '@/views/AboutPage.vue'
import InputDialogPage from '@/views/InputDialogPage.vue'

import Table from '@/components/Table.vue'

const routes = [
  { path: '*', component: Home },
  { path: '/create', component: InputDialogPage },
  { path: '/cases', component: CaseListPage },
  { path: '/about', component: AboutPage },
  { path: '/table', component: Table }
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
