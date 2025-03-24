# Web Automation Test

## Descrição

Este repositório contém um projeto de automação de testes para aplicações web. O objetivo é fornecer uma estrutura robusta e escalável para testar diferentes aspectos de uma aplicação web de forma automatizada, utilizando ferramentas de automação como o [Selenium](https://www.selenium.dev/) e o [pytest](https://pytest.org/). Para este projeto em específico foi utilizado como base o site [saucedemo](https://www.saucedemo.com/), que simula um e-commerce, fornecendo diversos tipos de usuários, produtos e ações.

## Tecnologias

O projeto utiliza as seguintes tecnologias:

- **Python**: Linguagem de programação principal para os testes.
- **Selenium**: Ferramenta para automação de navegadores, utilizada para interagir com a interface da aplicação.
- **pytest**: Framework para execução dos testes e gerenciamento de resultados.
- **WebDriver**: Drivers específicos para cada navegador (Chrome, Firefox, etc.) usados para controlar o navegador.
- **python-html**: Plugin para o pytest que gera relatórios HTML detalhados, facilitando a visualização dos resultados dos testes.

## Funcionalidades

- Automação de testes em navegadores.
- Relatórios detalhados de execução e falhas.

## Lista de Testes
1. **Validações de login**
    - 1.1. Com usuário e senha vazio
    - 1.2. Com usuário válido e senha vazia
    - 1.3. Com usuário inválido e senha inválida
    - 1.4. Com conta bloqueada
    - 1.5. Com usuário e senha válido

2. **Validações de ordenação dos produtos**
    - 2.1. Opção 'Name (A to Z)'
    - 2.2. Opção 'Name (Z to A)'
    - 2.3. Opção 'Price (low to high)'
    - 2.4. Opção 'Price (high to low)'

3. **Validações de carrinho de compra**
    - 3.1. Adicionar apenas 1 item ao carrinho
    - 3.2. Adicionar múltiplos item ao carrinho

4. **Validações de checkout**
    - 4.1. Sem nenhum campo preenchido
    - 4.2. Apenas com first name preenchido
    - 4.3. Com first name, last name e sem postal code
    - 4.4. Checkout completo de apenas 1 item
    - 4.5. Checkout completo de múltiplos itens

## Requisitos

- **Python 3.7+**: O projeto foi desenvolvido e testado com Python 3.7 ou superior.
- **Dependências**: Todas as dependências necessárias estão listadas no arquivo `requirements.txt`.

## Instalação

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

### 1. Clonar o repositório

```bash
git clone https://github.com/viniraf/web-automation-test.git
```

### 2. Instalar as dependências

Navegue até o diretório do projeto e instale as dependências usando o `pip`:

```bash
cd web-automation-test
```

```bash
pip install -r requirements.txt
```

## Execução de Testes

### 1. Executando testes com o pytest

Para rodar os testes, utilize o comando:

```bash
pytest
```

Isso executará todos os testes presentes no diretório de testes e exibirá os resultados no terminal.

```bash
pytest --html=report_tests.html
```
Isso executará todos os testes presentes no diretório de testes e criará um relatório HTML com os resultados.

## Estrutura do Projeto

Aqui está uma visão geral da estrutura do projeto:

```
web-automation-test/
│
├── pages/                   # Diretório contendo as Páginas de Objeto para interação com a interface
│   ├── example_page.py      # Exemplo de página de objeto
│
├── tests/                   # Diretório contendo os testes automatizados
│   ├── conftest.py          # Arquivo com fixtures comuns entre os testes
│   ├── test_01_example.py   # Exemplo de arquivo de teste
│
├── pytest.ini               # Configurações do pytest
├── README.md                # Este arquivo
└── requirements.txt         # Arquivo com as dependências do projeto

```
