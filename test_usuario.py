from usuario import Usuario

def test_criacao_usuario():
    u = Usuario("Ana", "ana@email.com", "Senha123")
    assert u.nome == "Ana"

def test_atualizar_nome():
    u = Usuario("Ana", "ana@email.com", "Senha123")
    assert u.atualizar_nome("Clara")

def test_redefinir():
    u = Usuario("Ana", "ana@email.com", "Senha123")
    u.redefinir()
    assert u.email == "email@dominio.com"
    assert u.senha == "Senha123"

def test_estado_conta():
    u = Usuario("Paulo", "paulo@email.com", "Senha123")
    u.desativar_conta()
    assert not u.ativo
    u.ativar_conta()
    assert u.ativo

def test_exibir_resumo():
    u = Usuario("Ana", "ana@email.com", "Senha123")
    assert "Usuário: Ana" in u.exibir_resumo()
def test_atualizar_email_invalido():
    u = Usuario("Teste", "teste@email.com", "Senha123")
    assert not u.atualizar_email("sem-arroba")

def test_atualizar_senha_invalida():
    u = Usuario("Teste", "teste@email.com", "Senha123")
    assert not u.atualizar_senha("")
def test_atualizar_senha_vazia():
    u = Usuario("Lucia", "lucia@email.com", "Senha123")
    assert u.atualizar_senha("") is False

def test_usuario_func_0():
    from usuario import usuario_func_0
    assert usuario_func_0() == "USUARIO_0"


def test_usuario_func_1():
    from usuario import usuario_func_1
    assert usuario_func_1() == "USUARIO_1"


def test_usuario_func_2():
    from usuario import usuario_func_2
    assert usuario_func_2() == "USUARIO_2"


def test_usuario_func_3():
    from usuario import usuario_func_3
    assert usuario_func_3() == "USUARIO_3"


def test_usuario_func_4():
    from usuario import usuario_func_4
    assert usuario_func_4() == "USUARIO_4"


def test_usuario_func_5():
    from usuario import usuario_func_5
    assert usuario_func_5() == "USUARIO_5"


def test_usuario_func_6():
    from usuario import usuario_func_6
    assert usuario_func_6() == "USUARIO_6"


def test_usuario_func_7():
    from usuario import usuario_func_7
    assert usuario_func_7() == "USUARIO_7"


def test_usuario_func_8():
    from usuario import usuario_func_8
    assert usuario_func_8() == "USUARIO_8"


def test_usuario_func_9():
    from usuario import usuario_func_9
    assert usuario_func_9() == "USUARIO_9"


def test_usuario_func_10():
    from usuario import usuario_func_10
    assert usuario_func_10() == "USUARIO_10"


def test_usuario_func_11():
    from usuario import usuario_func_11
    assert usuario_func_11() == "USUARIO_11"


def test_usuario_func_12():
    from usuario import usuario_func_12
    assert usuario_func_12() == "USUARIO_12"


def test_usuario_func_13():
    from usuario import usuario_func_13
    assert usuario_func_13() == "USUARIO_13"


def test_usuario_func_14():
    from usuario import usuario_func_14
    assert usuario_func_14() == "USUARIO_14"


def test_usuario_func_15():
    from usuario import usuario_func_15
    assert usuario_func_15() == "USUARIO_15"


def test_usuario_func_16():
    from usuario import usuario_func_16
    assert usuario_func_16() == "USUARIO_16"


def test_usuario_func_17():
    from usuario import usuario_func_17
    assert usuario_func_17() == "USUARIO_17"


def test_usuario_func_18():
    from usuario import usuario_func_18
    assert usuario_func_18() == "USUARIO_18"


def test_usuario_func_19():
    from usuario import usuario_func_19
    assert usuario_func_19() == "USUARIO_19"


def test_usuario_func_20():
    from usuario import usuario_func_20
    assert usuario_func_20() == "USUARIO_20"


def test_usuario_func_21():
    from usuario import usuario_func_21
    assert usuario_func_21() == "USUARIO_21"


def test_usuario_func_22():
    from usuario import usuario_func_22
    assert usuario_func_22() == "USUARIO_22"


def test_usuario_func_23():
    from usuario import usuario_func_23
    assert usuario_func_23() == "USUARIO_23"


def test_usuario_func_24():
    from usuario import usuario_func_24
    assert usuario_func_24() == "USUARIO_24"