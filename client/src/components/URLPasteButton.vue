<template>
    <button @click="handlePaste">Paste</button>
</template>

<script setup>

import { useMediaStore } from '@/stores/mediaStore.js'

let  mediaStore = useMediaStore()

const handlePaste = () => {
    navigator.clipboard.readText()
        .then(pastedText => {
            mediaStore.url = pastedText
            console.log('Pasted Text: ', mediaStore.url)
        })
        .catch(error => {
            console.log('Failed To Paste: ', error)
        })
}
</script>

<style  scoped>

</style>