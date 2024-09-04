<template>
    <main>
        <section>
            <h2>{{ title }}</h2>
            <hr>
            <form @submit.prevent="submitProfile" class="d-flex flex-collumn w-50">
                <label for="firstname_field">Nome:</label>
                <input type="text" id="firstname_field" v-model="firstname">

                <label for="lastname_field">Sobrenome:</label>
                <input type="text" id="lastname_field" v-model="lastname">

                <label for="email_field">Email:</label>
                <input type="email" id="email_field" v-model="email">

                <label for="phone_field">Telefone:</label>
                <input type="text" id="phone_field" v-model="phone">

                <label for="userType_field">Tipo de perfil:</label>
                <select id="userType_field" v-model="userType">
                    <option value="paciente">Paciente</option>
                    <option value="terapeuta">Terapeuta</option>
                </select>

                <hr class="mt-1 mb-1">
                <input type="submit" value="Enviar">
            </form>

            <button v-if="id" @click='deleteProfile'>Excluir Usuário</button>
        </section>
        <section>
            <h2>Sessões correntes:</h2>
            <ul v-if="sessions.length > 0">
                <li v-for="session in sessions" class="mb-1">
                    <ul>
                        <li>Sessão {{ session.tipo }}</li>
                        <li>Data: {{ normalizeDate(session.horario).date }}</li>
                        <li>Horário: {{ normalizeDate(session.horario).hour }}</li>
                    </ul>
                </li>
            </ul>
            <hr>
        </section>
    </main>
</template>

<script>
import { useProfileStore } from '@/stores/profile';
import { HttpRequest, httpErrorHandler } from '@/services/HttpRequest';
import { normalizeDate } from '@/services/Normalize';

export default {
    name: 'PatientProfile',
    computed: {
        $store() {
            return useProfileStore();
        },
    },
    data(){
        return {
            title: "Novo Perfil",
            firstname: "",
            lastname: "",
            userType: "",
            email: "",
            phone: "",
            sessions: [],
            id: null,
        };
    },
    methods: {
        async submitProfile(){
            let body = this.setProfile();
            try {
                let request = new HttpRequest().useCsrfToken();

                if(this.id){
                    request = await request.put(`http://localhost:8000/core/usuario/${this.id}/`, body);
                    alert("Informações salvas, perfil editado com sucesso.");
                } else {
                    request = await request.post(`http://localhost:8000/core/usuario/${this.id}/`);
                    alert(`Novo perfil de ${body.first_name} ${body.lastname} criado com sucesso!`);
                }

            } catch(error) {
                console.error(httpErrorHandler(error));
            }
        },

        async deleteProfile() {
            let warn = confirm(`Tem certeza que quer deletar ${this.firstname} ${this.lastname}?`)
            if(warn){
                try {
                    const request = new HttpRequest().useCsrfToken();
                    let response = await request.delete(`http://localhost:8000/core/usuario/${this.id}/`);
                    if(response) {
                        alert("Operação concluída.");
                        this.$router.push('/patients');
                    }
                } catch(error) {
                    console.error(httpErrorHandler(error));
                }
            }
        },

        loadStore() {
            let patient = this.$store.profile;
            this.id = patient.id
            this.firstname = patient.user.first_name;
            this.lastname = patient.user.last_name;
            this.userType = patient.tipo
            this.email = patient.contatos.email;
            this.phone = patient.contatos.telefone;
            this.sessions = patient.sessao
            this.title = "Editar Perfil"
        },
        
        setProfile(){
            let body = {
                foto: null,
                tipo: this.$store.profile.tipo,

                user: {
                    first_name: this.firstname,
                    last_name: this.lastname
                },
                contatos: {
                    telefone: this.phone,
                    email: this.email
                },
                sessao: this.sessions,
                pacientes: [],
            };

            if(this.id == null){
                body.user = {
                    username: this.email,
                    password: "Qwerty123@",
                    first_name: this.firstname,
                    last_name: this.lastname
                };

                body.tipo = this.userType;
            };

            return body;
        },
    },
    mounted() {
        try {
            this.loadStore();
        } catch(error){
            console.log("Sem dados persistidos.");
        }
    }
};
</script>