<template>
  <div class="signin">
    <h2>Sign In</h2>
    <form @submit.prevent="signin">
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input v-model="form.mot_de_passe" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

interface SignInForm {
  email: string
  mot_de_passe: string
}

const form = reactive<SignInForm>({
  email: '',
  mot_de_passe: ''
})

const error = ref<string | null>(null)

const signin = async () => {
  try {
    const res = await axios.post('http://localhost:5000/auth/signin', form)
    localStorage.setItem('user', JSON.stringify(res.data))
    router.push('/')
  } catch (err: any) {
    error.value = err.response?.data?.error || 'Login failed'
  }
}
</script>
