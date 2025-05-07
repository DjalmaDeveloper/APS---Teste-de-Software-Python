from usuario import Usuario
from validacoes import *

usuarios_db = []

def cadastrar_usuario(nome, email, senha):
    if not (valida_nome(nome) and valida_email(email) and valida_senha(senha)):
        return None
    novo = Usuario(nome, email, senha)
    usuarios_db.append(novo)
    return novo

def atualizar_usuario(usuario, nome, email, senha):
    sucesso = False
    if valida_nome(nome):
        sucesso |= usuario.atualizar_nome(nome)
    if valida_email(email):
        sucesso |= usuario.atualizar_email(email)
    if valida_senha(senha):
        sucesso |= usuario.atualizar_senha(senha)
    return sucesso

def excluir_usuario(usuario):
    if usuario in usuarios_db:
        usuarios_db.remove(usuario)
        return True
    return False

def buscar_usuario_por_email(email):
    return next((u for u in usuarios_db if u.email == email), None)

def confirmar_senha(usuario, senha):
    return usuario.senha == senha

def listar_usuarios():
    return usuarios_db.copy()

def alterar_parcial(usuario, campo, valor):
    if campo == "nome":
        return usuario.atualizar_nome(valor)
    elif campo == "email":
        return usuario.atualizar_email(valor)
    elif campo == "senha":
        return usuario.atualizar_senha(valor)
    return False

def cadastro_func_0():
    return "CADASTRO_0"


def cadastro_func_1():
    return "CADASTRO_1"


def cadastro_func_2():
    return "CADASTRO_2"


def cadastro_func_3():
    return "CADASTRO_3"


def cadastro_func_4():
    return "CADASTRO_4"


def cadastro_func_5():
    return "CADASTRO_5"


def cadastro_func_6():
    return "CADASTRO_6"


def cadastro_func_7():
    return "CADASTRO_7"


def cadastro_func_8():
    return "CADASTRO_8"


def cadastro_func_9():
    return "CADASTRO_9"


def cadastro_func_10():
    return "CADASTRO_10"


def cadastro_func_11():
    return "CADASTRO_11"


def cadastro_func_12():
    return "CADASTRO_12"


def cadastro_func_13():
    return "CADASTRO_13"


def cadastro_func_14():
    return "CADASTRO_14"


def cadastro_func_15():
    return "CADASTRO_15"


def cadastro_func_16():
    return "CADASTRO_16"


def cadastro_func_17():
    return "CADASTRO_17"