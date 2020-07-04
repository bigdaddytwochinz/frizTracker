import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  {
    path: '/',
    name: 'Home'
  },
  {
    path: '/about',
    name: 'About'
  },
  {
    path: '*',
    name: 'notFound'
  }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.name}.vue`)

  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
