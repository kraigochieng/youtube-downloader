<template>
    <input type="text" placeholder="Enter/Paste Youtube URL" v-model="mediaStore.url"/>
</template>

<script setup>
    import { useMediaStore } from '@/stores/mediaStore.js';
    import { onUpdated } from 'vue'
    import axios from 'axios';

    const mediaStore = useMediaStore()

    onUpdated(() => {
        axios.post('/api/video/', { 'url': mediaStore.url }, { cors: true })
        .then(response => {
            let media = response.data

            mediaStore.full_length = media.full_length

            console.log(mediaStore)
        })
        .catch(error => console.error(error))
    })
</script>

<style scoped>

</style>