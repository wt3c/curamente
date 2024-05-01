import HEADER from "./common.js"


const APP = Vue.createApp({
    data() {
        return {
            patient: 'Lucas G. Souza',
        };
    }, 
    methods: {
    },
});

APP.component(HEADER.nametag, HEADER)

APP.mount("#app")