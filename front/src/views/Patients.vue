<template>
    <main class="direction__collumn__page">
            <section class="container window mt-1">
                <h2 class="mb-1">Pacientes de {{ therapist }}</h2>
                <hr>
                <p v-if="patients.length == 0 || null" class="mt-1">Não há dados de pacientes.</p>
                <ul class="content" v-if="userId">
                    <li class="mt-1" v-for="patient in patients" :key="patient.id">
                        <h3>{{ patient.user.first_name }} {{ patient.user.last_name }}</h3>
                        <ul class="content">
                            <li>Email: {{ patient.contatos.email }}</li>
                            <li>Telefone: {{ patient.contatos.telefone }}</li>
                            <li>
                                <RouterLink to="/sessions">
                                    Sessões de {{ patient.user.first_name }} {{ patient.user.last_name }}
                                </RouterLink>
                            </li>
                            <li>
                                <button @click="managePatient(patient)" class="content">
                                    Gerenciar Perfil
                                </button>
                            </li>
                        </ul>
                    </li>
                </ul>
            </section>  
        </main>
</template>

<script>
import { HttpRequest, httpErrorHandler } from '@/services/HttpRequest';
import { useProfileStore } from '@/stores/profile';

export default {
    name: 'Patients',
    data() {
        return {
            userId: null,
            therapist: "",
            patients: [],
        };
    },
    beforeMount(){
        try{
            // USER AUTHENTICATED TEMPLATE BEFORE THE FEATURE, DO NOT DEPLOY!!!
            const user = JSON.parse(sessionStorage.getItem('therapist_user'));
			this.therapist = user.first_name;
			this.userId = user.id;

        } catch(error){
			console.log("Sem dados de usuário.");
		}

        if(this.userId){
            this.getPatients();
        }
    },
    methods: {
        async getPatients(){
            try {
                let data = await new HttpRequest().get(`http://localhost:8000/core/usuario/${this.userId}/`);
                this.patients = data.pacientes;
            } catch (error) {
                console.error(httpErrorHandler(error));
            }
        }, 
        
        managePatient(patient) {
            this.savePatientData(patient);
            this.$router.push('/manage');
        },
        
        savePatientData(patient) {
            const profileStore = useProfileStore();
            profileStore.profile = patient;
        },
    },
};
</script>