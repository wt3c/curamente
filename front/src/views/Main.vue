<template>
  <HeaderVue />
  <RouterView />
</template>

<script>
  import HeaderVue from '../components/Header.vue'

  export default {
    data() {
      return {}
    },
    components: {
      HeaderVue
    }
  }
</script>
