
# Título do Projeto

Projeto criado para criar uma lista de tarefas TODO.

# Nome do Projeto

Todo List

## Descrição

Este projeto foi desenvolvido utilizando Django, um framework web em Python que facilita a criação de aplicações robustas e escaláveis. O objetivo principal deste projeto é [Criar uma lista de tarefas e poder gerencia-las], proporcionando aos usuários uma interface intuitiva e funcional para [que o usuario possa, criar, editar, concluir e excluir uma tarefa].

## Objetivo

O objetivo do projeto é [Facilitar a criação de tarefas diarias], permitindo que os usuários [possam monitorar as atividades criadas].

## História

Este projeto surgiu da necessidade de [colocar em práticas estudos e apredizados.]. 
## Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

- **[Python 11](https://www.python.org/)**: Linguagem de programação usada no backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Framework web em Python que facilita o desenvolvimento rápido e seguro de aplicações web.
- **[HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML/HTML5)**: Estruturação da interface do usuário.
- **[CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)**: Estilização da interface do usuário.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: Framework CSS para design responsivo e componentes UI.
- **[Git](https://git-scm.com/)**: Controle de versão para gerenciamento do código-fonte.
- **[Banco SQLITE](https://git-scm.com/)**: Armazenamento de dados do projeto.


## Demonstrações

Aqui estão alguns GIFs que demonstram funcionalidades importantes do projeto:

### Criando uma Tarefa

![Criando tarefa](https://github.com/user-attachments/assets/63f07d6b-2256-4bd2-9ac0-b41f2354bd74)

&nbsp;

### Editar Tarefa

![Editar](https://github.com/user-attachments/assets/e8bf990d-ee54-429d-aff1-3fb7ab41921d)

&nbsp;

### Concluir Tarefa

![Concluir](https://github.com/user-attachments/assets/aec5a287-7416-49b2-aa93-397e6b10517e)

&nbsp;

### Excluir Tarefa

![Excluir](https://github.com/user-attachments/assets/fea1dbcf-865a-465f-a386-ff990d31271b)

&nbsp;

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    https://github.com/kemuelkesley/todo-list_django.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd todo-list_django
    ```

3. Crie um ambiente virtual e ative-o:
    ```bash
    Criando ambiente virtutal:
    
    python -m venv venv

    Ativando ambiente Virtual
    
    # No Linux source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Crie um arquivo .env:
    ```bash
    Crie um arquivo .env na raiz do projeto, com essa configuração:

    SECRET_KEY="3jay6+mi5666)e2vzmf=y&ob$1f97ob7o@9ut!w@azl71o*n&"
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3

    ```

6. Realize as migrações do banco de dados:
    ```bash
    1 - python manage.py migrate
    2 - python manage.py migrate todos

6. Criar um Usuario para acessar a área Administrativa:
    ```bash
    1 - python manage.py createsuperuser
    2 - Crie o nome do usuario
    3 - Crie e-mail caso queira
    4 - Crie sua senha
    5 - Confirme no Final
    6 - Para acessar a área administrativa http://127.0.0.1:8000/admin/
    7 - Digite o usuario criado e a senha.

    ```

7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver

    Endereço:

    http://127.0.0.1:8000/
    ```

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, problemas ou pull requests, sinta-se à vontade para colaborar.

## Licença

Este projeto está licenciado sob a [kemSoftware].

