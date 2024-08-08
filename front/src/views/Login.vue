<template>
    <div class="direction__collumn__page">
        <section class="container window mt-2">
            <h1 class="mb-1">Login</h1>
            <hr>
            <form @submit.prevent="handleLogin" class="form d-flex flex-collumn mt-1 font--medium">
                <label for="email_field">Email</label>
                <input type="email" v-model="email" id="email_field" class="mb-1">

                <label for="password_field">Password</label>
                <input type="password" v-model="password" id="password_field">

                <button type="submit" class="btn btn--submit btn--small mt-2">Login</button>

                <h2 class="mt-1">{{ authenticated }}</h2>
            </form>
        </section>
    </div>
</template>

<script>
    export default {
        data () {
        return {
            email: '',
            password: '',
            authenticated: ''
        };
    },
    methods: {
        async handleLogin() {
            try {
                const RESPONSE = await fetch("/users.json");
                const USERS = await RESPONSE.json();

                const USER = USERS.users.find(
                    (u) => u.email === this.email && u.password == this.password
                );

                if (USER) {
                    this.authenticated = 'Você está autenticado!';
                    //Redirecionar para a próxima página <- fazer nas views do Django?
                } else {
                    alert("Credenciais inválidas. Tente novamente.");
                }
            } catch (error) {
                console.error("Erro ao carregar dados de login:", error);
            }
        },
    }, 
};
</script>