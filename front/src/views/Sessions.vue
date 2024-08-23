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
    computed: {
        $store() {
            return useProfileStore();
        },
    },
    data(){
        return {
            patient: "Nome do Paciente",
            id: null,
            sessions: []
            
        };
    }, 
    components: {
        NewSession,
        SessionList
    },
    methods: {
        loadStore() {
            let patient = this.$store.profile;
            this.id = patient.id
            this.patient = `${patient.user.first_name} ${patient.user.last_name}`;
            this.sessions = patient.sessao
        },
    }
}
</script>

<style>
    @import '@/assets/sessions.css';
</style>