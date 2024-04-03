# Principais informações sobre o Front-end
## Design System
O Front-end do aplicativo de terapia segue o modelo de design atômico, onde um pequeno componente denominado átomo ganha um papel junto de outros componentes para que se formem moléculas, organismos, templates e páginas.

Ao desenvolver uma funcionalidade ou componente, reflita se isto pode se estender de seu propósito original e ser reutilizado em outras partes do projeto. 

Material de apoio: [Planejando Componentes Front-end: com Atomic Design (Vídeo)](https://www.youtube.com/watch?v=um_EnNF1D0g&lc=UgzmaP4keqVOe9uPzLx4AaABAg&ab_channel=Meri%C3%A9liManzano%7CMeriCoding)

## Estrutura de diretórios

```  
_>assets_
_>components_
_>consumables // tem utilidade apenas em desenvolvimento._
_>docs_
_>scripts_ 
_>styles_
arquivos.html
``` 
 
- **Assets**: Arquivos de mídia do projeto -- imagens, ícones, vídeos, músicas e etc.
- **Components**: Códigos em javascript que exportam objetos/componentes Vue.js
- **Consumables**: Arquivos JSON de teste para simular consumo de API.
- **Scripts**: Arquivos Javascript para códigos que se aplicam diretamente nas páginas.
- **Styles**: Arquivos de estilização CSS (Utilizando as convenções Mobile-first e BEM)

## Como utilizar o Vue.js dentro do projeto?
Nesse projeto foi optado por utilizar o Vue.js importado via CDN para que o desenvolvimento seja mais simples e ágil. O motivo é que o Back-end em Django já consome boa parte da estrutura do projeto e adicionar o Vue ao projeto como CLI traria mais um modelo MVC para ter que se aprofundar e lidar, retardando o processo.

Sendo assim, ao desenvolver uma página da web no projeto, importe o Vue no HTML desejado utilizando a **seguinte versão**:
``` HTML
<head>
<script src="https://cdn.jsdelivr.net/npm/vue@3.4.21/dist/vue.global.js" defer></script>
</head>
```

## Como importar e utilizar um componente Vue?
1. Adicione ao script principal da sua página HTML o atributo `type=module`:
```HTML
<script src="./scripts/meuScript.js" type="module" defer></script>
```
2. Localize o componente desejado dentro do diretório **/components** e importe-o pelo caminho do arquivo no principal script da sua página:
```Javascript
// --> Dentro de ./scripts/meuScript.js <--

// Importa o componente HEADER do arquivo common.js
import { HEADER } from '../components/common.js'; 

const APP = Vue.createApp({
    data(){
        return {
        };
    }
});

// Adiciona o componente ao App
APP.component(HEADER.nametag, HEADER) //nametag = "app-header"
APP.mount("#app");

```
**Importante!**: O componente deve ser atribuído ao app pela sua ***nametag***. Isso evita que os elementos importados tenham diferentes nomes pelas páginas, facilitando na identificação e na manutenção do código.

3. Verifique na documentação ou no diretório **./styles** se o componente que está sendo importado requer um arquivo de estilos.
```HTML
<head>
<link rel="stylesheet" href="styles/global.css">
<link rel="stylesheet" href="styles/common.css">

<script src="https://cdn.jsdelivr.net/npm/vue@3.4.21/dist/vue.global.js" defer></script>
<script src="./scripts/meuScript.js" type="module" defer></script>
</head>
``` 

4. Adicione o componente importado como um elemento HTML utilizando o nome atribuído na nametag.
```HTML
<body>
  <div id="#app">
	<App-Header></App-Header>
  </div>
</body>
```
Para facilitar a identificação de elementos importados dentro do código é interessante que se utilize a convenção de nomes iniciados em letras maiúsculas.

dessa forma: `<app-header> fica mais legível como <App-Header>`

Acesse: [Guia de componentes Vue](./3--vue-components-guide.md)


## Como criar um Componente Vue no projeto?
Partindo do pressuposto que o componente será desenvolvido com base no Vue.js CDN, é possível cria-lo da seguinte forma:

 1. Utilize o arquivo **./components/test.html** para criar o template do seu componente, isso garante as vantagens do autocomplete da IDE durante o desenvolvimento (Faça isso importando o Vue).
 
``` HTML
<head>
<script src="https://cdn.jsdelivr.net/npm/vue@3.4.21/dist/vue.global.js" defer></script>
<script src="./test.js" type="module" defer></script>
</head>
<body>
<!-- Inicia a Aplicação Vue -->
  <div id="app">
  <!-- Template (É o que de fato vai ser utilizado) -->
	<h1>Hello World!</h1>
	<button @click="count++">Contagem: {{ count }}</button>
  <!-- Fim do Template -->
  </div> 
</body>
```
2. Utilize o arquivo **./components/test.js** que já possuí um app montado para desenvolver a lógica do componente.
```Javascript
const APP = Vue.createApp({
data() {
	return {
	count: 0
	};
  }
});

APP.mount('#app')
``` 
3. Quando tudo estiver funcionando como planejado, abra um arquivo.js para comportar o componente (como **./components/common.js**), insira o código pronto dentro de um objeto e exporte-o.
```Javascript
export const COUNTER = {
   nametag: "counter", //A string da nametag deve ser toda em caracteres minúsculos
   data() {
     return {
	     count: 0
     };
	},
	template:`
	<h1>Hello World!</h1>  
	<button @click="count++">Contagem: {{ count }}</button>
	`
}

//Agora é só importar esse objeto no script da página HTML desejada, como visto antes.
```
**Importante!**: Assim como no código acima, não se esqueça de criar um nome na propriedade nametag para o componente Vue desenvolvido. Como mencionado antes, este será o nome do elemento que será chamado mais tarde no HTML. No caso do exemplo citado, o elemento será `<Counter></Counter>`. 


## Padrões de Estilização

O projeto segue o conceito de desenvolvimento mobile-first, então as funcionalidades são desenvolvidas voltadas primeiramente a dispositivos móveis e depois são adaptadas a outros dispositivos. Classes generalistas de CSS estão presentes majoritariamente no arquivo **./styles/global.css**, e são reutilizadas como componentes de estilo por praticamente todas as páginas HTML.

Acesse: [Guia de componentes CSS](./2--css-components-guide.md)
  
Também é utilizada a metodologia BEM no CSS, onde os nomes de classes são organizados no formato (Bloco, Elemento e Modificador) ajudando na clareza e organização do código.

Se você não é familiarizado com os conceitos citados pode saber mais através dos seguintes materiais:

- [BEM: A Convenção CSS Para Um Front End Muito Melhor (Vídeo)](https://www.youtube.com/watch?v=rltjnLyjFZk&t=648s&ab_channel=dpw)
- [Media Queries e breakpoints: projetando melhor experiência (Artigo)](https://blog.apiki.com/media-queries-breakpoints-projetos-mobile-first/)
- [Criando componentes CSS com o padrão BEM | Alura (Artigo)](https://www.alura.com.br/artigos/criando-componentes-css-com-padrao-bem)
