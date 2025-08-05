<template>
	<main class="content">
	  <h1>Bem vindo {{ therapist }}!</h1>
	  <p>{{ description }}</p>

	  <section class="content" v-if="userId">
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
		<button class="content" v-on:click="this.$router.push('/manage');">Novo Paciente</button>
	  </section>
	</main>
</template>
  
<script>
import { HttpRequest, httpErrorHandler} from '@/services/HttpRequest';
import { Normalizer } from '@/services/Normalizer';

export default {
	name: 'Home',
	data() {
		return {
			userId: null,
			therapist: "Terapeuta",
			description: "Não há novas sessões no momento.",
			patients: [],
		};
	},
	beforeMount() {
		try {
			// USER AUTHENTICATED TEMPLATE BEFORE THE FEATURE, DO NOT DEPLOY!!!
			const user = JSON.parse(sessionStorage.getItem('therapist_user'));
			this.therapist = user.first_name;
			this.userId = user.id;

		} catch(error){
			console.log("Sem dados de usuário.");
		}

		if (this.userId){
			this.getData();
		}
	},
	methods: {
		normalizeDate(info){
			return new Normalizer().normalizeDate(info);
		},
		async getData() {
			try {
				let data = await new HttpRequest().get(`http://localhost:8000/core/usuario/${this.userId}/`);
				this.patients = data.pacientes;
				if(this.patients.length > 0){
					this.description = "Aqui estão as sessões correntes:"
				} 

			} catch(error) {
				console.error(httpErrorHandler(error));
			}
		},
	},
}
</script>