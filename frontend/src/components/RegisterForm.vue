<template>
  <form @submit.prevent="handleRegister">
    <input v-model="username" placeholder="Username" />
    <input v-model="email" placeholder="Email" />
    <input v-model="password" type="password" placeholder="Password" />
    <button type="submit">Register</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      alert(`Registro con ${this.username}, ${this.email}`)
      // Aquí luego conectaremos con el backend
    }
  }
}
</script>
