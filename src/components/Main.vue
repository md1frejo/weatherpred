<script>

 import { ArrowLeftFromLine,ArrowRightFromLine,ListEnd } from 'lucide-vue-next'
 import {hello} from '@/utils/misc.js'

</script>

<template>

  <div class="p-8">
    <div class="bg-gradient-to-b from-lightblueg-900 to-lightblueg-1100p-6 rounded-2xl text-center space-x-4">
      <div class="flex items-center space-x-4">
	<ArrowLeftFromLine class="w-10 h-10 text-deepskyblue-200" />
	<p class="text-ma1 font-roboto">weather data from 30 of the largest cities in the world</p>
	<ArrowRightFromLine class="w-20 h-20 text-deepskyblue-200" />
	<ArrowLeftFromLine class="w-20 h-20 text-red-400" />
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
 
