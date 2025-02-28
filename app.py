import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Função para conectar ao banco de dados
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password= '',  # Substitua pela senha correta
            database="loja"
        )
        return conexao
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
        return None

# Função para inserir um cliente
def inserir_cliente(nome, email, telefone, tree, atualizar_lista_clientes):
    if not nome or not email or not telefone:
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios!")
        return

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
            atualizar_lista_clientes(tree)  # Atualiza a lista de clientes
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao inserir cliente: {err}")
        finally:
            cursor.close()
            conexao.close()

# Função para listar clientes
def listar_clientes():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao listar clientes: {err}")
            return []
        finally:
            cursor.close()
            conexao.close()

# Função para listar clientes no Combobox
def listar_clientes_combobox():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT id, nome FROM clientes")
            return cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao listar clientes: {err}")
            return []
        finally:
            cursor.close()
            conexao.close()

# Função para registrar um pedido
def registrar_pedido(id_cliente, data_pedido, valor_total, tree_pedidos, atualizar_lista_pedidos):
    if not id_cliente or not data_pedido or not valor_total:
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios!")
        return

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO pedidos (id_cliente, data_pedido, valor_total) VALUES (%s, %s, %s)", (id_cliente, data_pedido, valor_total))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")
            atualizar_lista_pedidos(tree_pedidos)  # Atualiza a lista de pedidos
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao registrar pedido: {err}")
        finally:
            cursor.close()
            conexao.close()

# Função para listar pedidos
def listar_pedidos():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                SELECT pedidos.id, clientes.nome, pedidos.data_pedido, pedidos.valor_total
                FROM pedidos
                JOIN clientes ON pedidos.id_cliente = clientes.id
            """)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao listar pedidos: {err}")
            return []
        finally:
            cursor.close()
            conexao.close()

# Função para excluir um cliente
def excluir_cliente(id, tree, atualizar_lista_clientes):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            atualizar_lista_clientes(tree)  # Atualiza a lista de clientes
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao excluir cliente: {err}")
        finally:
            cursor.close()
            conexao.close()

# Função para editar um cliente
def editar_cliente(id, nome, email, telefone, tree, atualizar_lista_clientes):
    if not nome or not email or not telefone:
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios!")
        return

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("UPDATE clientes SET nome = %s, email = %s, telefone = %s WHERE id = %s", (nome, email, telefone, id))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            atualizar_lista_clientes(tree)  # Atualiza a lista de clientes
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao atualizar cliente: {err}")
        finally:
            cursor.close()
            conexao.close()

# Função principal
def main():
    root = Tk()
    root.title("Sistema de Gerenciamento de Loja")
    root.geometry("1000x700")
    root.configure(bg="#f0f0f0")

    # Estilo para os botões
    estilo = ttk.Style()
    estilo.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="black", font=("Arial", 12))
    estilo.map("TButton", background=[("active", "#45a049")])

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Aba de Clientes
    frame_clientes = ttk.Frame(notebook, padding=20)
    notebook.add(frame_clientes, text="Clientes")

    # Widgets para inserir clientes
    Label(frame_clientes, text="Nome", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
    nome_entry = ttk.Entry(frame_clientes, font=("Arial", 12))
    nome_entry.grid(row=0, column=1, pady=5)

    Label(frame_clientes, text="Email", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
    email_entry = ttk.Entry(frame_clientes, font=("Arial", 12))
    email_entry.grid(row=1, column=1, pady=5)

    Label(frame_clientes, text="Telefone", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
    telefone_entry = ttk.Entry(frame_clientes, font=("Arial", 12))
    telefone_entry.grid(row=2, column=1, pady=5)

    # Treeview para exibir clientes
    tree_clientes = ttk.Treeview(frame_clientes, columns=("ID", "Nome", "Email", "Telefone"), show="headings", height=10)
    tree_clientes.heading("ID", text="ID")
    tree_clientes.heading("Nome", text="Nome")
    tree_clientes.heading("Email", text="Email")
    tree_clientes.heading("Telefone", text="Telefone")
    tree_clientes.grid(row=4, column=0, columnspan=2, pady=10)

    # Função para atualizar a lista de clientes
    def atualizar_lista_clientes(tree):
        for row in tree.get_children():
            tree.delete(row)
        for cliente in listar_clientes():
            tree.insert("", "end", values=cliente)

    # Botões para clientes
    ttk.Button(frame_clientes, text="Inserir", command=lambda: inserir_cliente(
        nome_entry.get(),
        email_entry.get(),
        telefone_entry.get(),
        tree_clientes,
        atualizar_lista_clientes
    )).grid(row=3, column=0, pady=10)

    ttk.Button(frame_clientes, text="Editar", command=lambda: editar_cliente(
        tree_clientes.item(tree_clientes.selection())["values"][0],
        nome_entry.get(),
        email_entry.get(),
        telefone_entry.get(),
        tree_clientes,
        atualizar_lista_clientes
    )).grid(row=3, column=1, pady=10)

    ttk.Button(frame_clientes, text="Excluir", command=lambda: excluir_cliente(
        tree_clientes.item(tree_clientes.selection())["values"][0],
        tree_clientes,
        atualizar_lista_clientes
    )).grid(row=3, column=2, pady=10)

    # Aba de Pedidos
    frame_pedidos = ttk.Frame(notebook, padding=20)
    notebook.add(frame_pedidos, text="Pedidos")

    # Widgets para registrar pedidos
    Label(frame_pedidos, text="Cliente", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
    clientes_combobox = ttk.Combobox(frame_pedidos, font=("Arial", 12))
    clientes_combobox.grid(row=0, column=1, pady=5)

    Label(frame_pedidos, text="Data do Pedido", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
    data_pedido_entry = DateEntry(frame_pedidos, font=("Arial", 12))
    data_pedido_entry.grid(row=1, column=1, pady=5)

    Label(frame_pedidos, text="Valor Total", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
    valor_total_entry = ttk.Entry(frame_pedidos, font=("Arial", 12))
    valor_total_entry.grid(row=2, column=1, pady=5)

    # Treeview para exibir pedidos
    tree_pedidos = ttk.Treeview(frame_pedidos, columns=("ID", "Cliente", "Data", "Valor Total"), show="headings", height=10)
    tree_pedidos.heading("ID", text="ID")
    tree_pedidos.heading("Cliente", text="Cliente")
    tree_pedidos.heading("Data", text="Data")
    tree_pedidos.heading("Valor Total", text="Valor Total")
    tree_pedidos.grid(row=4, column=0, columnspan=2, pady=10)

    # Função para atualizar a lista de pedidos
    def atualizar_lista_pedidos(tree):
        for row in tree.get_children():
            tree.delete(row)
        for pedido in listar_pedidos():
            tree.insert("", "end", values=pedido)

    # Botão para registrar pedido
    ttk.Button(frame_pedidos, text="Registrar Pedido", command=lambda: registrar_pedido(
        int(clientes_combobox.get().split(" - ")[0]),
        data_pedido_entry.get_date(),
        float(valor_total_entry.get()),
        tree_pedidos,
        atualizar_lista_pedidos
    )).grid(row=3, column=0, pady=10)

    # Carregar dados iniciais
    def carregar_dados():
        clientes = listar_clientes_combobox()
        clientes_combobox['values'] = [f"{cliente[0]} - {cliente[1]}" for cliente in clientes]
        atualizar_lista_clientes(tree_clientes)
        atualizar_lista_pedidos(tree_pedidos)

    carregar_dados()

    root.mainloop()

if __name__ == "__main__":
    main()