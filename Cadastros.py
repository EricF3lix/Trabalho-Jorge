from datetime import date, datetime
from logger import salvarAlunoNoArquivo, salvarProfessorNoArquivo

def menuAluno(dadosAlunos):
    
    print("Vamos começar a cadastrar o Aluno.")
    nome = input("Informe o nome completo do aluno: ").upper()
    idade = input("Informe a data de nascimento no formato dd/mm/aaaa: ")
    idade = calcula_idade(idade)
    peso = int(input("Informe o peso do aluno em kg: "))
    altura = int(input("Informe a altura do aluno em cm: "))
    sexo = input("Informe se é do sexo masculino ou feminino: ").upper()
    plano = input("Informe o plano que o aluno deseja (mensal, trimestral, semestral ou anual): ").upper()
    
    dadosAlunos[nome] = {
        "idade" : idade,
        "peso" : peso,
        "altura" : altura,
        "sexo" : sexo,
        "plano" : plano
    }
    print(f"Aluno {nome} cadastrado com sucesso!\n")
    salvarAlunoNoArquivo(dadosAlunos)
    return dadosAlunos
    

def menuProfessor(dadosProfessor):
    
    print("Vamos começar a cadastrar o Professor")
    nome = input("Informe o nome completo do professor: ").upper()
    cpf = int(input("Informe o CPF do professor (somente digitos): "))
    areaAtuacao = input("Informe a área de atuação do professor (dança, boxe, funcional ou musculação): ").upper()
    capacitacao = input("Informe a capacitação profissional do professor: (estagiário, formado, pós graduação, mestrado ou doutorado)").upper()
    turnoTrabalho = input("Informe o turno que o professor irá trabalhar (manhã, tarde ou noite): ").upper()
    cargaHoraria = int(input("Informe a carga horária semanal do professor: "))
    salario = defineSalario(areaAtuacao, capacitacao, cargaHoraria)
    
    dadosProfessor[nome] = {
        "CPF" : cpf,
        "Atuação" : areaAtuacao,
        "Capacitação": capacitacao,
        "Turno de Trabalho": turnoTrabalho,
        "Carga Horária" : cargaHoraria,
        "Salário" : salario 
    }
    print("Professor cadastrado com sucesso!\n")
    salvarProfessorNoArquivo(dadosProfessor)
    return dadosProfessor
    
    
    
def defineSalario(areaAtuacao, capacitacao, cargaHoraria):
    if areaAtuacao in ("DANÇA", "BOXE"):
        if(capacitacao == "ESTAGIÁRIO"):
            salario = 0
        elif (capacitacao == "FORMADO"):
            salario = (130.25*cargaHoraria)
        elif (capacitacao == "MESTRADO"):
            salario = (150.25*cargaHoraria)
        else:
            salario = (180.25*cargaHoraria)
        return salario
    
    else:
        if(capacitacao == "ESTAGIÁRIO"):
            salario = 0
        elif (capacitacao == "FORMADO"):
            salario = (100.25*cargaHoraria)
        elif (capacitacao == "MESTRADO"):
            salario = (120.25*cargaHoraria)
        else:
            salario = (150.25*cargaHoraria)
        return salario


def calcula_idade(idade):
    nascimento = datetime.strptime(idade, "%d/%m/%Y").date()
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade
