import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // important pour accéder depuis le conteneur
    port: 5173,
    strictPort: true, // empêche Vite de changer de port
    watch: {
      usePolling: true, // force Vite à surveiller les fichiers même dans Docker
    },
    proxy: {
      '/api': 'http://localhost:5000', // proxy vers Flask
    },
  },
})
