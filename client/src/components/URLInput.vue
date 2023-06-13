<template>
    <input type="text" placeholder="Enter/Paste Youtube URL" v-model="mediaStore.url"/>
</template>

<script setup>
    import { useMediaStore } from '@/stores/mediaStore.js';
    import { onUpdated } from 'vue'
    import axios from 'axios';

    const mediaStore = useMediaStore()

    onUpdated(() => {
        axios.post('/api/media/', { 'url': mediaStore.url }, { cors: true })
        .then(response => {
            // Check if URL is valid
            if(Object.keys(response.data).length !== 0) {
                mediaStore.isUrlValid = true
                mediaStore.title = response.data.title
                mediaStore.resolution = response.data.resolution
                mediaStore.length = response.data.length
                mediaStore.thumbnail_url = response.data.thumbnail_url
            } else {
                mediaStore.isUrlValid = false
            }
            
            console.log(mediaStore)
        })
        .catch(error => console.error(error))
    })
</script>

<style scoped>

</style>