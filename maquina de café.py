print("Olá, escolha o tipo do café, as opções são:\n 1- café normal (R$:2,50) \n 2- café expresso (R$:2,75) \n 3- Capuccino (R$:3,50) \n 4- Mocaccino (R$:3,25) ")
y = int(input("digite sua escolha: "))
if y == 1:
    print("você escolheu café normal")
elif y == 2:
    print("você escolheu café expresso")
elif y == 3:
    print("você escolheu Capuccino")
elif y == 4:
    print ("você escolheu moccacino")
else: 
    print ("escolha uma opção válida")

if y < 0 or y > 4:
    print("compra cancelada")
else: 
    quantidade = int(input("digite quantos cafés você quer: "))
    if quantidade >= 1:
        if y >= 1 and y <= 4:
            valor = 2.50 * quantidade
        elif y == 2: 
            valor =  2.75 * quantidade
        elif y == 3:
            valor = 3.50 * quantidade
        elif y == 4: 
            valor = 3.75 * quantidade
        else: 
            valor = 0
    else: 
        print("quantidade inválida")

    print("a quantidade de café que você quer é: ", quantidade, "o valor da sua compra é: ", valor, " reais")
    print("formas de pagamento: \n 1- dinheiro \n 2- cartão \n 3- pix")
    forma = int(input("digite a forma de pagamento: "))
    pagamento = float(input("digite o valor do pagamento: "))
    total = pagamento - valor
    if forma == 1:
        if total == 0:
            print("não necessita de troco, obrigada pela compra")
        elif total < 0:
            print("valor insufificente para finalizar a compra")
        else:
            print("o troco é: ", total)
            moeda1 = total % 1 
            if moeda1 == 0:
                troco = total
                print("a quantidade de moedas de 1 real vai ser: ", total)
                print("obrigada pela compra")
            else: 
                moeda2 = moeda1 % 0.5
                if moeda2 == 0:
                    troco = total % 1 / 5
                    print(" a quantidade de moedas de 1 é: ", int(total),"\n e a quantidade de moedas de 50 centavos vai ser: ", troco)
                    print("obrigada pela compra")
                else: 
                    moeda3 = moeda2 % 0.25
                    if moeda3 == 0:
                        cinquenta = total % 1 / 5
                        troco = cinquenta / 0.25
                        print("a quantidade de moedas de 1 real é: ", int(total), "\n a quantidade de moedas de 50 centavos vai ser: ", int(cinquenta), "\n e a quantidade de moedas de 25 centavos é: ", troco)
                        print("obrigada pela compra")
                    else:
                        moeda4 = moeda3 % 0.10
                        if moeda4 == 0:
                            cinquenta = total % 1 / 5 
                            vinte = cinquenta / 0.25
                            troco = vinte / 0.10
                            print("a quantida de moedas de 1 real é: ", int(total), "\n a quantida de moedas de 50 centavos vai ser: ", int(cinquenta), "\n a quantidade de moedas de 25 centavos é: ", int(vinte), "\n e a quantidade de moedas de 10 centavos é: ", troco)
                            print("obrigada pela compra")
                        else:
                            moeda5 = moeda4 % 0.05
                            if moeda5 == 0:
                                cinquenta = total % 1 / 5
                                vinte = cinquenta / 0.25
                                dez = vinte / 0.10
                                troco = dez / 0.05
                                print("a quantida de moedas de 1 real é: ", int(total), "\n a quantida de moedas de 50 centavos vai ser: ", int(cinquenta), "\n a quantidade de moedas de 25 centavos é: ", int(vinte), "\n a quantidade de moedas de 10 centavos é: ", int(dez),"\n a quantidade de moedas de 5 centavos é: ", troco)
                                print("obrigada pela compra")
                            else:
                                moeda6 = moeda5 / 0.01
                                cinquenta = total % 1 / 5
                                vinte = cinquenta / 0.25
                                dez = vinte / 0.10
                                cinco = dez / 0.05
                                troco = moeda6
                                print("a quantida de moedas de 1 real é: ", int(total), "\n a quantida de moedas de 50 centavos vai ser: ", int(cinquenta), "\n a quantidade de moedas de 25 centavos é: ", int(vinte), "\n a quantidade de moedas de 10 centavos é: ", int(dez),"\n a quantidade de moedas de 5 centavos é: ",int(cinco), "\n a quantidade de moedas de 1 centavo é: ", round(troco))
                                print("obrigada pela compra")
    elif forma == 2:
        print("passe o cartão na maquina abaixo, com o valor de: ",total)
        print("obrigada pela compra")
    elif forma == 3:
        print("mande o pagamento de: ", total, "\n para o pix 123.456.789-10 \n em nome da loja: cafeteria pucpr ")
        print("obrigada pela compra")
    else:
        print("selecione uma opção valida")

