export class HttpError extends Error {
    constructor(message, status) {
        super(message);
        this.status = status;
    }
}

export class HttpRequest {
    constructor() {
        let setCsrfToken = false;
    }

    async get(endpoint){
        const response = await fetch(endpoint, this.configOptions());
        if(!response.ok) {
            throw new HttpError("Erro na requisição", response.status);
        }

        return response.json();
    }

    async post(endpoint, body) {
        const response = await fetch(endpoint, this.configOptions('POST', body));
        if (!response.ok) {
            throw new HttpError('Erro na requisição', response.status);
        }

        return response.json();
    }

    async put(endpoint, body) {
        const response = await fetch(endpoint, this.configOptions('PUT', body));
        if (!response.ok) {
            throw new HttpError('Erro na requisição', response.status);
        }

        return response.json();
    }

    async delete(endpoint, body) {
        const response = await fetch(endpoint, this.configOptions('DELETE', body));
        if (!response.ok) {
            throw new HttpError('Erro na requisição', response.status);
        }

        return true;
    }

    configOptions(method = "GET", body = null) {
        let options = {
            method: method,
            headers: { 'Content-Type' : 'application/json' },
        };

        if (body) {
            options['body'] = JSON.stringify(body);
        }

        if (this.setCsrfToken){
            const csrfToken = this.getCookie('csrftoken');
            if (!csrfToken) {
                throw new Error("Token CSRF não encontrado.");
            }
            options.headers = { 'Content-Type' : 'application/json', 'X-CSRFToken': csrfToken};
        }
        
        return options;
    }

    getCookie(name){
        const value = `;${document.cookie}`;
        const parts = value.split(`;${name}=`);
        if (parts.length === 2) {
            return parts.pop().split(';').shift();
        }

        return null;
    }
    
    useCsrfToken() {
        this.setCsrfToken = true;
        return this;
    }
};

export function httpErrorHandler(error){
    let message;
    if(error instanceof HttpError) {
        switch(error.status) {
            case 400:
                message = "Solicitação inválida"
                break
            case 401:
                message = "Não autorizado"
                break;
            case 403:
                message = "Proibido"
                break;
            case 404:
                message = "Não encontrado"
                break;
            case 500:
                message = "Erro interno do servidor"
                break;
            case 503:
                message = "Serviço indisponível"
            default:
                return "Ocorreu um erro inesperado na requisição, tente novamente mais tarde.";
        }
        return `Status ${error.status} -- ${message}`;

    } else {
        return `Ocorreu um erro inesperado, entre contato com o suporte: ${error}`
    }
}
