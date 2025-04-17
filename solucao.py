from sqlalchemy import create_engine, text

# Substitua 'sqlite:///teste.db' pelo URL do seu banco de dados
DATABASE_URL = 'sqlite:///biblioteca.db'
engine = create_engine(DATABASE_URL)

def consulta_aluno(id):
    try:
        sqlcomando = text ("SELECT * FROM Aluno WHERE id = :id")

        # Testa a conexão
        with engine.connect() as connection:
            print("Conexão com o banco de dados bem-sucedida!")
            resultado = connection.execute(sqlcomando, {"id":id})
            aluno = resultado.fetchone()
            if aluno:
                print(aluno)
            else:
                print("Aluno não encontrado.")

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# 1b) Crie uma função todos_alunos que retorna uma lista com um dicionário para cada aluno.
def todos_alunos():
    try:
        # Cria o engine de conexão
        
        sqlcomando = text ("SELECT * FROM Aluno")

        # Testa a conexão
        with engine.connect() as connection:
            print("Conexão com o banco de dados bem-sucedida!")
            resultado = connection.execute(sqlcomando)
            alunos = []
            while True:
                aluno = resultado.fetchone()
                if aluno is None:
                    break
                aluno = dict(aluno._mapping) 
                alunos.append(aluno)
        print(alunos)


            #alunos = resultado.fetchall()
            #for aluno in alunos:
            #    print(aluno)

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    


# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição) e o adiciona no banco de dados.
def cria_livro(id, descricao):
        with engine.connect() as connection:
            sqlcomando = text ("INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (:id, :id_aluno, :descricao)")
            connection.execute(sqlcomando, ({'id':id, 'id_aluno':None, 'descricao':descricao}))

def todos_livros():
        # Cria o engine de conexão  
        sqlcomando = text ("SELECT * FROM Livro")
        # Testa a conexão
        with engine.connect() as connection:
            resultado = connection.execute(sqlcomando)
            livros = []
            while True:
                livro = resultado.fetchone()
                if livro is None:
                    break
                livro = dict(livro._mapping) 
                livros.append(livro)
        print(livros)

if __name__ == "__main__":
    cria_livro(5, "Livro de Desenvolvimento de APIs")
    todos_livros()