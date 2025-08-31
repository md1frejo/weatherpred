<script setup>
 import { defineProps, defineEmits } from 'vue'

 const props = defineProps({
   cities: Array,
   selectedCity: String
 })
 const emit = defineEmits(['update:selectedCity'])

 function selectCity(city) {
   emit('update:selectedCity', city)
 }
 
</script>

<template>
  <p class="text-2xl mb-2">Cities</p>
  <ul>
    <li 
      v-for="(city, idx) in props.cities" 
      :key="idx" 
      @click="selectCity(city)" 
      class="cursor-pointer hover:text-blue-500"
    >
      {{ city }}
    </li>
  </ul>
</template>
