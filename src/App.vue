<script setup>

 import Topbar from './components/Topbar.vue'
 import Main from './components/Main.vue'
 import Center from './components/Center.vue'
 import Bottom from './components/Bottom.vue'
 
</script>

<template>

  <Topbar />
  <Main />

  <div class="min-h-screen flex flex-col">
    <!-- Top row: Center (100% width) -->
    <div class="w-full bg-gray-200 p-4">
      <Center />
    </div>
  </div>

</template>

<style scoped>
 
</style>

