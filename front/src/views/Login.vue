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

                <h2 class="mt-1">{{ authenticated }}</h2>
            </form>
        </section>
    </div>
</template>

<script>
import { HttpRequest, HttpError, httpErrorHandler } from '@/services/HttpRequest';
import { useAuthStore } from '@/stores/auth';

export default {
    data () {
    return {
            username: '',
            password: '',
            authenticated: ''
        };
    },
    methods: {
        async login() {
            let body = {
                username: this.username,
                password: this.password
            }
            
            try {
                let response = await new HttpRequest().post("http://localhost:8000/login/", body);
                if(response){
                    this.authenticated = 'Você está autenticado!';
                    const authStore = useAuthStore();
                    authStore.userId = response.id;
					authStore.firstname = response.user.first_name;
                    setTimeout( () => { this.$router.push('/') }, 1000);
                }

            } catch(error) {
                if (error instanceof HttpError && error.status == 401) {
                    this.authenticated = "Credenciais inválidas. Tente novamente";
                } else {
                    console.error(httpErrorHandler(error));
                }  
            };
        }
    },
};

</script>