from CRUD import create, read, update, delete




def test_create_aluno():
    dadosAlunos = {}
    dadosProfessor = {}

    dadosAlunos, dadosProfessor = create(dadosAlunos, dadosProfessor,"ALUNO","ERIC", 20, 70.5 , 175, "MASCULINO", 12.0, "MENSAL" )

    assert "ERIC" in dadosAlunos
    assert dadosAlunos["ERIC"]["idade"] == 20
    assert dadosAlunos["ERIC"]["peso"] == 70.5
    assert dadosAlunos["ERIC"]["altura"] == 175
    assert dadosAlunos["ERIC"]["sexo"] == "MASCULINO"
    assert dadosAlunos["ERIC"]["imc"] == 12.0
    assert dadosAlunos["ERIC"]["plano"] == "MENSAL"


def test_create_professor():
    dadosAlunos = {}
    dadosProfessor = {}

    dadosAlunos, dadosProfessor = create(dadosAlunos, dadosProfessor,"PROFESSOR","JOAO",123,"BOXE","MESTRADO", "MANHA",40,5000.0)

    assert "JOAO" in dadosProfessor
    assert dadosProfessor["JOAO"]["cpf"] == 123
    assert dadosProfessor["JOAO"]["atuacao"] == "BOXE"
    assert dadosProfessor["JOAO"]["capacitacao"] == "MESTRADO"
    assert dadosProfessor["JOAO"]["turno"] == "MANHA"
    assert dadosProfessor["JOAO"]["carga horaria"] == 40
    assert dadosProfessor["JOAO"]["salario"] == 5000.0




def test_read_aluno():
    dadosAlunos = {"ERIC": {"idade": 20}}
    dadosProfessor = {}

    resultado = read(dadosAlunos, dadosProfessor, "ALUNO", "ERIC")
    assert resultado == 1
    resultado = read(dadosAlunos, dadosProfessor, "ALUNO", "")
    assert resultado == 0


def test_read_professor():
    dadosAlunos = {}
    dadosProfessor = {"JOAO": {"cpf": 123}}

    resultado = read(dadosAlunos, dadosProfessor, "PROFESSOR", "JOAO")
    assert resultado == 1
    resultado = read(dadosAlunos, dadosProfessor, "PROFESSOR", "")
    assert resultado == 0




def test_update_aluno():
    dadosAlunos = {"ERIC": {"idade": 20}}
    dadosProfessor = {}

    dadosAlunos, dadosProfessor, resultado = update(dadosAlunos, dadosProfessor, "ALUNO", "ERIC", "idade", 30)
    assert resultado == 1
    assert dadosAlunos["ERIC"]["idade"] == 30


def test_update_professor():
    dadosAlunos = {}
    dadosProfessor = {"JOAO": {"cpf": 123}}

    dadosAlunos, dadosProfessor, resultado = update(dadosAlunos, dadosProfessor, "PROFESSOR", "JOAO", "cpf", 999)
    assert resultado == 1
    assert dadosProfessor["JOAO"]["cpf"] == 999




def test_delete_aluno():
    dadosAlunos = {"ERIC": {"idade": 20}}
    dadosProfessor = {}

    dadosAlunos, dadosProfessor, resultado = delete(dadosAlunos, dadosProfessor, "ALUNO", "ERIC")
    assert resultado == 1
    assert "ERIC" not in dadosAlunos


def test_delete_professor():
    dadosAlunos = {}
    dadosProfessor = {"JOAO": {"cpf": 123}}

    dadosAlunos, dadosProfessor, resultado = delete(dadosAlunos, dadosProfessor, "PROFESSOR", "JOAO")
    assert resultado == 1
    assert "JOAO" not in dadosProfessor
