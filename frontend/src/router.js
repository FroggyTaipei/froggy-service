import Vue from 'vue'
import VueRouter from 'vue-router'

// import ExampleComponent from '@/components/ExampleComponent.vue'
import Home from '@/views/Home.vue'
// import Demo from '@/components/Demo.vue'
// import Demo1 from '@/components/SecondPage.vue'

const routes = [
  { path: '*', component: Home },
  // { path: '/demo1', component: SecondPage}
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
