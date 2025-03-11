import { createRouter, createWebHistory } from 'vue-router'
import Error404 from '../views/Error404.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../views/HomeView.vue'),
      name: 'home',
    },
    {
      path: '/sobre_nosotros',
      component: () => import('../views/SobreNosotros.vue'),
      name: 'sobre_nosotros',
    },
    {
      path: '/:pathMatch(.*)*',
      component: Error404,
    }
  ],
})

export default router
