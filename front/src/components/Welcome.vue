<template>
    <main class="content">
      <h1>Hello World!</h1>
      <p>{{ name }} coded this page.</p>
    </main>
</template>
  
  <script>
    export default {
    name: 'Welcome',
    data() {
        return {
            name: 'Alexandre'
        }
    }
    }
</script>