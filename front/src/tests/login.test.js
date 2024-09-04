import { expect, test, describe } from 'vitest';
import { HttpRequest, HttpError} from '@/services/HttpRequest.js';

// ----> É NECESSÁRIO QUE O SERVIDOR DA API ESTEJA ATIVO <----
// ATENÇÃO: Adicione credenciais válidas no arquivo .env.local adequado.
const SUCCESS_POST_BODY = {
    username: import.meta.env.VITE_USER,
    password: import.meta.env.VITE_PASSWORD
}

// Execute com: npm run test:unit
const RESPONSE_TIMEOUT = 30000
const POST_ENDPOINT = "http://localhost:8000/login/"

const UNAUTHORIZED_POST_BODY = {
    username: "blablablabla",
    password: "jsijdaiodjsioadj"
}

describe("Request in POST method to endpoint /login/", () => {
    
    // Verifica se a função post com credenciais válidas está retornando um JSON que contém dados do usuário;
    test("Should have username property equals login credentials.", async () => {
        expect( await new HttpRequest().post(POST_ENDPOINT, SUCCESS_POST_BODY)).toHaveProperty('user.username', SUCCESS_POST_BODY.username)
    }, RESPONSE_TIMEOUT);

    // Verifica se a função post com credenciais inválidas está retornando uma ErrorAPI status 401;
    test("Should have HttpError Status 401 UNAUTHORIZED", async () => {
        expect.assertions(1)
        try { 
            await new HttpRequest().post(POST_ENDPOINT, UNAUTHORIZED_POST_BODY);
        } catch (error) {
            expect(error).toBeInstanceOf(HttpError).toHaveProperty('status', 401);
        }
    }, RESPONSE_TIMEOUT);
})