from Cadastros import menuAluno, menuProfessor 
from interfaceUsuario import imprimeUsuario, atualizaDados


def create(dadosAlunos, dadosProfessor, escolha):
    if escolha == 1:
        dadosAlunos = menuAluno(dadosAlunos)
    else:
        dadosProfessor = menuProfessor(dadosProfessor)
    return dadosAlunos, dadosProfessor
        
      
def read(dadosAlunos, dadosProfessor, usuario, nome):
    if (nome in dadosAlunos) or (nome in dadosProfessor):
        imprimeUsuario(dadosAlunos, dadosProfessor, usuario, nome)
        return 1  
    else:
        return 0

      
   
        
        
        
    
    
    
       
def update(dadosAlunos, dadosProfessor, usuario, nome):
    if nome in dadosAlunos or nome in dadosProfessor:
        dadosAlunos, dadosProfessor = atualizaDados(dadosAlunos, dadosProfessor, usuario, nome)
        return dadosAlunos, dadosProfessor, 1
    else:
        return dadosAlunos, dadosProfessor, 0
    
    
    
       
    
def delete(dadosAlunos, dadosProfessor):
    usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()
    if usuario == "ALUNO":
        nome = input("Informe o nome do aluno que deseja deletar: ").upper()
        if nome in dadosAlunos:
            confirmacao = input(f"Tem certeza que deseja deletar o aluno {nome}? [s/n]: ").lower()
            if confirmacao == 's':
                del dadosAlunos[nome]  
                print(f"Aluno {nome} deletado com sucesso!")
            else:
                print("Deleção cancelada.")
        else:
            print("Aluno não encontrado.")       
    elif usuario == "PROFESSOR":
        nome = input("Informe o nome do professor que deseja deletar: ").upper()
        if nome in dadosProfessor:
            confirmacao = input(f"Tem certeza que deseja deletar o professor {nome}? (s/n): ").lower()
            if confirmacao == 's':
                del dadosProfessor[nome] 
                print(f"Professor {nome} deletado com sucesso!")
            else:
                print("Deleção cancelada.")
        else:
            print("Professor não encontrado.")
    else:
        print("Entrada inválida. Tente novamente.")
    return dadosAlunos, dadosProfessor  

    
    
 
