from math import cos
from math import sin
from math import tan
from math import radians
from math import degrees

print("Olá\nSeja bem vindo ao programa que calcula angulo, escolha uma das opções abaixo: ")
print("1- sen (x), 2 - cos(x), 3 - tg(x), 4 - cossec(x), 5 - sec(x), 6 - cotg(x), 0 - Sair do programa ")
escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    print("Sua escolha foi sen (x)")
    numero = float(input("digite o angulo desejado em graus: "))
    trans1 = radians(numero)
    resultado = sin(trans1)
    print("o resultado da conta é:", round(resultado, 2))

elif escolha == 2:
    print("Sua escolha foi cos (x)")
    numero = int(input("digite o angulo desejado em graus: "))
    trans1 = radians(numero)
    resultado = cos(trans1)
    print("o resultado da conta é:", round(resultado, 2))

elif escolha == 3:
    print("Sua escolha foi tg (x)")
    numero = int(input("digite o angulo desejado em graus: "))
    trans1 = radians(numero)
    resultado = tan(trans1)
    print("o resultado da conta é:", round(resultado, 2))

elif escolha == 4:
    print("Sua escolha foi cossec (x)")
    numero = int(input("digite o angulo desejado em graus: "))
    trans1 = radians(numero)
    resultado = (1/sin(trans1))
    print("o resultado da conta é:", round(resultado, 2))

elif escolha == 5:
    print("Sua escolha foi sec (x)")
    numero = int(input("digite o angulo desejado em graus: "))
    trans1 = radians(numero)
    resultado = (1/cos(trans1))
    print("o resultado da conta é:", round(resultado, 2))

elif escolha == 6:
    print("Sua escolha foi costg (x)")
    numero = int(input("digite o angulo desejado em graus: "))
    trans1 = radians(numero)
    resultado = (1/tan(trans1))
    print("o resultado da conta é:", round(resultado, 2))
elif escolha == 0:
    ("saindo do programa")

else:
    ("por favor digite uma escolha valida")

