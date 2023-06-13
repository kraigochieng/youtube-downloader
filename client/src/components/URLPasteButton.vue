<template>
    <button @click="handlePaste" @touchend="handlePaste">Paste</button>
</template>

<script setup>

import { useMediaStore } from '@/stores/mediaStore.js'

let  mediaStore = useMediaStore()

const handlePaste = () => {
    if(navigator.clipboard && navigator.clipboard.readText) {
        navigator.clipboard.readText()
        .then(pastedText => {
            mediaStore.url = pastedText
            console.log('Pasted Text: ', mediaStore.url)
        })
        .catch(error => {
            console.log('Failed To Paste: ', error)
        })
    } else {
        alert('Clipboard API not supported')
    }
}
</script>

<style  scoped>

</style>