from CRUD import create, read, update, delete 
from logger import lerArquivoAluno, lerArquivoProfessor, salvarAlunoNoArquivo, salvarProfessorNoArquivo
from OperacaoMatematica import defineSalario, calcula_idade


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



def escolheAlunoOuProfessor():
    usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()
    opcoesUsuario = ["ALUNO", "PROFESSOR"]
    usuario = validaEscolha(usuario, opcoesUsuario)
    nome = input(f"Informe o nome do {usuario} que deseja ver os dados: ").upper()
    return usuario, nome



def menuInicial(dadosAlunos, dadosProfessor):
    programa = 1
    while programa == 1:
        print("Seja bem vindo ao sistema da F3 Fitness. Digite:")
        print("1 - Cadastrar alunos ou professor")
        print("2 - Ver dados dos usuários do sistema")
        print("3 - Atualizar dados de Cadastro")
        print("4 - Remover usuário do sistema")
        print("5 - Ver todos os produtos fornecidos pela F3 Fitness")
        print("0 - Fechar programa")
        escolha = input("Escolha o que você deseja fazer: ")
        opcoes = ["0", "1", "2", "3", "4", "5"]
        escolha = validaEscolha(escolha, opcoes)

        if escolha == 0:
            print("Programa encerrado")
            programa = 0
            return dadosAlunos, dadosProfessor
        
        elif escolha == 1:
            print("1 - Cadastrar ALUNO")
            print("2 - Cadastrar PROFESSOR")
            escolha = input("escolha uma das opções: ")
            opcoesCadastro = ["1", "2"]
            escolha = validaEscolha(escolha, opcoesCadastro)
            dadosAlunos, dadosProfessor = create(dadosAlunos, dadosProfessor, escolha)
                
        elif escolha == 2:
            usuario, nome = escolheAlunoOuProfessor()
                    
            resultado = read(dadosAlunos, dadosProfessor, usuario, nome)
            if resultado == 0:
                print("Não foi possivel encontrar o usuário.")

        elif escolha == 3:
            usuario, nome = escolheAlunoOuProfessor()
            dadosAlunos, dadosProfessor, resultado = update(dadosAlunos, dadosProfessor, usuario, nome)
            if resultado == 0:
                print("Não foi possivel encontrar o usuário")
                
        elif escolha == 4:
            usuario, nome = escolheAlunoOuProfessor()
            dadosAlunos, dadosProfessor, resultado = delete(dadosAlunos, dadosProfessor, usuario, nome)
            if resultado == 0:
                print("Não foi possível encontrar o usuário.")    
        
        elif escolha == 5:
            print("Os nossos produtos com os respectivos valores são:")   
            print("Plano MENSAL - R$ 90.00") 
            print("Plano TRIMESTRAL - R$ 260.00")
            print("Plano SEMESTRAL - R$ 500.00")
            print("Plano ANUAL - R$ 950.00")
            print("\n")        


    


dadosAlunos = lerArquivoAluno(dadosAlunos)
dadosProfessor = lerArquivoProfessor(dadosProfessor)

dadosAlunos, dadosProfessor = menuInicial(dadosAlunos, dadosProfessor)
salvarAlunoNoArquivo(dadosAlunos)
salvarProfessorNoArquivo(dadosProfessor)



        
    
    
    

      
    
