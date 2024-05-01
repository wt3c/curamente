const APP = Vue.createApp({
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
                const RESPONSE = await fetch("../consumables/users.json");
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
});


APP.mount('#app');