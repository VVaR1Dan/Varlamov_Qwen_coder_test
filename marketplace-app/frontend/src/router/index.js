import { createRouter, createWebHistory } from 'vue-router'
import ProductList from '../views/ProductList.vue'
import ProductEdit from '../views/ProductEdit.vue'
import ProductCreate from '../views/ProductCreate.vue'

const routes = [
  {
    path: '/',
    name: 'ProductList',
    component: ProductList
  },
  {
    path: '/product/:id',
    name: 'ProductEdit',
    component: ProductEdit,
    props: true
  },
  {
    path: '/create',
    name: 'ProductCreate',
    component: ProductCreate
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
