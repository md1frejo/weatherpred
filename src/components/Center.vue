<script setup>

 import { Telescope } from "lucide-vue-next";
 
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

 function randcity(cities) {

   const arr=cities.value
   const rc=Math.floor(Math.random()*arr.length)

   return arr[rc]
 }

 const randc=randcity(cities)
 
 const firstCity = cities.value[0]
 const cityData = wdata[firstCity]

 const selectedCity = ref({
   city: firstCity,
   temp: downsampleDaily(cityData.temp),
   precip: downsampleDaily(cityData.precip)
 })

 function pearson(city) {

   const x=wdata[city].temp
   const y=wdata[city].precip
   
   if (x.length !== y.length) {
     throw new Error("Arrays must have the same length");
  }

   const n = x.length;

  // means
   const meanX = x.reduce((a, b) => a + b, 0) / n;
   const meanY = y.reduce((a, b) => a + b, 0) / n;
   
  // numerator and denominators
   let num = 0;
   let denomX = 0;
   let denomY = 0;

   for (let i = 0; i < n; i++) {
    const dx = x[i] - meanX;
    const dy = y[i] - meanY;
    num += dx * dy;
    denomX += dx * dx;
    denomY += dy * dy;
  }

   console.log(num / Math.sqrt(denomX * denomY))
   const co=num / Math.sqrt(denomX * denomY);

   return Math.round(co * 1000) / 1000;
 }

 /* 
  * function pearson(city) {
  *   
  *   const te=wdata[city].temp
  *   const pr=wdata[city].precip

  *   const tes = te.reduce((acc, val) => acc + val, 0)
  *   const prs = pr.reduce((acc, val) => acc + val, 0)
  *   const teaverage = tes/te.length
  *   const prsverage = prs/te.length
  *   
  *   console.log(te)
  * }
  */
 
</script>

<template>

  <div class="p-8 bg-GhostWhiteg-100">
    <div class="bg-gradient-to-b from-deepskyblue-800 to-deepskyblue-1100 p-6 rounded-2xl text-center space-x-4">
      <div class="flex items-center space-x-4">
	<div class="bg-gradient-to-b from-deepskyblue-800 to-deepskyblue-1100 p-6 rounded-2xl text-center space-x-4">
	  <div class="flex items-center space-x-4">
	    <Telescope class="w-10 h-10 text-navajoWhite4g-200" />
	    <p class="text-c1 font-roboto">is it any correlation in <span class="text-slateblueg-100 font-roboto"> {{ selectedCity.city }} </span> between temperature and precipation?
	    </p>
	    <p class="text-c1 font-roboto">pearson prediction of <span class="text-red4g-100 font-roboto"> {{ pearson(selectedCity.city) }} </span> gives <span class="text-slateblueg-100 font-roboto"> {{pearson(selectedCity.city)>0.8?"correlation":"no correlation"}} </span></p>
	  </div>
	</div>  
      </div>
    </div>  
  <div class="flex flex-1">
    <!-- Left column -->
    <div class="w-[15%] bg-gradient-to-b from-deepskyblue-1000 to-deepskyblue-1300 p-4">
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
