from CRUD import create, read, update, delete 
from logger import lerArquivoAluno, lerArquivoProfessor, salvarAlunoNoArquivo, salvarProfessorNoArquivo
from OperacaoMatematica import calcula_idade, defineSalario

dadosAlunos = {}
dadosProfessor = {} 


def validaEscolha(escolha, opcoes):
    while escolha not in opcoes:
        escolha = input("Entrada inválida. Tente novamente: ")
    
    if escolha == "ALUNO" or escolha == "PROFESSOR":
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

def escolheAlunoOuProfessor(usuario, nome):
    usuario = input("Informe se é ALUNO ou PROFESSOR: ").upper()
    opcoesUsuario = ["ALUNO", "PROFESSOR"]
    usuario = validaEscolha(usuario, opcoesUsuario)
    nome = input(f"Informe o nome do {usuario} que deseja ver os dados: ").upper()
    return usuario, nome



def menuInicial(dadosAlunos, dadosProfessor):
    programa = 1
    usuario = ''
    nome = ''
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
            cadastro = input("escolha uma das opções: ")
            opcoesCadastro = ["1", "2"]
            cadastro = validaEscolha(cadastro, opcoesCadastro)
            
            if cadastro == 1:
                print("Vamos começar a cadastrar o Aluno.")
                nome = input("Informe o nome completo do aluno: ").upper()
                idade = input("Informe a data de nascimento no formato dd/mm/aaaa: ")
                idade = calcula_idade(idade)
                peso = int(input("Informe o peso do aluno em kg: "))
                altura = int(input("Informe a altura do aluno em cm: "))
                sexo = input("Informe se é do sexo masculino ou feminino: ").upper()
                imc = float (input("Informe seu IMC em porcentagem: "))
                plano = input("Informe o plano que o aluno deseja (mensal, trimestral, semestral ou anual): ").upper()
                dadosAlunos, dadosProfessor = create(dadosAlunos, dadosProfessor, cadastro, nome, idade, peso, altura, sexo, imc, plano)
            
            else:
                print("Vamos começar a cadastrar o Professor")
                nome = input("Informe o nome completo do professor: ").upper()
                cpf = int(input("Informe o CPF do professor (somente digitos): "))
                areaAtuacao = input("Informe a área de atuação do professor (danca, boxe, funcional ou musculacao): ").upper()
                capacitacao = input("Informe a capacitação profissional do professor: (estagiario, formado, pos graduacao, mestrado ou doutorado)").upper()
                turnoTrabalho = input("Informe o turno que o professor irá trabalhar (manhã, tarde ou noite): ").upper()
                cargaHoraria = int(input("Informe a carga horária semanal do professor: "))
                salario = defineSalario(areaAtuacao, capacitacao, cargaHoraria)
    
                dadosAlunos, dadosProfessor = create(dadosAlunos, dadosProfessor, cadastro,  nome, cpf, areaAtuacao, capacitacao, turnoTrabalho, cargaHoraria, salario)
                
        elif escolha == 2:
            usuario, nome = escolheAlunoOuProfessor(usuario, nome)    
            resultado = read(dadosAlunos, dadosProfessor, usuario, nome)
            if resultado == 1:
                imprimeUsuario(dadosAlunos, dadosProfessor, usuario, nome)
            if resultado == 0:
                print("Não foi possivel encontrar o usuário.")

        elif escolha == 3:
            usuario, nome = escolheAlunoOuProfessor(usuario, nome)
            
            if usuario == "ALUNO":
                if nome in dadosAlunos:
                    print(f"Dados atuais do {usuario}:")
                    print(f"Nome: {nome}")
                    for chave, valor in dadosAlunos[nome].items():
                        print(f"{chave}: {valor}")
                    campo = input("Qual campo você deseja atualizar? ").lower()
                    if campo in dadosAlunos[nome]:  
                        novoValor = input(f"Informe o novo valor para {campo}: ")
                        if campo == "idade" or campo == "peso" or campo == "altura" or campo == "imc":
                            novoValor = int(novoValor)
                        dadosAlunos, dadosProfessor = update(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor)
                    else:
                        print("Campo não encontrado")
                else:
                    print("Aluno não encontrado")
            
            elif usuario == "PROFESSOR":
                if nome in dadosProfessor:
                    print(f"Dados atuais do {usuario}:")
                    print(f"Nome: {nome}")
                    for chave, valor in dadosProfessor[nome].items():
                        print(f"{chave}: {valor}")
                    campo = input("Qual campo você deseja atualizar? ").lower()
                    if campo in dadosProfessor[nome]:  
                        novoValor = input(f"Informe o novo valor para {campo}: ")
                        if campo == "cpf" or campo == "carga horaria":
                            novoValor = int(novoValor)
                        elif campo == salario:
                            novoValor = float(novoValor)
                        dadosAlunos, dadosProfessor = update(dadosAlunos, dadosProfessor, usuario, nome, campo, novoValor)
                    else:
                        print("Campo não encontrado")
                else:
                    print("Aluno não encontrado")

        elif escolha == 4:
            usuario, nome = escolheAlunoOuProfessor(usuario, nome)
            dadosAlunos, dadosProfessor, resultado = delete(dadosAlunos, dadosProfessor, usuario, nome)
            if resultado == 1:
                print("Usuário removido com sucesso")
            else:
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

