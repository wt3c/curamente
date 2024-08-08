<template>
    <details @click="getSessions">
            <summary class="session__title title--toggle">{{ title }}</summary>
                <ul class="session__list">
                    <li v-for="item in items" :key="item.id">
                    <SessionItem 
                    :data="item.data"
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
                const RESPONSE = await fetch(this.path);
                const DATA = await RESPONSE.json();
                this.items = DATA.items;

            } catch (error) {
                console.error("Erro ao carregar os dados das sessões:", error);
            }
        },
    }
}
</script>

<style>
    @import '@/assets/sessions.css';
</style>