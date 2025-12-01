from logger import salvarAlunoNoArquivo, salvarProfessorNoArquivo

def create(dadosAlunos, dadosProfessor, usuario, nome, caracteristicas2, caracteristicas3, caracteristicas4, caracteristicas5, caracteristicas6, caracteristicas7):
    if usuario == "ALUNO":
        dadosAlunos[nome] = {
        "idade" : caracteristicas2,
        "peso" : caracteristicas3,
        "altura" : caracteristicas4,
        "sexo" : caracteristicas5,
        "imc" : caracteristicas6,
        "plano" : caracteristicas7
        }
        salvarAlunoNoArquivo(dadosAlunos)
    else:
        dadosProfessor[nome] = {
            "cpf" : caracteristicas2,
            "atuacao" : caracteristicas3,
            "capacitacao": caracteristicas4,
            "turno": caracteristicas5,
            "carga horaria" : caracteristicas6,
            "salario" : caracteristicas7 
        }
        salvarProfessorNoArquivo(dadosProfessor)
   
    return dadosAlunos, dadosProfessor
        
      
def read(dadosAlunos, dadosProfessor, usuario, nome):
    
    if usuario == "ALUNO":
        if nome in dadosAlunos:
            return 1
        else:
            return 0 
    
    elif usuario == "PROFESSOR":
        if nome in dadosProfessor:
            return 1
        else:
            return 0
    else:
        return 0

        
       
def update(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor):
    if usuario == "ALUNO":
        dadosAlunos[nome][campo] = novoValor
        resultado = 1
        salvarAlunoNoArquivo(dadosAlunos)
        return dadosAlunos, dadosProfessor, resultado
    elif usuario == "PROFESSOR":
        dadosProfessor[nome][campo] = novoValor
        resultado = 1   
        salvarProfessorNoArquivo(dadosProfessor)
        return dadosAlunos, dadosProfessor, resultado
    
    return dadosAlunos, dadosProfessor, 0
    
    
    
    
       
    
def delete(dadosAlunos, dadosProfessor, usuario, nome):
    if usuario == "ALUNO":
        if nome in dadosAlunos:
            del dadosAlunos[nome]
            salvarAlunoNoArquivo(dadosAlunos)
            return dadosAlunos, dadosProfessor, 1
        else:
            return dadosAlunos, dadosProfessor, 0
    elif usuario == "PROFESSOR":
        if nome in dadosProfessor:
            del dadosProfessor[nome]
            salvarProfessorNoArquivo(dadosProfessor)
            return dadosAlunos, dadosProfessor, 1
        else:
            return dadosAlunos, dadosProfessor, 0

#finalizado
 
