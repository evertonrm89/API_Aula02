from sqlalchemy import create_engine, text

# Substitua 'sqlite:///teste.db' pelo URL do seu banco de dados
DATABASE_URL = 'sqlite:///biblioteca.db'
engine = create_engine(DATABASE_URL)

def consulta_aluno(id):
    try:
        sqlcomando = text ("SELECT * FROM Aluno WHERE id = :id")

        # Testa a conexão
        with engine.connect() as connection:
            resultado = connection.execute(sqlcomando, {"id":id})
            aluno = resultado.fetchone()
            if aluno:
                #print(aluno)
                return aluno
            else:
                #print("Aluno não encontrado.")
                return None

    except Exception as e:
        print(f"Erro consulta_aluno(id): {e}")
        return None

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
        print(f"Erro todos_alunos(): {e}")
    


# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição) e o adiciona no banco de dados.
def cria_livro(descricao=''):

    try:
        sqlcomando = text ("INSERT INTO Livro (descricao) VALUES (:descricao)")
        with engine.connect() as connection:
            connection.execute(sqlcomando, {"descricao":descricao})
            connection.commit()

    except Exception as e:
        print(f"Erro cria_livro(descricao=''): {e}")
        
def consulta_id_livro(id):
    try:
        sqlcomando = text ("SELECT * FROM Livro WHERE id_livro = :id")

        with engine.connect() as connection:
            resultado = connection.execute(sqlcomando, {"id":id})
            livro = resultado.fetchone()
        
            if livro:
                #print(livro)
                return livro
            else:
                #print("Livro não encontrado.")
                return None
            
    except Exception as e:
        print(f"Erro consulta_id_livro(id): {e}")
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

def empresta_livro(id_livro, id_aluno):
    try:
        livro = consulta_id_livro(id_livro)
        aluno = consulta_aluno(id_aluno)
        #livro = dict(livro)
        if livro is None:
            print("Livro não Existe.")
        elif aluno is None:
            print("Aluno não Existe")
        elif livro[1] is not None:
            print("Livro já emprestado.")
        else:
            print("Livro disponível para empréstimo.")
            sqlAlterar = text ("UPDATE Livro SET id_aluno = :id_A WHERE id_livro = :id_L")
            with engine.connect() as connection:
                connection.execute(sqlAlterar, {"id_A":id_aluno, "id_L":id_livro})
                connection.commit()
                livro = consulta_id_livro(id_livro)
                print(livro)

    except Exception as e:
        print(f"Erro (empresta livro): {e}")

# 4) Crie uma função devolve_livro, que recebe a id de um livro, e marca o livro como disponível.

def devolve_livro(id_livro):
    try:
        livro = consulta_id_livro(id_livro)
        if livro is None:
            print("Livro não Existe.")

        elif livro[1] is None:
            print("Livro não esta emprestado.")
        else:
            print("Livro Devolvido.")
            sqlAlterar = text ("UPDATE Livro SET id_aluno = null WHERE id_livro = :id_L")
            with engine.connect() as connection:
                connection.execute(sqlAlterar, {"id_L":id_livro})
                connection.commit()
                livro = consulta_id_livro(id_livro)
                print(livro)

    except Exception as e:
        print(f"Erro (devolve_livro(id_livro)): {e}")


if __name__ == "__main__":
    devolve_livro(5)