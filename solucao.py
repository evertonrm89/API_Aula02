from sqlalchemy import create_engine, text

# Substitua 'sqlite:///teste.db' pelo URL do seu banco de dados
DATABASE_URL = 'sqlite:///biblioteca.db'

def consulta_aluno(id):
    try:
        # Cria o engine de conexão
        engine = create_engine(DATABASE_URL)
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
        engine = create_engine(DATABASE_URL)
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
    

if __name__ == "__main__":
    todos_alunos()
    # Aqui você pode adicionar outras chamadas de função ou lógica do seu programa