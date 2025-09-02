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

const firstCity = cities.value[0]
const cityData = wdata[firstCity]

const selectedCity = ref({
    city: firstCity,
    temp: downsampleDaily(cityData.temp),
    precip: downsampleDaily(cityData.precip)
})

</script>

<template>

  <div class="p-8 bg-GhostWhiteg-100">
    <div class="bg-gradient-to-b from-antiquewhiteg-900 to-antiquewhiteg-400 via-slateblueg-1500 p-6 rounded-2xl text-center space-x-4">
      <p class="text-4xl">prediction: does it gonna rain in ..?</p>
    </div>  
  <div class="flex flex-1">
    <!-- Left column -->
    <div class="w-[15%] bg-antiquewhiteg-800 p-4">
      <Left :cities="cities" v-model:selectedCity="selectedCity" />
    </div>
    
    <!-- Graph column -->
    <div class="w-[85%] bg-antiquewhiteg-900 p-4">
      <Graph
        v-if="selectedCity"
        :city="selectedCity.city"
        :temp="selectedCity.temp"
        :precip="selectedCity.precip"
	/>
    </div>
    </div>
</div>

</template>
