from random import randint
print("Olá,\nSeja bem vindo ao jogo de adivinhação, como funciona: \nVocê escolhe qual adivinhação você quer tentar\nEm seguida dira qual numero aleatório que ira sair")
x = int(input("digite o numero inicial da sua adivinhação: "))
y = int(input("digite o numero final da sua adivinhação: "))
print("você escolheu um numero aleatório de: ", x, "a", y)
if x >= 0 and y >= 0:
    numero = int(input("digite um numero inteiro que deseja e tente a sorte:\n"))
    aleatorio = (randint(x, y))
    if numero <0 :
        print("escolha uma numero maior que zero")
    elif numero > aleatorio:
        print("seu numero é maior que o numero sortiado")
        print("o numero que voce escolheu foi: ", numero, "o numero aleatorio é: ", aleatorio)
    elif numero < aleatorio:
        print("o seu numero é menor do que o numero sortiado")
        print("o numero que voce escolheu foi: ", numero, "o numero aleatorio é: ", aleatorio)
    else:
        print("Parabéns!!! Você acertou")
        print("o numero que voce escolheu foi: ", numero, "o numero aleatorio é: ", aleatorio)
else:
    print("digite numeros positivos maiores ou iguais a zero")