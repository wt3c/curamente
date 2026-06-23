<template>
    <details @click="getSessions">
            <summary class="session__title title--toggle">{{ title }}</summary>
                <ul class="session__list">
                    <li v-for="item in items" :key="item.id">
                    <SessionItem 
                    :date="item.date"
                    :main="item.period"
                    :df="item.df"
                    :dc="item.dc"
                    :notes="item.text" />
                    </li>
                </ul>
    </details> 
</template>

<script>
import SessionItem from "@/components/SessionItem.vue";
import { HttpRequest, httpErrorHandler } from "@/services/HttpRequest";

export default {
    name: "SessionList",
    components: {
        SessionItem
    },
    props: {
        title: String,
        path: String,
    },
    data() {
        return {
            items: [],
            notes_active: false
        };
    }, 
    methods: {
        async getSessions() {
            try {
                let data = await new HttpRequest().get(this.path);
                this.items = data.items;

            } catch(error) {
                console.error(httpErrorHandler(error));
            }
        },
    },
}
</script>

<style>
    @import '@/assets/sessions.css';
</style>