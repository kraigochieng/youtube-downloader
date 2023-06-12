<template>
    <button @click="clearUrl">Clear</button>
</template>

<script setup>
    import { useMediaStore } from '@/stores/mediaStore.js'
    let mediaStore = useMediaStore()

    function clearUrl() {
        mediaStore.url= ''
    }
</script>

<style scoped>

</style>