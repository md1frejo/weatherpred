<script setup>
 import wdata from '../../wstats.json'

 const props = defineProps({
   cities: Array,
   selectedCity: String
 })

 // 👇 add this
 const emit = defineEmits(['update:selectedCity'])

 function selectCity(city) {
   const cityData = wdata[city]

   const tempDaily = downsampleDaily(cityData.temp)
   const precipDaily = downsampleDaily(cityData.precip)

   emit('update:selectedCity', {
     city,
     temp: tempDaily,
     precip: precipDaily
   })
 }

 function downsampleDaily(values) {
   const daily = []
   for (let i = 0; i < values.length; i += 24) {
     const day = values.slice(i, i + 24)
     const avg = day.reduce((a, b) => a + b, 0) / day.length
     daily.push(avg)
   }
   return daily
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
