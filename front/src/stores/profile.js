import { defineStore } from 'pinia';

export const useProfileStore = defineStore('profile', {
    state: () => ({
        profile: '',
    }),
    actions: {
        resetStore() {
            this.$reset();
        }
    }
});