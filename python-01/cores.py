cor1 = int(input("digite o numero da primeira cor da sua escolha: (1)vermelho, (2) amarelo ou (3) azul: "))
cor2 = int(input("digite o numero da segunda cor da sua escolha: (1)vermelho, (2) amarelo ou (3) azul: "))

print("suas cores escolhidas foram: ", cor1," e ", cor2)

if cor1 == 1 and cor2 == 1:
    print("a mistura é: vermelho")

elif cor1 == 1 and cor2 == 2:
    print("a mistura é: laranja")

elif cor1 == 1 and cor2 == 3:
    print("a mistura é: roxo")

elif cor1 == 2 and cor2 == 1:
    print("a mistura é: laranja")

elif cor1 == 2 and cor2 == 2:
    print("a mistura é: amarelo")

elif cor1 == 2 and cor2 == 3:
    print("a mistura é: verde")

elif cor1 == 3 and cor2 == 3:
    print("a mistura é: azul")

elif cor1 == 3 and cor2 == 1:
    print("a mistura é: roxo")

elif cor1 == 3 and cor2 == 2:
    print("a mistura é: verde")

else:
    print("por favor digite 1, 2 ou 3")