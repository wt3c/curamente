import { defineStore } from 'pinia'

export const useAuthStore = defineStore('profile', {
    state: () => ({
        userId: null,
        firstname: "Terapeuta",
    }),
});