from interfaceUsuario import imprimeUsuario, atualizaDados
from OperacaoMatematica import menuAluno, menuProfessor


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
    
    
    
       
    
def delete(dadosAlunos, dadosProfessor, usuario, nome):
    if usuario == "ALUNO":
        if nome in dadosAlunos:
            del dadosAlunos[nome]
            return dadosAlunos, dadosProfessor, 1
        else:
            return dadosAlunos, dadosProfessor, 0
    elif usuario == "PROFESSOR":
        if nome in dadosProfessor:
            del dadosProfessor[nome]
            return dadosAlunos, dadosProfessor, 1
        else:
            return dadosAlunos, dadosProfessor, 0

    
    
 
