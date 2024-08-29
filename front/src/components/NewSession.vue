<template>
    <section class="sessionContainer">
        <h2 class="session__title">Sessão Cronológica</h2>
        <hr>
        <form class="newSession__form">
            <div class="newSession__form__row-1">
                <div class="row-1__period">
                    <label for="period-field" class="row-1__fieldname">Período</label>
                    <input type="text" id="period-field" class="newSession__input">
                </div>

                <div class="row-1__discomforts">
                    <legend class="row-1__fieldname">Níveis de Desconforto</legend>
                    <label for="DF" class="discomforts__label">D.F</label>
                    <input type="number" id="DF" min="0" max="10" class="newSession__input input--discomfort">
                    <label for="DC" class="discomforts__label">D.C</label>
                    <input type="number" id="DC" min="0" max="10" class="newSession__input input--discomfort">
                </div>
            </div>

            <div class="newSession__form__row-2">
                <button class="btn btn--openNotes" v-on:click="openWriteNotes" alt="Escrever nota" type="button">Adicionar nota</button>
                <Checkbox label="overcome" description="Superado?" />
            </div>

            <span class="newSession__notes" :class="{active:write_notes}">
                <textarea class="notes__textarea" cols="30" rows="10" placeholder="Digite aqui..."></textarea>
            </span>
            
            <hr>
            <input type="submit" value="Salvar Sessão" class="btn btn--submit">
        </form>
    </section>
</template>

<script>
import Checkbox from "./Checkbox.vue"

export default {
    name: 'NewSession',
    data(){
        return {
            write_notes: false
        };
    }, 
    methods: {
        openWriteNotes(){
            this.write_notes = !this.write_notes
        }
    },
    components: {
        Checkbox,
    }
}
</script>

<style>
    @import '@/assets/sessions.css';
</style>