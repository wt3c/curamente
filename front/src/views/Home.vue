<template>
	<main class="content">
	  <h1>Bem vindo {{ therapist }}!</h1>
	  <p>{{ description }}</p>

	  <section class="content" v-if="user">
		<ul class="mb-1">
		  <li v-for="patient in patients">
			<h3>{{ patient.user.first_name }} {{ patient.user.last_name }}</h3>
			<ul>
			  <li v-for="session in patient.sessao">
				<p>Data de consulta: {{ normalizeDate(session.horario).date }}</p>
				<p>Horário de consulta: {{ normalizeDate(session.horario).hour }}</p>
			  </li>
			</ul>
		  </li>
		</ul>
		<hr class="mb-1">
		<button class="content">Novo Paciente</button>
	  </section>
	</main>
</template>
  
<script>
import { useAuthStore } from '@/stores/auth';
import { HttpRequest, httpErrorHandler} from '@/services/HttpRequest';
import { Normalizer } from '@/services/Normalizer';

export default {
	name: 'Home',
	computed: {
		$store() {
	  		return useAuthStore();
		},
  	},
	data() {
		return {
			user: null,
			therapist: "Terapeuta",
			description: "Não há novas sessões no momento.",
			patients: [],
		};
	}, 
	methods: {
		normalizeDate(info){
			return new Normalizer().normalizeDate(info);
		},
		async getData() {
			try {
				let data = await new HttpRequest().useCsrfToken().get(`http://localhost:8000/core/usuario/${this.user}/`);
				this.patients = data.pacientes;
				this.description = "Aqui estão as sessões correntes:"

			} catch(error) {
				console.error(httpErrorHandler(error));
			}
		},
	},
	beforeMount() {
		try {
			this.therapist = this.$store.firstname;
			this.user = this.$store.userId;
		} catch(error){
			console.log("Sem dados persistidos.");
		}

		if (this.user) {
			this.getData();
		}
	},
}
</script>