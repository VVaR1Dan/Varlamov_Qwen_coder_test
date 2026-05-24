<template>
  <div class="product-list">
    <h1>Список товаров</h1>
    
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else-if="products.length === 0" class="empty">Товаров пока нет</div>
    
    <div v-else class="products-grid">
      <div 
        v-for="product in products" 
        :key="product.id" 
        class="product-card"
        @click="goToProduct(product.id)"
      >
        <h3>{{ product.name }}</h3>
        <p class="price">{{ formatPrice(product.price) }} ₽</p>
        <p class="id">ID: {{ product.id }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const API_URL = 'http://localhost:8000'

const router = useRouter()
const products = ref([])
const loading = ref(true)
const error = ref(null)

const fetchProducts = async () => {
  try {
    const response = await axios.get(`${API_URL}/products`)
    products.value = response.data
  } catch (err) {
    error.value = 'Ошибка загрузки товаров: ' + err.message
  } finally {
    loading.value = false
  }
}

const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU').format(price)
}

const goToProduct = (id) => {
  router.push(`/product/${id}`)
}

onMounted(() => {
  fetchProducts()
})
</script>

<style scoped>
.product-list {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 2rem;
}

.loading, .error, .empty {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}

.error {
  color: #e74c3c;
}

.empty {
  color: #7f8c8d;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.product-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.product-card h3 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
}

.price {
  font-size: 1.5rem;
  font-weight: bold;
  color: #27ae60;
  margin: 0.5rem 0;
}

.id {
  color: #95a5a6;
  font-size: 0.9rem;
  margin: 0;
}
</style>
