import { defineStore } from "pinia";
import { ref } from "vue";

export const useMediaStore = defineStore('media', () => {
    const url = ref('')
    const full_length = ref('')
    return { url, full_length }
})