<script setup>

 import { ArrowLeftFromLine,ArrowRightFromLine,UtilityPole } from 'lucide-vue-next'
 import {hello} from '@/utils/misc.js'

</script>

<template>

  <div class="p-8">
    <div class="bg-gradient-to-t from-deepskyblue-800 to-deepskyblue-1000 p-6 rounded-2xl text-center space-x-4">
      <div class="flex items-center space-x-4">
	<UtilityPole class="w-10 h-10 text-SteelBlueg-300" />
	<p class="text-center flex-1 text-ma1 font-caveat">weather data from 30 of the largest cities in the world</p>
	<UtilityPole class="w-10 h-10 text-SteelBlueg-300" />
      </div>
    </div>
  </div>
</template>

<style scoped>

 /* bg-gradient-to-t → bottom → top

    bg-gradient-to-tr → bottom-left → top-right

    bg-gradient-to-r → left → right

    bg-gradient-to-br → top-left → bottom-right

    bg-gradient-to-b → top → bottom

    bg-gradient-to-bl → top-right → bottom-left

    bg-gradient-to-l → right → left

    bg-gradient-to-tl → bottom-right → top-left
  */
 
</style>
 
