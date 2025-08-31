<script setup>

 import {
   Chart as ChartJS,
   Title,
   Tooltip,
   Legend,
   LineElement,
   CategoryScale,
   LinearScale,
   PointElement
 } from 'chart.js'

 import { Line } from 'vue-chartjs'

 // Register Chart.js components
 ChartJS.register(
   Title,
   Tooltip,
   Legend,
   LineElement,
   CategoryScale,
   LinearScale,
   PointElement
 )

 // Example rainfall data (daily)
 const labels = [
   '2025-08-21',
   '2025-08-22',
   '2025-08-23',
   '2025-08-24',
   '2025-08-25',
   '2025-08-26',
   '2025-08-27'
 ]

 const data = {
   labels,
   datasets: [
     {
       label: 'Daily Rainfall (mm)',
       data: [2, 15, 5, 20, 7, 12, 0], // Example values
       borderColor: 'rgba(54, 162, 235, 1)',
       backgroundColor: 'rgba(54, 162, 235, 0.2)',
       tension: 0.3, // smooth curve
       fill: true
     }
   ]
 }

 const options = {
   responsive: true,
   plugins: {
     legend: {
       position: 'top'
     },
     title: {
       display: true,
       text: 'Daily Rainfall Over Time'
     }
   },
   scales: {
     x: {
       title: {
         display: true,
         text: 'Date'
       }
     },
     y: {
       title: {
         display: true,
         text: 'Rainfall (mm)'
       },
       beginAtZero: true
     }
   }
 }
</script>

<template>
  <div class="p-4">
    <Line :data="data" :options="options" />
  </div>
</template>
