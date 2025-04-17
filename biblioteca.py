from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///biblioteca.db')
#   mas se quisesse uma solução mais robusta, poderia
# usar mudando o código muito pouco
# engine = create_engine('postgresql://usuario:senha@localhost:5432/imobiliaria')


# criar a tabela
def criar_tabelas():
    with engine.connect() as con:
        create_tabela_aluno = """
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
        rs = con.execute(create_tabela_aluno)
        create_tabela_livro = """
        CREATE TABLE IF NOT EXISTS Livro (
            id_livro INTEGER PRIMARY KEY,
            id_aluno INTEGER,
            descricao TEXT NOT NULL,
            FOREIGN KEY(id_aluno) REFERENCES Aluno(id)
        )
        """

        rs = con.execute(create_tabela_livro)

def criar_alunos():
    with engine.connect() as con:     
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com');"
        rs = con.execute(add_aluno)

def criar_livros():
    with engine.connect() as con:
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1,1,'Python completo e total')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias póstumas de brás cubas')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')"
        rs = con.execute(add_livro)

# criar_tabelas()
# criar_alunos()

class AlunoNaoExisteException(Exception):
    pass
# estamos definindo uma classe AlunoNaoExisteException, que
# herda todas as funcionalidades, todos os métodos e atributos,
# de Exception
# no lugar do pass, escreveríamos as mudanças,
# as coisas que AlunoNaoExisteException faz diferente de Exception
# mas não fizemos mudança nenhuma (por isso pass)

if __name__ == "__main__":
    pass