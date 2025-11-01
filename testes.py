import pytest
from CRUD import create, read, update, delete


def validaCreate(dadosAlunos, dadosProfessor, escolha, nome):
    if escolha == 1:  
        if nome in dadosAlunos:
            print("Função funcionando perfeitamente para Alunos")
            return 1
        else:
            print("Houve algum problema em cadastrar um novo Aluno")
            return 0
    else: 
        if nome in dadosProfessor:
            print("Função funcionando perfeitamente para Professores")
            return 1
        else:
            print("Houve algum problema em cadastrar um novo Professor")
            return 0




def validaDelete(dadosAlunos, dadosProfessor, usuario, nome):
    if usuario.upper() == "ALUNO":  
        if nome  not in dadosAlunos:
            print("Função funcionando perfeitamente para Alunos")
            return 1
        else:
            print("Houve algum problema em cadastrar um novo Aluno")
            return 0
    else: 
        if nome  not in dadosProfessor:
            print("Função funcionando perfeitamente para Professores")
            return 1
        else:
            print("Houve algum problema em cadastrar um novo Professor")
            return 0




def validaRead(dadosAlunos, dadosProfessor, usuario, nome):
    resultado = read(dadosAlunos, dadosProfessor, usuario, nome)
    
    if usuario.upper() == "ALUNO":
        if resultado == 1 and nome in dadosAlunos:
            print(f"Função read funcionando corretamente para o aluno '{nome}'")
            return 1
        elif resultado == 0 and nome not in dadosAlunos:
            print(f"Função read corretamente não encontrou o aluno '{nome}'")
            return 1
        else:
            print(f"Houve algum problema ao ler o aluno '{nome}'")
            return 0

    elif usuario.upper() == "PROFESSOR":
        if resultado == 1 and nome in dadosProfessor:
            print(f"Função read funcionando corretamente para o professor '{nome}'")
            return 1
        elif resultado == 0 and nome not in dadosProfessor:
            print(f"Função read corretamente não encontrou o professor '{nome}'")
            return 1
        else:
            print(f"Houve algum problema ao ler o professor '{nome}'")
            return 0


   





def validaUpdate(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor):
    if usuario.upper() == "ALUNO":
        dadosAlunos, dadosProfessor = update(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor)
        if dadosAlunos[nome][campo] == novoValor:
            print("Função funcionando perfeitamente para atualizar dados do aluno")
            return 1
        else:
            print("Houve algum problema em atualizar o campo do aluno")
            return 0

    elif usuario.upper() == "PROFESSOR":
        dadosAlunos, dadosProfessor = update(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor)
        if dadosProfessor[nome][campo] == novoValor:
            print("Função funcionando perfeitamente para atualizar dados do professor")
            return 1
        else:
            print("Houve algum problema em atualizar o campo do professor")
            return 0



        
        



