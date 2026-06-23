# Cura mentes

O sistema Cura mentes é focado em cadastrar clientes e informações que auxiliam ao terapeuta a direcionar as suas
consultas.

O sistema é feito em duas camadas separadas: Frontend e Backend

## Tecnologias

### Frontend
* Vue.js 3
* Vue Router
* Pinia (gerenciamento de estado)

### Backend
* Python 3.13+
* Django
* Django REST Framework

## Configuração do Ambiente

### Requisitos
- Python 3.13 ou superior
- Node.js 18 ou superior
- npm ou yarn

### Backend (Django)

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd curamente
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

O backend estará disponível em http://localhost:8000/

### Frontend (Vue.js)

1. Navegue até a pasta do frontend:
```bash
cd front
```

2. Instale as dependências:
```bash
npm install
# ou
yarn install
```

3. Inicie o servidor de desenvolvimento:
```bash
npm run dev
# ou
yarn dev
```

O frontend estará disponível em http://localhost:5173/

## Uso

1. Acesse o frontend em http://localhost:5173/
2. Faça login com suas credenciais
3. Gerencie pacientes, sessões e perfis através da interface

## API Endpoints

### Autenticação
- POST `/login/` - Autenticar usuário

### Usuários
- GET `/core/usuario/` - Listar pacientes do terapeuta
- POST `/core/usuario/` - Criar novo usuário
- GET `/core/usuario/<id>/` - Obter detalhes de um usuário específico
- PUT `/core/usuario/<id>/` - Atualizar usuário
- DELETE `/core/usuario/<id>/` - Excluir usuário