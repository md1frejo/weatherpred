<script setup>
 import { ref, computed } from 'vue'
 import {
   Chart as ChartJS,
   Title,
   Tooltip,
   Legend,
   LineElement,
   CategoryScale,
   LinearScale,
   PointElement,
   Filler
 } from 'chart.js'
 import zoomPlugin from 'chartjs-plugin-zoom'
 import { Line } from 'vue-chartjs'

 ChartJS.register(
   Title,
   Tooltip,
   Legend,
   LineElement,
   CategoryScale,
   LinearScale,
   PointElement,
   Filler,
   zoomPlugin
 )

 const props = defineProps({
   city: { type: String, required: true },
   temp: { type: Array, required: true },
   precip: { type: Array, required: true }
 })

 function generateDates(startDate, days) {
   const dates = []
   let current = new Date(startDate)
   for (let i = 0; i < days; i++) {
     dates.push(current.toISOString().slice(0, 10))
     current.setDate(current.getDate() + 1)
   }
   return dates
 }

 const chartRef = ref(null)

 const showTemp = ref(true)
 const showPrecip = ref(true)

 const data = computed(() => {
   const labels = generateDates("2020-01-01", props.temp.length)

   const datasets = []
   if (showTemp.value) {
     datasets.push({
       label: `Temperature in ${props.city}`,
       data: props.temp,
       borderColor: 'rgba(255, 99, 132, 1)',
       backgroundColor: 'rgba(255, 99, 132, 0.2)',
       tension: 0.3,
       yAxisID: 'y'
     })
   }
   if (showPrecip.value) {
     datasets.push({
       label: `Precipitation in ${props.city}`,
       data: props.precip,
       borderColor: 'rgba(54, 162, 235, 1)',
       backgroundColor: 'rgba(54, 162, 235, 0.2)',
       tension: 0.3,
       fill: true,
       yAxisID: 'y1'
     })
   }

   return { labels, datasets }
 })

 const options = {
   responsive: true,
   maintainAspectRatio: false,
   plugins: {
     legend: { position: 'top' },
     title: { display: true, text: 'from 2020-01-01 to 2025-01-01' },
     zoom: {
       zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: 'x' },
       pan: { enabled: true, mode: 'x' }
     }
   },
   scales: {
     y: { type: 'linear', position: 'left', title: { display: true, text: 'Temperature (°C)' } },
     y1: { type: 'linear', position: 'right', title: { display: true, text: 'Precipitation (mm)' }, grid: { drawOnChartArea: false } }
   }
 }

function resetZoom() {
  if (chartRef.value?.chart) {
    chartRef.value.chart.resetZoom()
  }
 }

</script>

<template>
  <div class="p-4 space-y-4">
    <p class="text-gp1">temperature and rain in {{ props.city }}</p>

    <div class="h-96">
      <Line ref="chartRef" :data="data" :options="options" />
    </div>

    <!-- Toggle buttons -->
    <div class="space-x-2">
      <button
        @click="showTemp = !showTemp"
        class="px-3 py-1 rounded-lg shadow text-white"
        :class="showTemp ? 'bg-red-600 hover:bg-redg-700' : 'bg-gray-500 hover:bg-gray-600'"
      >
        {{ showTemp ? 'Hide Temperature' : 'Show Temperature' }}
      </button>

      <button
        @click="showPrecip = !showPrecip"
        class="px-3 py-1 rounded-lg shadow text-white"
        :class="showPrecip ? 'bg-blue-600 hover:bg-SteelBlueg-300' : 'bg-gray-500 hover:bg-gray-600'"
      >
        {{ showPrecip ? 'Hide Precipitation' : 'Show Precipitation' }}
      </button>
    </div>

    <!-- Reset zoom button -->
    <button
      @click="resetZoom"
      class="px-4 py-2 bg-green-600 text-white rounded-lg shadow hover:bg-green4g-500 transition"
    >
      Reset Zoom
    </button>
  </div>
</template>
