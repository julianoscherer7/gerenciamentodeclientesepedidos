# Documentação Resumida das Funções do Código

Este documento descreve de forma resumida as principais funções do sistema de gerenciamento de loja.

---

## Funções Principais

### 1. **`conectar()`**
- **O que faz**: Conecta ao banco de dados MySQL.
- **Retorno**: Retorna a conexão ou `None` em caso de erro.

---

### 2. **`inserir_cliente(nome, email, telefone, tree, atualizar_lista_clientes)`**
- **O que faz**: Insere um cliente no banco de dados e atualiza a lista na interface.
- **Parâmetros**:
  - `nome`, `email`, `telefone`: Dados do cliente.
  - `tree`: Widget `Treeview` para exibir clientes.
  - `atualizar_lista_clientes`: Função para atualizar a lista.

---

### 3. **`listar_clientes()`**
- **O que faz**: Retorna todos os clientes do banco de dados.
- **Retorno**: Lista de clientes.

---

### 4. **`listar_clientes_combobox()`**
- **O que faz**: Retorna clientes para preencher a lista suspensa de pedidos.
- **Retorno**: Lista de clientes (ID e nome).

---

### 5. **`registrar_pedido(id_cliente, data_pedido, valor_total, tree_pedidos, atualizar_lista_pedidos)`**
- **O que faz**: Registra um pedido no banco de dados e atualiza a lista na interface.
- **Parâmetros**:
  - `id_cliente`, `data_pedido`, `valor_total`: Dados do pedido.
  - `tree_pedidos`: Widget `Treeview` para exibir pedidos.
  - `atualizar_lista_pedidos`: Função para atualizar a lista.

---

### 6. **`listar_pedidos()`**
- **O que faz**: Retorna todos os pedidos do banco de dados.
- **Retorno**: Lista de pedidos.

---

### 7. **`excluir_cliente(id, tree, atualizar_lista_clientes)`**
- **O que faz**: Exclui um cliente do banco de dados e atualiza a lista na interface.
- **Parâmetros**:
  - `id`: ID do cliente.
  - `tree`: Widget `Treeview` para exibir clientes.
  - `atualizar_lista_clientes`: Função para atualizar a lista.

---

### 8. **`editar_cliente(id, nome, email, telefone, tree, atualizar_lista_clientes)`**
- **O que faz**: Atualiza os dados de um cliente no banco de dados e atualiza a lista na interface.
- **Parâmetros**:
  - `id`: ID do cliente.
  - `nome`, `email`, `telefone`: Novos dados do cliente.
  - `tree`: Widget `Treeview` para exibir clientes.
  - `atualizar_lista_clientes`: Função para atualizar a lista.

---

### 9. **`main()`**
- **O que faz**: Inicializa a interface gráfica e configura as abas de clientes e pedidos.

---

## Interface Gráfica

### Aba de Clientes
- **Formulário**: Inserir, editar e excluir clientes.
- **Lista**: Exibe clientes em uma `Treeview`.

### Aba de Pedidos
- **Formulário**: Registrar pedidos com cliente, data e valor.
- **Lista**: Exibe pedidos em uma `Treeview`.

---

## Validações
- Verifica campos obrigatórios antes de inserir ou editar dados.
- Exibe mensagens de erro ou sucesso.

---

## Estrutura do Banco de Dados

- **`clientes`**: Armazena dados dos clientes.
- **`pedidos`**: Armazena dados dos pedidos, com referência ao cliente.

---

## Como Executar

1. Instale as dependências:
   ```bash
   pip install mysql-connector-python tkcalendar