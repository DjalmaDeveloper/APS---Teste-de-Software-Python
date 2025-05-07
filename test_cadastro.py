from cadastro import *
from usuario import Usuario

def test_cadastrar_usuario_valido():
    u = cadastrar_usuario("João", "joao@empresa.com", "Senha123")
    assert u is not None
    assert u.email == "joao@empresa.com"

def test_cadastrar_usuario_nome_invalido():
    assert cadastrar_usuario("", "valido@empresa.com", "Senha123") is None

def test_cadastrar_usuario_email_invalido():
    assert cadastrar_usuario("João", "emailinvalido", "Senha123") is None

def test_cadastrar_usuario_senha_invalida():
    assert cadastrar_usuario("João", "joao@empresa.com", "123") is None

def test_atualizar_usuario():
    u = Usuario("João", "joao@email.com", "Senha123")
    assert atualizar_usuario(u, "Carlos", "carlos@email.com", "NovaSenha123")

def test_atualizar_usuario_apenas_nome():
    u = Usuario("A", "a@a.com", "Senha123")
    assert atualizar_usuario(u, "Novo Nome", "invalido", "fraca") == True

def test_excluir_usuario():
    u = cadastrar_usuario("Maria", "maria@empresa.com", "Senha123")
    assert excluir_usuario(u)
    assert not excluir_usuario(u)  # já foi excluído

def test_buscar_usuario_por_email():
    u = cadastrar_usuario("Pedro", "pedro@empresa.com", "Senha123")
    encontrado = buscar_usuario_por_email("pedro@empresa.com")
    assert encontrado is not None

def test_confirmar_senha():
    u = cadastrar_usuario("Laura", "laura@empresa.com", "Senha123")
    assert confirmar_senha(u, "Senha123")

def test_listar_usuarios():
    lista = listar_usuarios()
    assert isinstance(lista, list)

def test_alterar_parcial():
    u = cadastrar_usuario("Tiago", "tiago@empresa.com", "Senha123")
    assert alterar_parcial(u, "nome", "Lucas")
def test_confirmar_senha_falha():
    u = cadastrar_usuario("Test", "test@empresa.com", "Senha123")
    assert not confirmar_senha(u, "Errada")

def test_listar_usuarios_nao_vazio():
    lista = listar_usuarios()
    assert len(lista) >= 1

def test_alterar_parcial_email_invalido():
    u = cadastrar_usuario("Alvo", "alvo@empresa.com", "Senha123")
    resultado = alterar_parcial(u, "email", "invalido")
    assert not resultado
def test_alterar_parcial_invalido():
    u = cadastrar_usuario("João", "joao@empresa.com", "Senha123")
    resultado = alterar_parcial(u, "idade", "25")
    assert resultado is False

def test_cadastro_func_0():
    from cadastro import cadastro_func_0
    assert cadastro_func_0() == "CADASTRO_0"


def test_cadastro_func_1():
    from cadastro import cadastro_func_1
    assert cadastro_func_1() == "CADASTRO_1"


def test_cadastro_func_2():
    from cadastro import cadastro_func_2
    assert cadastro_func_2() == "CADASTRO_2"


def test_cadastro_func_3():
    from cadastro import cadastro_func_3
    assert cadastro_func_3() == "CADASTRO_3"


def test_cadastro_func_4():
    from cadastro import cadastro_func_4
    assert cadastro_func_4() == "CADASTRO_4"


def test_cadastro_func_5():
    from cadastro import cadastro_func_5
    assert cadastro_func_5() == "CADASTRO_5"


def test_cadastro_func_6():
    from cadastro import cadastro_func_6
    assert cadastro_func_6() == "CADASTRO_6"


def test_cadastro_func_7():
    from cadastro import cadastro_func_7
    assert cadastro_func_7() == "CADASTRO_7"


def test_cadastro_func_8():
    from cadastro import cadastro_func_8
    assert cadastro_func_8() == "CADASTRO_8"


def test_cadastro_func_9():
    from cadastro import cadastro_func_9
    assert cadastro_func_9() == "CADASTRO_9"


def test_cadastro_func_10():
    from cadastro import cadastro_func_10
    assert cadastro_func_10() == "CADASTRO_10"


def test_cadastro_func_11():
    from cadastro import cadastro_func_11
    assert cadastro_func_11() == "CADASTRO_11"


def test_cadastro_func_12():
    from cadastro import cadastro_func_12
    assert cadastro_func_12() == "CADASTRO_12"


def test_cadastro_func_13():
    from cadastro import cadastro_func_13
    assert cadastro_func_13() == "CADASTRO_13"


def test_cadastro_func_14():
    from cadastro import cadastro_func_14
    assert cadastro_func_14() == "CADASTRO_14"


def test_cadastro_func_15():
    from cadastro import cadastro_func_15
    assert cadastro_func_15() == "CADASTRO_15"


def test_cadastro_func_16():
    from cadastro import cadastro_func_16
    assert cadastro_func_16() == "CADASTRO_16"


def test_cadastro_func_17():
    from cadastro import cadastro_func_17
    assert cadastro_func_17() == "CADASTRO_17"