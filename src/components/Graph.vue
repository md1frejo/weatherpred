<script setup>

 import { computed } from 'vue' 
 
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

 import { Line } from 'vue-chartjs'

 ChartJS.register(
   Title,
   Tooltip,
   Legend,
   LineElement,
   CategoryScale,
   LinearScale,
   PointElement,
   Filler // 👈 don’t forget this
 )

 function generateDates(startDate, days) {
   const dates = []
   let current = new Date(startDate)
   for (let i = 0; i < days; i++) {
     dates.push(current.toISOString().slice(0, 10)) // YYYY-MM-DD
     current.setDate(current.getDate() + 1)
   }
   return dates
 }

 const data = computed(() => {
   const labels = generateDates("2020-01-01", props.temp.length)

  return {
    labels,
    datasets: [
      {
        label: `Temperature in ${props.city}`,
        data: props.temp,
        borderColor: 'rgba(255, 99, 132, 1)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        tension: 0.3,
        yAxisID: 'y'
      },
      {
        label: `Precipitation in ${props.city}`,
        data: props.precip,
        borderColor: 'rgba(54, 162, 235, 1)',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        tension: 0.3,
        fill: true,
        yAxisID: 'y1'
      }
    ]
  }
 })
 
 const props = defineProps({
   city: {
     type: String,
     required: true
   },
   temp: {
     type: Array,
     required: true
   },
   precip: {
     type: Array,
     required: true
   }
 })

 // Build chart data reactively

 const options = {
   responsive: true,
   plugins: {
     legend: { position: 'top' },
     title: { display: true, text: 'Weather Data' }
   },
   scales: {
     y: {
       type: 'linear',
       position: 'left',
       title: { display: true, text: 'Temperature (°C)' }
     },
     y1: {
       type: 'linear',
       position: 'right',
       title: { display: true, text: 'Precipitation (mm)' },
       grid: { drawOnChartArea: false }
     }
   }
 }
</script>

<template>
  <div class="p-4">
    <Line :data="data" :options="options" />
  </div>
</template>
