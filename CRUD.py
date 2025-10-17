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
        
        
        
    
    
    
       
def update(dadosAlunos, dadosProfessor):
    usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()

    
    if usuario == "ALUNO":
        nome = input("Informe o nome do aluno que deseja atualizar: ").upper()
        if nome in dadosAlunos:
            print("Dados atuais do aluno:")
            print(f"Nome: {nome}")
            for chave, valor in dadosAlunos[nome].items():
                print(f"{chave}: {valor}")
            campo = input("Qual campo você deseja atualizar? ").lower()
            if campo in dadosAlunos[nome]:  
                novo_valor = input(f"Informe o novo valor para {campo}: ")
                dadosAlunos[nome][campo] = novo_valor  
                print(f"{campo} atualizado com sucesso para {novo_valor}!")
            else:
                print("Campo não encontrado nos dados do aluno.")
        else:
            print("Aluno não encontrado.")
    elif usuario == "PROFESSOR":
        nome = input("Informe o nome do professor que deseja atualizar: ").upper()
        if nome in dadosProfessor:
            print("Dados atuais do professor:")
            print(f"Nome: {nome}")
            for chave, valor in dadosProfessor[nome].items():
                print(f"{chave}: {valor}")
            campo = input("Qual campo você deseja atualizar? ").lower()
            if campo in dadosProfessor[nome]:  
                novo_valor = input(f"Informe o novo valor para {campo}: ")
                dadosProfessor[nome][campo] = novo_valor  
                print(f"{campo} atualizado com sucesso para {novo_valor}!")
            else:
                print("Campo não encontrado nos dados do professor.")
        else:
            print("Professor não encontrado.")
    else:
        print("Entrada inválida. Tente novamente.")
    return dadosAlunos, dadosProfessor
    
    
    
       
    
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

    
    
 
