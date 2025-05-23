<template>
  <div class="signup">
    <h2>Sign Up</h2>
    <form @submit.prevent="signup">
      <input v-model="form.nom" placeholder="Name" required />
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input v-model="form.mot_de_passe" type="password" placeholder="Password" required />
      <button type="submit">Register</button>
    </form>
    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

interface SignUpForm {
  nom: string
  email: string
  mot_de_passe: string
}

const form = reactive<SignUpForm>({
  nom: '',
  email: '',
  mot_de_passe: ''
})

const error = ref<string | null>(null)

const signup = async () => {
  try {
    const res = await axios.post('http://localhost:5000/auth/signup', form, {
        withCredentials: true
    })
    router.push('/signin')
  } catch (err: any) {
    error.value = err.response?.data?.error || 'Signup failed'
  }
}
</script>
