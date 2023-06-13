<template>
    <table>
        <thead>
            <th>Video</th>
        </thead>
        <tbody>
            <tr v-for="resolution in mediaStore.resolution" :key="resolution">
               <td @click="downloadVideo(mediaStore.url, resolution)">{{ resolution }}</td> 
            </tr>
        </tbody>
    </table>
</template>

<script setup>
    import axios from 'axios';
    import { useMediaStore } from '@/stores/mediaStore.js'

    const mediaStore = useMediaStore()

    function downloadVideo(url, resolution) {
        axios.post('/api/download-video/', { 'url': url, 'resolution': resolution })
            .then(response => console.log(response))
            .catch(error => console.error(error))
    }
</script>

<style scoped>

</style>