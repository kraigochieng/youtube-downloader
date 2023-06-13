<template>
  <div>
    <URLComponent />
    <template v-if="mediaStore.isUrlValid">
      <PreviewComponent />
      <VideoTable />
    </template>
    <template v-else>
      <p>Enter Valid URL</p>
    </template>
    
  </div>
</template>

<script setup>

import VideoTable from './components/VideoTable.vue';
import PreviewComponent from './components/PreviewComponent.vue';
import URLComponent from './components/URLComponent.vue';



import { useMediaStore } from '@/stores/mediaStore.js'
const mediaStore = useMediaStore()
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
