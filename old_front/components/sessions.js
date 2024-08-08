export const NEW_SESSION = {
    nametag: "new-session",
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
    template:`
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
                <div class="checkbox__wrapper">
                    <label for="overcome">
                        <input type="checkbox" id="overcome">
                        <span class="cbx">
                          <svg width="12px" height="11px" viewBox="0 0 12 11">
                            <polyline points="1 6.29411765 4.5 10 11 1"></polyline>
                          </svg>
                        </span>
                        <span>Superado?</span>
                    </label>
                </div>
            </div>

            <span class="newSession__notes" :class="{active:write_notes}">
                <textarea class="notes__textarea" cols="30" rows="10" placeholder="Digite aqui..."></textarea>
            </span>
            
            <hr>
            <input type="submit" value="Salvar Sessão" class="btn btn--submit">
        </form>
    </section>
    `
};

export const SESSION_ITEM = {
    nametag: "session-item",
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
    template:`
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
    `,
    mounted() {
        this.changeColor(this.df, this.dc);
    },
};

export const SESSION_LIST = {
    nametag: "session-list",
    components: {
        SESSION_ITEM
    },
    props: {
        title: String,
        path: String,
    },
    data() {
        return {
            items: [],
            notes_active: false
        };
    }, 
    methods: {
        async getSessions() {
            try {
                const RESPONSE = await fetch(this.path);
                const DATA = await RESPONSE.json();
                this.items = DATA.items;

            } catch (error) {
                console.error("Erro ao carregar os dados das sessões:", error);
            }
        },
    },

    template:`
    <details @click="getSessions">
            <summary class="session__title title--toggle">{{ title }}</summary>
                <ul class="session__list">
                    <li v-for="item in items" :key="item.id">
                    <SESSION_ITEM 
                    :data="item.data"
                    :main="item.period"
                    :df="item.df"
                    :dc="item.dc"
                    :notes="item.text">
                    </SESSION_ITEM>
                    </li>
                </ul>
    </details>  
    `
}