import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Welcome from '@/components/Welcome.vue'
import Patients from '@/views/Patients.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: Home,
      children: [
        { path:'/', component: Welcome },
        { path:'patients', component: Patients },
        { path:'sessions', component: () => import('../views/Sessions.vue') },
    ]},
    { path: '/login', name: 'login', component: () => import('../views/Login.vue') },
  ]
});

export default router
