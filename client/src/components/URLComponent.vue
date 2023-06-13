<template>
    <div>
        <URLInput />
        <URLPasteButton v-if="!isPhone"/>
        <p v-else>Manually Patse</p>
        <URLClearButton />
    </div>
</template>

<script setup>

import { ref } from 'vue'
import URLClearButton from './URLClearButton.vue';
import URLInput from './URLInput.vue';
import URLPasteButton from './URLPasteButton.vue';

import { isMobilePhone } from '@/functions/isMobilePhone.js';

const isPhone = ref(isMobilePhone())

</script>

<style scoped>

</style>