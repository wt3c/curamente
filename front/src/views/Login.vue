<template>
    <div class="direction__collumn__page">
        <section class="container window mt-2">
            <h1 class="mb-1">Login</h1>
            <hr>
            <form @submit.prevent="login" class="form d-flex flex-collumn mt-1 font--medium">
                <label for="email_field">Usuário</label>
                <input type="text" v-model="username" id="email_field" class="mb-1">

                <label for="password_field">Senha</label>
                <input type="password" v-model="password" id="password_field">

                <button type="submit" class="btn btn--submit btn--small mt-2">Login</button>

                <h2 class="mt-1">{{ message }}</h2>
            </form>
        </section>
    </div>
</template>

<script>
import { HttpRequest, HttpError, httpErrorHandler } from '@/services/HttpRequest';

export default {
    data () {
    return {
            username: '',
            password: '',
            message: ''
        };
    },
    methods: {
        async login() {
            let body = {
                username: this.username,
                password: this.password
            }
            
            try {
                this.message = 'Autenticando...';
                let response = await new HttpRequest().post("http://localhost:8000/login/", body);
                if(response){
                    // JUST FOR AUTHENTICATED FEATURES TESTS, IN PRODUCTION IT HAVE TO BE DIFFERENT!
                    const user_model = {
                        id: response.id,
                        username: response.user.username,
                        first_name: response.user.first_name,
                        last_name: response.user.last_name,
                        email: response.contatos.email,
                        phone: response.contatos.telefone
                    };
                    sessionStorage.setItem('therapist_user', JSON.stringify(user_model));
                    this.$router.push('/');
                }

            } catch(error) {
                if (error instanceof HttpError && error.status == 401) {
                    this.message = "Credenciais inválidas. Tente novamente";
                } else {
                    console.error(httpErrorHandler(error));
                }  
            };
        }
    },
};

</script>