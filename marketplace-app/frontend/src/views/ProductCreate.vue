<template>
  <div class="product-create">
    <h1>Создание нового товара</h1>
    
    <form @submit.prevent="createProduct" class="edit-form">
      <div class="form-group">
        <label for="name">Название *</label>
        <input 
          type="text" 
          id="name" 
          v-model="form.name" 
          required 
          placeholder="Введите название товара"
        />
      </div>
      
      <div class="form-group">
        <label for="price">Цена *</label>
        <input 
          type="number" 
          id="price" 
          v-model.number="form.price" 
          required 
          step="0.01"
          min="0"
          placeholder="Введите цену"
        />
      </div>
      
      <div class="form-row">
        <div class="form-group">
          <label for="color">Цвет</label>
          <input 
            type="text" 
            id="color" 
            v-model="form.color" 
            placeholder="Например: Белый"
          />
        </div>
        
        <div class="form-group">
          <label for="size">Размер</label>
          <input 
            type="text" 
            id="size" 
            v-model="form.size" 
            placeholder="Например: M, L, XL"
          />
        </div>
      </div>
      
      <div class="form-group">
        <label for="material">Материал</label>
        <input 
          type="text" 
          id="material" 
          v-model="form.material" 
          placeholder="Например: Хлопок, Металл"
        />
      </div>
      
      <div class="form-group">
        <label for="description">Описание</label>
        <textarea 
          id="description" 
          v-model="form.description" 
          rows="5"
          placeholder="Введите подробное описание товара"
        ></textarea>
      </div>
      
      <div class="form-actions">
        <button type="submit" :disabled="saving" class="btn-save">
          {{ saving ? 'Создание...' : 'Создать товар' }}
        </button>
        <button type="button" @click="cancel" class="btn-cancel">Отмена</button>
      </div>
      
      <div v-if="error" class="error-message">{{ error }}</div>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const API_URL = 'http://localhost:8000'

const router = useRouter()
const saving = ref(false)
const error = ref(null)

const form = reactive({
  name: '',
  price: 0,
  color: '',
  size: '',
  material: '',
  description: ''
})

const createProduct = async () => {
  saving.value = true
  error.value = null
  
  try {
    const response = await axios.post(`${API_URL}/products`, form)
    // После создания переходим на страницу редактирования созданного товара
    router.push(`/product/${response.data.id}`)
  } catch (err) {
    error.value = 'Ошибка создания товара: ' + err.message
  } finally {
    saving.value = false
  }
}

const cancel = () => {
  router.push('/')
}
</script>

<style scoped>
.product-create {
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 2rem;
}

.edit-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #2c3e50;
}

input, textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus, textarea:focus {
  outline: none;
  border-color: #3498db;
}

textarea {
  resize: vertical;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn-save, .btn-cancel {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-save {
  background-color: #27ae60;
  color: white;
  flex: 1;
}

.btn-save:hover:not(:disabled) {
  background-color: #219a52;
}

.btn-save:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.btn-cancel {
  background-color: #ecf0f1;
  color: #2c3e50;
}

.btn-cancel:hover {
  background-color: #bdc3c7;
}

.error-message {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #f8d7da;
  color: #721c24;
  border-radius: 4px;
  text-align: center;
}
</style>
