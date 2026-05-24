<template>
  <div id="app">
    <nav class="navbar">
      <router-link to="/" class="nav-link">Главная</router-link>
      <router-link to="/create" class="nav-link btn-create">Создать товар</router-link>
    </nav>
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  min-height: 100vh;
}

.navbar {
  background-color: #2c3e50;
  padding: 1rem 2rem;
  display: flex;
  gap: 1rem;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: #34495e;
}

.nav-link.btn-create {
  background-color: #27ae60;
  margin-left: auto;
}

.nav-link.btn-create:hover {
  background-color: #219a52;
}

.main-content {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
