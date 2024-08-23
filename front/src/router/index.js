import { createRouter, createWebHistory } from 'vue-router'
import Main from '../views/Main.vue'
import Home from '@/views/Home.vue'
import Patients from '@/views/Patients.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'main', component: Main,
      children: [
        { path:'/', component: Home },
        { path:'patients', component: Patients },
        { path:'sessions', component: () => import('../views/Sessions.vue') },
        { path:'manage', component: () => import('../views/ManageProfile.vue') },
    ]},
    { path: '/login', name: 'login', component: () => import('../views/Login.vue') },
  ]
});

export default router
