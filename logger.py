LOG_FILE = 'dadosAcademia.txt'

def salvarAlunoNoArquivo(dadosAlunos):
    with open(LOG_FILE, 'a') as arquivo:
        for nome, info in dadosAlunos.items():
            linha = f"ALUNO: {nome} | " + " | ".join([f"{chave}: {valor}" for chave, valor in info.items()])      
            arquivo.write(linha + "\n") 

def salvarProfessorNoArquivo(dadosProfessor):
     with open(LOG_FILE, 'a') as arquivo:
        for nome, info in dadosProfessor.items():
            linha = f"Professor: {nome} | " + " | ".join([f"{chave}: {valor}" for chave, valor in info.items()]) 
            arquivo.write(linha + "\n") 

    