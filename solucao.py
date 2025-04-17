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
def cria_livro(descricao=''):

    try:
        sqlcomando = text ("INSERT INTO Livro (descricao) VALUES (:descricao)")
        with engine.connect() as connection:
            connection.execute(sqlcomando, {"descricao":descricao})
            connection.commit()

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        
def consulta_id_livro(id):
    try:
        sqlcomando = text ("SELECT * FROM Livro WHERE id_livro = :id")

        with engine.connect() as connection:
            resultado = connection.execute(sqlcomando, {"id":id})
            livro = resultado.fetchone()
        
            if livro:
                print(livro)
                return livro
            else:
                print("Livro não encontrado.")
                return None
            
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

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

# 3) Crie uma função empresta_livro, 
# que recebe a id de um livro, a id de um aluno e marca o livro como emprestado pelo aluno.

def empresta_livro(id_livro):
    try:
        livro = consulta_id_livro(id_livro)
        #livro = dict(livro)
        if livro is None:
            print("Livro não encontrado.")
        elif livro[1] is not None:
            print("Livro já emprestado.")
        else:
            print("Livro disponível para empréstimo.")
            
        

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados (empresta livro): {e}")

if __name__ == "__main__":
    empresta_livro(1)