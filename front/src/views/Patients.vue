<template>
    <main class="direction__collumn__page">
            <section class="container window mt-1">
                <h2 class="mb-1">Pacientes de {{ therapist }}</h2>
                <hr>
                <ul class="content" v-if="user">
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
                <p v-else class="mt-1">Não há dados de pacientes.</p>
            </section>  
        </main>
</template>

<script>
import { HttpRequest, httpErrorHandler } from '@/services/HttpRequest';
import { useProfileStore } from '@/stores/profile';
import { useAuthStore } from '@/stores/auth';

export default {
    name: 'Patients',
    computed: {
		$store() {
	  		return useAuthStore();
		},
  	},
    data() {
        return {
            user: null,
            therapist: "",
            patients: [],
        };
    },
    methods: {
        async getPatients(){
            try {
                let data = await new HttpRequest().useCsrfToken().get(`http://localhost:8000/core/usuario/${this.user}/`);
                this.patients = data.pacientes;
            } catch (error) {
                console.error(httpErrorHandler(error))
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
    beforeMount(){
        try{
            this.therapist = this.$store.firstname;
            this.user = this.$store.userId; 
        } catch(error){
			console.log("Sem dados persistidos.");
		}

        if(this.user){
            this.getPatients();
        }
    },
};
</script>