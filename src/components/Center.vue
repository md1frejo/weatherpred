<script setup>
 import Left from './Left.vue'
 import Graph from './Graph.vue'
 import citiesa from '../../cities.json'
 import wdata from '../../wstats.json'
 import { ref } from 'vue'

 // list of city names
 const cities = ref(citiesa)

 // helper to downsample to daily
 function downsampleDaily(values) {
   const daily = []
   for (let i = 0; i < values.length; i += 24) {
     const day = values.slice(i, i + 24)
     const avg = day.reduce((a, b) => a + b, 0) / day.length
     daily.push(avg)
   }
   return daily
 }

 // 👇 initialize with first city
 const firstCity = cities.value[0]
 const cityData = wdata[firstCity]
 const selectedCity = ref({
   city: firstCity,
   temp: downsampleDaily(cityData.temp),
   precip: downsampleDaily(cityData.precip)
 })
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
      <Graph
        v-if="selectedCity"
        :city="selectedCity.city"
        :temp="selectedCity.temp"
        :precip="selectedCity.precip"
      />
    </div>
  </div>
</template>
