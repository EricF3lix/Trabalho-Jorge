from CRUD import create, read, update, delete 
from logger import lerArquivoAluno, lerArquivoProfessor, salvarAlunoNoArquivo, salvarProfessorNoArquivo
from OperacaoMatematica import calcula_idade, defineSalario
from datetime import date, datetime

dadosAlunos = {}
dadosProfessor = {} 


def validaEscolha(escolha, opcoes):
    while escolha not in opcoes:
        escolha = input("Entrada inválida. Tente novamente: ")
    
    if escolha.isdigit():   
        escolha = int(escolha)  
        return escolha
    else:
        return escolha
    
    

def validaEntradaUsuario(tipo, entrada):
    repeticao = 1
    while repeticao == 1:
        entrada.strip()
        if tipo == "str":
            if entrada.isdigit() or entrada =="":
                entrada = input("Entrada inválida. Tente novamente: ").upper()
            else:
                return entrada.upper()
        elif tipo == "int":
            if entrada.isdigit():
                entrada = int(entrada)
                return entrada
            else:
                entrada = input("Entrada inválida. Tente novamente: ")
        
        elif tipo == "data":
            if entrada.isdigit():
                entrada = input("Entrada inválida. Tente novamente: ")
            else:
                auxiliar = entrada.split("/")
                hoje = date.today()
                if len(auxiliar) == 3:
                    dia = int(auxiliar[0])
                    mes = int(auxiliar[1])
                    ano = int(auxiliar[2])
                    if (dia >=1 and dia <=31) and (mes>=1 and mes<=12) and ano >= 1900 and ano <= hoje.year:
                        if dia == hoje.day and mes == hoje.month:
                            print("FELIZ ANIVERSÁRIO")
                        return entrada
                    else:
                        entrada = input("Entrada inválida. Tente novamente: ")
                else:
                    entrada = input("Entrada inválida. Tente novamente: ")
        
        elif tipo == "float":
            auxiliar = entrada.split(".")
            if len(auxiliar == 2):
                entrada = float(entrada)
                return entrada
            else:
                entrada = input("Entrada inválida. Tente novamente: ")
        


                


    
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
                nome = validaEntradaUsuario("str", nome)
                
                idade = input("Informe a data de nascimento no formato dd/mm/aaaa: ")
                idade = validaEntradaUsuario("data", idade)
                idade = calcula_idade(idade)
                
                peso = input("Informe o peso do aluno em kg: ")
                peso = validaEntradaUsuario("int", peso)
                
                altura = input("Informe a altura do aluno em cm: ")
                altura = validaEntradaUsuario("int", altura)

                sexo = input("Informe se é do sexo masculino ou feminino: ").upper()
                opcoesValidas = ["MASCULINO", "FEMININO"]
                sexo = validaEscolha(sexo, opcoesValidas)
                
                imc = input("Informe seu IMC em porcentagem: ")
                imc = validaEntradaUsuario("float", imc)
                
                plano = input("Informe o plano que o aluno deseja (mensal, trimestral, semestral ou anual): ").upper()
                opcoesValidas = ["MENSAL", "TRIMESTRAL", "SEMESTRAL", "ANUAL"]
                plano = validaEscolha(plano, opcoesValidas)
                
                dadosAlunos, dadosProfessor = create(dadosAlunos, dadosProfessor, cadastro, nome, idade, peso, altura, sexo, imc, plano)
            else:
                print("Vamos começar a cadastrar o Professor")
                nome = input("Informe o nome completo do professor: ").upper()
                nome = validaEntradaUsuario("str", nome)
                cpf = input("Informe o CPF do professor (somente digitos): ")
                cpf = validaEntradaUsuario("int", cpf)
                
                areaAtuacao = input("Informe a área de atuação do professor (danca, boxe, funcional ou musculacao): ").upper()
                opcoesValidas = ["DANCA", "BOXE", "FUNCIONAL", "MUSCULACAO"]
                areaAtuacao = validaEscolha (areaAtuacao, opcoesValidas)
                
                capacitacao = input("Informe a capacitação profissional do professor: (estagiario, formado, pos graduacao, mestrado ou doutorado)").upper()
                opcoesValidas = ["ESTAGIARIO", "FORMADO", "POS GRADUACAO", "MESTRADO", "DOUTORADO"]
                capacitacao = validaEscolha (capacitacao, opcoesValidas)
                
                turnoTrabalho = input("Informe o turno que o professor irá trabalhar (manha, tarde ou noite): ").upper()
                opcoesValidas = ["MANHA", "TARDE", "NOITE"]
                turnoTrabalho = validaEscolha(turnoTrabalho, opcoesValidas)
                cargaHoraria = input("Informe a carga horária semanal do professor: ")
                cargaHoraria = validaEntradaUsuario("int", cargaHoraria)
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
