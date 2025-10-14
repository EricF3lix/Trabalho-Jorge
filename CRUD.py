from Cadastros import menuAluno, menuProfessor



def create(dadosAlunos, dadosProfessor):
    print("1 - Cadastrar ALUNO")
    print("2 - Cadastrar PROFESSOR")
    escolha = int(input("escolha uma das opções: "))
    
    repeticao = 1
    while repeticao == 1:
        if escolha == 1:
            dadosAlunos = menuAluno(dadosAlunos)
            repeticao = 0
        elif escolha == 2:
            dadosProfessor = menuProfessor(dadosProfessor)
            repeticao = 0
        else:
            escolha = int(input("Entrada inválida. Tente novamente: "))
    return dadosAlunos, dadosProfessor
        
      
def read(dadosAlunos, dadosProfessor):
    usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()
    if usuario == "ALUNO":
        nome = input("Informe o nome do aluno que deseja ver os dados: ").upper()
        if nome in dadosAlunos:
            print(f"nome : {nome}")
            for chave, valor in dadosAlunos[nome].items():
                print(f"{chave} : {valor}")
        else:
            print("Aluno não encontrado.")
    elif usuario == "PROFESSOR":
        nome = input("Informe o nome do professor que deseja ver os dados: ").upper()
        if nome in dadosProfessor:
            print(f"nome : {nome}")
            for chave, valor in dadosProfessor[nome].items():
                print(f"{chave} : {valor}")
        else:
            print("Professor não encontrado.")
    else:
        print("Entrada inválida. Tente novamente.")
        
        
        
    
    
    
       
    
#def update():
    
    
       
    
#def delete():
    
    
 
