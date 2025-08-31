<script setup>

  import Graph from './Graph.vue'

  const props = defineProps({
  cities: {
  type: Array,
  required: true
  }
  })
 
</script>


<template>
  <!-- Flex row -->
  <p class="text-2xl mb-2">Cities</p>
  <ul>
    <li v-for="(city, idx) in props.cities" :key="idx">
      {{ city }}
    </li>
  </ul>

</template>

<style>
</style>
