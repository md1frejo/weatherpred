<!-- Center.vue -->
<script setup>
 import Left from './Left.vue'
 import Graph from './Graph.vue'
 import citiesa from '../../cities.json'
 import { ref } from 'vue'

 const cities = ref(citiesa)
 const selectedCity = ref(null) // Left will update this
</script>

<template>
  <p class="text-4xl mb-4">center</p>

  <div class="flex flex-1">
    <!-- Left column -->
    <div class="w-[15%] bg-gray-100 p-4">
      <Left :cities="cities" v-model:selectedCity="selectedCity" />
    </div>

    <!-- Graph column -->
    <div class="w-[85%] bg-white p-4">
      <Graph :city="selectedCity" />
    </div>
  </div>
</template>
