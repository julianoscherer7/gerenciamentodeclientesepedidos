# Sistema de Gerenciamento de Loja

Este é um sistema de gerenciamento de loja desenvolvido em Python com interface gráfica (Tkinter) e banco de dados MySQL. O sistema permite o cadastro de clientes e o registro de pedidos.

## Requisitos

- Python 3.x
- MySQL Server
- Bibliotecas Python: `mysql-connector-python`, `tkinter`, `tkcalendar`

## Instalação

1. **Instale o Python**:
   - Baixe e instale o Python a partir do site oficial: [python.org](https://www.python.org/).

2. **Instale o MySQL**:
   - Baixe e instale o MySQL Server a partir do site oficial: [MySQL Downloads](https://dev.mysql.com/downloads/mysql/).

3. **Instale as bibliotecas necessárias**:
   - Abra o terminal ou prompt de comando e execute:
     ```bash
     pip install mysql-connector-python tkcalendar
     ```

4. **Configure o banco de dados**:
   - Execute o script SQL fornecido (`script.sql`) para criar o banco de dados e as tabelas necessárias.

## Execução

1. **Configure as credenciais do banco de dados**:
   - No arquivo `app.py`, substitua `"sua_senha"` pela senha do seu usuário MySQL.

2. **Execute o aplicativo**:
   - No terminal ou prompt de comando, navegue até a pasta do projeto e execute:
     ```bash
     python app.py
     ```

## Funcionalidades

- **Clientes**:
  - Cadastrar novos clientes.
  - Editar informações de clientes existentes.
  - Excluir clientes.
  - Listar todos os clientes cadastrados.

- **Pedidos**:
  - Registrar novos pedidos.
  - Listar todos os pedidos registrados.

## Estrutura do Banco de Dados

O banco de dados `loja` contém duas tabelas:
- `clientes`: Armazena informações dos clientes.
- `pedidos`: Armazena informações dos pedidos, com referência ao cliente.

---

## Contato

Para dúvidas ou sugestões, entre em contato: [seu_email@exemplo.com]