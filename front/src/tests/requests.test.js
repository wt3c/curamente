import { beforeAll, describe, expect, expectTypeOf, test } from 'vitest';

// ----> É NECESSÁRIO QUE O SERVIDOR DA API ESTEJA ATIVO <----
// Adicione um id de usuário válido
const RESPONSE_ID_VALUE = 1
const BEFORE_ALL_TIMEOUT = 30000;
let response;
let body;

describe("Request in GET method to core/usuarios/id endpoint.", () => {

beforeAll(async () => {
    response = await fetch(`http://localhost:8000/core/usuario/${RESPONSE_ID_VALUE}/`);
    body = await response.json();
}, BEFORE_ALL_TIMEOUT);

test('Should have response status 200', () => {
    expect(response.status).toBe(200);
});

test('Should have content-type', () => {
    expect(response.headers.get('Content-Type')).toBe('application/json');
});

test('Should have array in the body', () => {
    expectTypeOf(body).toBeArray();
});

test(`The object id should contain value equals: ${RESPONSE_ID_VALUE}`, () => {
    expect(body.id).toBe(RESPONSE_ID_VALUE);
});
});