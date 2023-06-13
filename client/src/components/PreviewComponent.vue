<template>
    <h1>{{ mediaStore.title }}</h1>
    <img :src="mediaStore.thumbnail_url" width="500"/>
</template>

<script setup>
    import { useMediaStore }from '@/stores/mediaStore.js'

    const mediaStore = useMediaStore()
</script>

<style scoped>

</style>