

def create(dadosAlunos, dadosProfessor, escolha, variavel1, variavel2, variavel3, variavel4, variavel5, variavel6, variavel7):
    if escolha == 1:
        dadosAlunos[variavel1] = {
        "idade" : variavel2,
        "peso" : variavel3,
        "altura" : variavel4,
        "sexo" : variavel5,
        "imc" : variavel6,
        "plano" : variavel7
        }

    else:
        dadosProfessor[variavel1] = {
            "cpf" : variavel2,
            "atuacao" : variavel3,
            "capacitacao": variavel4,
            "turno de trabalho": variavel5,
            "carga horaria" : variavel6,
            "salario" : variavel7 
        }
    return dadosAlunos, dadosProfessor
        
      
def read(dadosAlunos, dadosProfessor, usuario, nome):
    if (nome in dadosAlunos) or (nome in dadosProfessor):
        return 1  
    else:
        return 0

        
       
def update(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor):
    if usuario == "ALUNO":
        dadosAlunos[nome][campo] = novoValor
    else:
        dadosProfessor[nome][campo] = novoValor
    return dadosAlunos, dadosProfessor
    
    
    
       
    
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

    
    
 
