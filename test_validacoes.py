from validacoes import *

def test_valida_email():
    assert valida_email("teste@dominio.com")
    assert not valida_email("invalido")

def test_valida_senha():
    assert valida_senha("Senha123")
    assert not valida_senha("abc")

def test_senha_forte():
    assert senha_forte("Senha123@")
    assert not senha_forte("senha123")

def test_valida_nome():
    assert valida_nome("Lucas")
    assert not valida_nome("")

def test_valida_id():
    assert valida_id(10)
    assert not valida_id(-1)

def test_valida_dominio_email():
    assert valida_dominio_email("usuario@empresa.com")
    assert not valida_dominio_email("usuario@gmail.com")

def test_valida_login():
    assert valida_login("lucas@empresa.com", "Senha123")
    assert not valida_login("lucas", "123")
def test_valida_dominio_email_falha():
    assert not valida_dominio_email("teste@outra.com")

def test_senha_forte_falha():
    assert not senha_forte("Senha123")
def test_senha_forte_sem_especial():
    assert not senha_forte("Senha123")  # válida mas sem especial

def test_valida_dominio_email_none():
    assert not valida_dominio_email(None)

def test_validacoes_func_0():
    from validacoes import validacoes_func_0
    assert validacoes_func_0() == "VALIDACOES_0"


def test_validacoes_func_1():
    from validacoes import validacoes_func_1
    assert validacoes_func_1() == "VALIDACOES_1"


def test_validacoes_func_2():
    from validacoes import validacoes_func_2
    assert validacoes_func_2() == "VALIDACOES_2"


def test_validacoes_func_3():
    from validacoes import validacoes_func_3
    assert validacoes_func_3() == "VALIDACOES_3"


def test_validacoes_func_4():
    from validacoes import validacoes_func_4
    assert validacoes_func_4() == "VALIDACOES_4"


def test_validacoes_func_5():
    from validacoes import validacoes_func_5
    assert validacoes_func_5() == "VALIDACOES_5"


def test_validacoes_func_6():
    from validacoes import validacoes_func_6
    assert validacoes_func_6() == "VALIDACOES_6"


def test_validacoes_func_7():
    from validacoes import validacoes_func_7
    assert validacoes_func_7() == "VALIDACOES_7"


def test_validacoes_func_8():
    from validacoes import validacoes_func_8
    assert validacoes_func_8() == "VALIDACOES_8"


def test_validacoes_func_9():
    from validacoes import validacoes_func_9
    assert validacoes_func_9() == "VALIDACOES_9"


def test_validacoes_func_10():
    from validacoes import validacoes_func_10
    assert validacoes_func_10() == "VALIDACOES_10"


def test_validacoes_func_11():
    from validacoes import validacoes_func_11
    assert validacoes_func_11() == "VALIDACOES_11"


def test_validacoes_func_12():
    from validacoes import validacoes_func_12
    assert validacoes_func_12() == "VALIDACOES_12"


def test_validacoes_func_13():
    from validacoes import validacoes_func_13
    assert validacoes_func_13() == "VALIDACOES_13"


def test_validacoes_func_14():
    from validacoes import validacoes_func_14
    assert validacoes_func_14() == "VALIDACOES_14"


def test_validacoes_func_15():
    from validacoes import validacoes_func_15
    assert validacoes_func_15() == "VALIDACOES_15"


def test_validacoes_func_16():
    from validacoes import validacoes_func_16
    assert validacoes_func_16() == "VALIDACOES_16"


def test_validacoes_func_17():
    from validacoes import validacoes_func_17
    assert validacoes_func_17() == "VALIDACOES_17"