<template>
  <div>
    <h1>Hello from dali !</h1>
    <p v-if="message">Backend says: {{ message }}</p>
    <p v-else>Loading...</p>
    <div>helooo theeereee</div>
    <p>eththrthtrh</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const message = ref<string | null>(null)

onMounted(async () => {
  try {
    const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/`)
    console.log('VITE_BACKEND_URL:', import.meta.env.VITE_BACKEND_URL) // 👈 LOG IT HERE

    const data = await response.json()
    message.value = data.message
    console.log('message.value', message.value)
  } catch (error) {
    console.error('Error fetching data:', error)
    message.value = 'Failed to connect to backend.'
  }
})
</script>
