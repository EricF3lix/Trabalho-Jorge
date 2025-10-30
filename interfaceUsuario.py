import CRUD 
from logger import lerArquivoAluno, lerArquivoProfessor

dadosAlunos = {}
dadosProfessor = {} 


def validaEscolha(escolha, opcoes):
    while escolha not in opcoes:
        escolha = input("Entrada inválida. Tente novamente: ")
    
    if escolha == "USUARIO" or escolha == "CADASTRO":
        return escolha
    else:   
        escolha = int(escolha)  
        return escolha
    
        
        
def imprimeUsuario(dadosAlunos, dadosProfessor, usuario, nome):
    if usuario == "ALUNO":
        print(f"nome : {nome}")
        for chave, valor in dadosAlunos[nome].items():
            print(f"{chave} : {valor}")
    elif usuario == "PROFESSOR":
        print(f"nome : {nome}")
        for chave, valor in dadosProfessor[nome].items():
            print(f"{chave} : {valor}")

def atualizaDados(dadosAlunos, dadosProfessor, usuario, nome):
    if usuario=="ALUNO":
        print(f"Dados atuais do {usuario}:")
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
        print(f"Dados atuais do {usuario}:")
        print(f"Nome: {nome}")
        for chave, valor in dadosProfessor[nome].items():
            print(f"{chave}: {valor}")
        campo = input("Qual campo você deseja atualizar? ").lower()
        if campo in dadosProfessor[nome]:  
            novo_valor = input(f"Informe o novo valor para {campo}: ")
            dadosProfessor[nome][campo] = novo_valor  
            print(f"{campo} atualizado com sucesso para {novo_valor}!")
        else:
            print("Campo não encontrado nos dados do aluno.")



def menu(dadosAlunos, dadosProfessor):
    programa = 1
    while programa == 1:
        print("Seja bem vindo ao sistema da F3 Fitness. Digite:")
        print("1 - Cadastrar alunos ou professor")
        print("2 - Ver dados dos usuários do sistema")
        print("3 - Atualizar dados de Cadastro")
        print("4 - Remover usuário do sistema")
        print("5 - Ver todos os produtos fornecidos pela F3 Fitness")
        print("0 - Fechar programa")
        escolha = int(input("Escolha o que você deseja fazer: "))
        opcoes = ["0", "1", "2", "3", "4", "5"]
        escolha = validaEscolha(escolha, opcoes)
        print("\n")
           
        if escolha == 0:
            print("Programa encerrado")
            programa = 0
            return dadosAlunos, dadosProfessor
        
        elif escolha == 1:
            print("1 - Cadastrar ALUNO")
            print("2 - Cadastrar PROFESSOR")
            cadastro = input("escolha uma das opções: ")
            opcoesCadastro = ["1", "2"]
            cadastro = validaEscolha(cadastro, opcoesCadastro, cadastro)
            dadosAlunos, dadosProfessor = CRUD.create(dadosAlunos, dadosProfessor, cadastro)
        
        elif escolha == 2:
            usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()
            opcoesUsuario = ["ALUNO", "PROFESSOR"]
            usuario = validaEscolha(usuario, opcoesUsuario)
            nome = input(f"Informe o nome do {usuario} que deseja ver os dados: ").upper()
            CRUD.read(dadosAlunos, dadosProfessor, usuario, nome)

        elif escolha == 3:
            usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()
            opcoesUsuario = ["ALUNO", "PROFESSOR"]
            usuario = validaEscolha(usuario, opcoesUsuario)
            nome = input(f"Informe o nome do {usuario} que deseja ver os dados: ").upper()
            CRUD.update(dadosAlunos, dadosProfessor, usuario, nome)
                
        elif escolha == 4:
            CRUD.delete(dadosAlunos, dadosProfessor)
            
        elif escolha == 5:
            print("Os nossos produtos com os respectivos valores são:")   
            print("Plano MENSAL - R$ 90.00") 
            print("Plano TRIMESTRAL - R$ 260.00")
            print("Plano SEMESTRAL - R$ 500.00")
            print("Plano ANUAL - R$ 950.00")
            print("\n")        
        else:
            escolha = int(input("Entrada inválida. Tente novamente: "))

dadosAlunos = lerArquivoAluno(dadosAlunos)
dadosProfessor = lerArquivoProfessor(dadosProfessor)

dadosAlunos, dadosProfessor = menu(dadosAlunos, dadosProfessor)



        
    
    
    

      
    
