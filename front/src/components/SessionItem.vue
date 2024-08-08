<template>
    <span class="session__item"
    v-bind:class=" {'item--green': color == 'G','item--red': color == 'R', 'item--yellow': color == 'Y'}">

        <div class="item__header" v-on:click="toggleNotes" v-on:setup="changeColor(df, dc)"
        v-bind:class="{'item--green': color == 'G','item--red': color == 'R', 'item--yellow': color == 'Y'}">
            <p>{{ data }}</p>
            <span class="visual-line"></span>
            <p>{{ main }}</p>
            <span class="visual-line"></span>
            <p>D.F= {{ df }}</p>
            <span class="visual-line"></span>
            <p>D.C= {{ dc }}</p>
        </div>
        
        <div class="session__notes {{ color }}" :class="{active:notes_active}" v-bind:class="
        {'item--green': color == 'G','item--red': color == 'R', 'item--yellow': color == 'Y'}">
            <p>{{ notes }}</p>
        </div>
    </span>
</template>

<script>
export default {
    name: "SessionItem",
    props: {
        data: String,
        main: String,
        df: Number,
        dc: Number,
        notes: String,
    },
    data() {
        return {
            notes_active: false,
            color: ""
        };
    },
    methods: {
        toggleNotes(){
            this.notes_active = !this.notes_active 
        },
        changeColor(df, dc){
            this.color = (df < 4 && dc < 4) ? "G" : (df > 7 || dc > 7) ? "R" : "Y";
        }
    },
    mounted() {
        this.changeColor(this.df, this.dc);
    }
}
</script>

<style>
    @import '@/assets/sessions.css';
</style>