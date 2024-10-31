import random as rd
import string

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres=""
    if maiusculas:
        caracteres+=string.ascii_uppercase
    if minusculas:
        caracteres+=string.ascii_lowercase
    if numeros:
        caracteres+=string.digits
    if especiais:
        caracteres+=string.punctuation
    senha = "".join(rd.choices(caracteres, k=tamanho))
    return senha
while True:
    print(gerar_senha(int(input("Digite o tamanho da senha: "))))
    if input("Deseja gerar outra senha? (s/n): ").lower() == "n":
        break