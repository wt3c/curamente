<template>
  <HeaderVue />
  <RouterView />
</template>

<script>
  import HeaderVue from '../components/Header.vue'

  export default {
    data() {
      return {
        name: 'Alexandre'
      }
    },
    components: {
      HeaderVue
    }
  }
</script>
