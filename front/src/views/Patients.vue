<template>
    <main class="direction__collumn__page">
            <section class="container window mt-1">
                <h2 class="mb-1">Pacientes de {{ therapist }}</h2>
                <hr>
                <ul class="content" >
                    <li class="mt-1" v-for="patient in patients" :key="patient.id">
                        <h3>{{ patient.name }}</h3>
                        <ul class="content">
                            <li>Email: {{ patient.email }}</li>
                            <li>Telefone: {{ patient.phone }}</li>
                            <li><RouterLink to="/sessions">Sessões de {{ patient.name }}</RouterLink></li>
                        </ul>
                    </li>
                </ul>
            </section>  
        </main>
</template>

<script>
export default {
    name: 'Patients',
    data() {
        return {
            therapist: "Zé Fulano",
            patients: []
        };
    },
    methods: {
        async getPatients(){
            try {
                const RESPONSE = await fetch("/patients.json");
                const DATA = await RESPONSE.json();
                this.patients = DATA.patients;

            } catch (error) {
                console.error("Erro ao carregar dados dos pacientes", error);
            }
        }
    },
    mounted(){
        this.getPatients();
    }
};
</script>