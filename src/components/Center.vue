<script setup>

 import Left from './Left.vue'
 import Graph from './Graph.vue'

 import citiesa from '../../cities.json';
 import { ref } from 'vue';
 
 const cities=ref(citiesa);
 
</script>

<template>

  <p class="text-4xl mb-4">center</p>


  <!-- Second row: Left + Graph -->
  <div class="flex flex-1">
    <!-- Left column (15%) -->
    <div class="w-[15%] bg-gray-100 p-4">
      <Left :cities="cities" />
    </div>

    <!-- Graph column (85%) -->
    <div class="w-[85%] bg-white p-4">
      <Graph />
    </div>
  </div>
  
</template>

<style>
</style>
