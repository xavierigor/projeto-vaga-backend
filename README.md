# ACMEVita

## Instalando e executando

Este projeto pode ser configurado de duas formas: com ou sem Docker.

> Antes de começar a instalação, será necessário definir as variáveis de ambiente. Para isso, crie um arquivo chamado
> .env.dev na raiz do projeto e copie todo o conteúdo de .env.example para ele. Depois, basta preencher as variáveis no
> arquivo .env.dev com as credenciais da sua base local (ou Docker).

### Sem Docker (virtualenv)

1. Crie um virtualenv python na sua máquina
```shell
python -m venv .venv
```

2. Ative-o

Windows
```shell
.\.venv\Scripts\activate
```

Unix
```shell
source .venv/bin/activate
```

3. Instale as dependências
```shell
pip install -r requirements.txt
```

4. Aplique as migrações e execute o projeto
```shell
python manage.py db upgrade
```
```shell
python manage.py run
```

### Com o Docker

1. Construa e suba os containers
```shell
docker-compose up --build
```

2. Em outro terminal, aplique as migrações
```shell
docker-compose exec web python manage.py db upgrade
```

## Visualizando a API

Para ver a documentação Swagger, acesse http://127.0.0.1:5000/ no seu navegador, lá estarão listados todos os
endpoints disponíveis para consumo.

## Testes

Para executar os testes, use `python manage.py test`, ou (com Docker), `docker-compose exec web python manage.py test`.

## Principais dependências

- Python 3.8.9
- Flask 2.1.1
- SQLAlchemy 1.4.35

---

# ACMEVita

Projeto de modelagem de dados e criação de uma API utilizando Python e Flask.

**Este projeto é parte do processo de seleção de desenvolvedor backend da [Telavita](https://telavita.com.br).**

## Sobre o projeto

A ACMEVita está expandindo seus negócios e precisa de um sistema para gerenciar seus departamentos, colaboradores e dependentes.

O seu único desenvolvedor backend está de ferias, você foi recrutado para finalizar este projeto, boa sorte!

### Requisitos

#### Como um Usuário da API eu gostaria de consultar todos os departamentos para visualizar a organização da ACMEVita.

* Cada departamento deve possuir um *nome do departamento*.
* A API deve responder com uma listagem de departamentos no formato JSON informando o *nome do departamento* de cada departamento.

#### Como um Usuário da API eu gostaria de consultar todos os colaboradores de um departamento para visualizar a organização da ACMEVita.

* Cada colaborador deve possuir um *nome completo*.
* Cada colaborador deve pertencer a *um* departamento.
* Cada colaborador pode possuir *nenhum, um ou mais* dependententes.
* A API deve responder com uma listagem de colaboradores do departamento no formato JSON informando o *nome completo* de cada colaborador e a respectiva flag booleana `have_dependents` caso o colaborador possua *um ou mais dependentes*.

### Diferenciais

* Testes unitários
* Referência (Swagger ou similar)
* Documentação e instruções de configuração
* Separação das camadas de responsabilidade (modelagem de dados, serialização, lógica, etc)

### Instruções

1. Faça um _fork_ ou download deste projeto.
2. Trabalhe localmente no seu projeto, faça até o ponto que conseguir.
3. Você está livre para organizar a estrutura do projeto como preferir.
4. Você deve utilizar o Flask para criar os endpoints da API.
4. Você pode utilizar a ORM de sua preferência para modelagem de dados.
5. Suba o seu projeto para o GitLab, GitHub ou similar.
6. Nos envie o link para o seu projeto, **mesmo que não esteja finalizado!**

**Qualquer dúvida, entre em contato com [Rafael](mailto:rc@telavita.com.br)!**
