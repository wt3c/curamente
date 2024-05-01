import HEADER from '../components/common.js';
import {NEW_SESSION, SESSION_LIST} from "../components/sessions.js";

const APP = Vue.createApp({
    data(){
        return {
            patient: "Fulano D. Tal"
        };
    }
});

APP.component(HEADER.nametag, HEADER); //App-Header
APP.component(NEW_SESSION.nametag, NEW_SESSION);
APP.component(SESSION_LIST.nametag, SESSION_LIST);

APP.mount("#app");