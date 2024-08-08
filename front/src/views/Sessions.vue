<template>
    <div id="app" class="direction__collumn__page">
        <p class="backTo">
            <RouterLink to="/patients">Voltar para a página do paciente</RouterLink>
        </p>
        <div class="sessions__wrapper">
            <NewSession />
            <section class="sessionContainer sessionContainer--patient">
                <div>
                    <h2 class="session__title">{{ patient }}</h2>
                    <hr>
                </div>
                <div class="session__list__wrapper">
                    <SessionList title="Sessões Cronológicas" path="/items.json" />
                    <SessionList title="Sessões Temáticas" path="/items2.json" />
                </div>
            </section>
        </div>
    </div>
</template>

<script>
import NewSession from "@/components/NewSession.vue";
import SessionList from "@/components/SessionList.vue";

export default {
    data(){
        return {
            patient: "Fulano D. Tal"
        };
    }, 
    components: {
        NewSession,
        SessionList
    }
}
</script>

<style>
    @import '@/assets/sessions.css';
</style>