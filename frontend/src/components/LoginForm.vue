<template>
  <form @submit.prevent="handleLogin">
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button type="submit">Login</button>
    <p v-if="error" style="color: red">{{ error }}</p>
  </form>
</template>

<script>
import api from '../axios.js'

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await api.post('/token/', {
          username: this.username,
          password: this.password,
        });
        const token = response.data.access;
        localStorage.setItem('accessToken', token);
        this.error = null;
        alert('Login exitoso');
        // Aquí podrías redirigir al usuario a otra vista
      } catch (err) {
        this.error = 'Credenciales incorrectas o error de conexión.';
      }
    }
  }
}
</script>
