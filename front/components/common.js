const HEADER = {
    nametag: 'app-header',
    data() {
        return {
            menu_active: false
        };
    },
    methods: {
        openMenu() {
            this.menu_active = true;
        },
        closeMenu() {
            this.menu_active = false;
        }
    },
    template:`
    <header class="header__container">
        <nav class="container">
            <h1></h1> <!-- Espaço container para futura logo. -->
            <img src="../assets/three-horizontal-lines-icon.svg" v-on:click="openMenu" alt="Abrir menu" class="header__menu__btn">

            <div class="menu__overlay" v-if="menu_active" v-on:click="closeMenu"></div>
            <div class="header__menu__items" :class="{active:menu_active}">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Perfil</a></li>
                    <li><a href="./patients.html">Pacientes</a></li>
                    <li><a href="./login.html">Logout</a></li>
                </ul>
            </div>
        </nav>
    </header>
    `
};

export default HEADER;