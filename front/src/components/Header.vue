<template>
    <header class="header__container">
        <nav class="container">
            <h1></h1> <!-- Espaço container para futura logo. -->
            <img src="../assets/three-horizontal-lines-icon.svg" v-on:click="openMenu" alt="Abrir menu" class="header__menu__btn">

            <div class="menu__overlay" v-if="menu_active" v-on:click="closeMenu"></div>
            <div class="header__menu__items" :class="{active:menu_active}">
                <ul>
                    <li><RouterLink to="/" v-on:click="closeMenu">Home</RouterLink></li>
                    <li><RouterLink to="/login" v-on:click="closeMenu">Perfil</RouterLink></li>
                    <li><RouterLink to="/patients" v-on:click="closeMenu">Pacientes</RouterLink></li>
                    <li><RouterLink to="/login" v-on:click="logout">Logout</RouterLink></li>
                </ul>
            </div>
        </nav>
    </header>
</template>

<script>
    export default {
        name: 'HeaderVue',
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
            },

            logout(){
                // AUTHENTICATED TEMPLATE BEFORE THE FEATURE, DO NOT DEPLOY!
                if(sessionStorage.getItem('therapist_user')){
                    sessionStorage.removeItem('therapist_user');
                }
            }
        }
    }
</script>

<style>
.header__container {
    background-color: #323232;
    color: #ffffff;
    width: 100%;
    height: 60px;

    display: flex;
    justify-content: center;
    align-items: center;
}

.header__container > nav {
    display: flex;
    justify-content: space-between;
    height: 60px;
    align-items: center;
    font-weight: 500;
}

.header__menu__btn {
    height: 24px;
}

.menu__overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 40%;
    height: 100vh;
    background-color: #000000;
    opacity: 0.8;
}

.header__menu__items {
    position: fixed;
    top: 0;
    right: 0;
    background-color: #222222;
    width: 60%;
    height: 100vh;
    z-index: 1;

    display: none;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.header__menu__items.active{
    display: flex;
}
.header__menu__items > ul {
    list-style: none;
    text-align: center;
}

.header__menu__items > ul li {
    margin: 20px 0px;
}

.header__menu__items > ul li a {
    color: var(--main-bg);
}

@media screen and (min-width: 992px){
    .header__menu__btn, .menu__overlay{
        display: none;
    }

    .header__menu__items{
        display: flex;
        position: static;
        height: 60px;
        width: auto;
        background-color: transparent;
    }

    .header__menu__items > ul {
        display: flex;
        gap: 22px;
    }
}
</style>