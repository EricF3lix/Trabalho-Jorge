from datetime import date, datetime
   
def defineSalario(areaAtuacao, capacitacao, cargaHoraria):
    if areaAtuacao in ("DANCA", "BOXE"):
        if(capacitacao == "ESTAGIARIO"):
            salario = 0
        elif (capacitacao == "FORMADO"):
            salario = (130.25*cargaHoraria)
        elif (capacitacao == "MESTRADO"):
            salario = (150.25*cargaHoraria)
        else:
            salario = (180.25*cargaHoraria)
        return salario
    
    else:
        if(capacitacao == "ESTAGIARIO"):
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

#finalizado


