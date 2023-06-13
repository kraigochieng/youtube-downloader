import { defineStore } from "pinia";
import { reactive, ref } from "vue";

export const useMediaStore = defineStore('media', () => {
    const isUrlValid = ref(false)
    const url = ref('')
    const title = ref('')
    const length = ref('')
    const thumbnail_url = ref('')
    const resolution = reactive([])
    return { isUrlValid, url, title, length, thumbnail_url, resolution }
})