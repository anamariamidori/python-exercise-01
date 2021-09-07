print("Olá, seja bem vindo ao hotel dog pucpr.")
print("vamos começar o orçamento: ")
dono = input("digite seu nome: ") 
sobre = input("digite seu sobrenome: ")
rg = input("digite seu rg: ")
pet = input("digite o nome do seu cachorro: ")
raça = input("digite a raça do seu pet: ")
idade = input("digite a idade do seu pet: ")
peso = int(input("digite o peso do seu pet: "))

if peso > 0 and peso < 8:
    valor = 50
    print("O dono é: ", dono, sobre, "\n Do rg", rg, "\n Cachorro: ", pet, "\n Da raça: ", raça, "\n De idade: ", idade, "anos", "\n De peso: ",peso ,"kg", "\n O orçamento fica: R$ ", valor," reias")
elif peso >= 8 and peso < 15:
    valor = 70
    print("O dono é: ", dono, sobre, "\n Do rg", rg, "\n Cachorro: ", pet, "\n Da raça: ", raça, "\n De idade: ", idade,"anos", "\n De peso: ",peso ,"kg", "\n O orçamento fica: R$ ", valor," reias")
elif peso >= 15 and peso < 70:
    valor = 100
    print("O dono é: ", dono, sobre, "\n Do rg", rg, "\n Cachorro: ", pet, "\n Da raça: ", raça, "\n De idade: ", idade,"anos", "\n De peso: ",peso ,"kg", "\n O orçamento fica: R$ ", valor,"reias")
elif peso > 70:
    valor = 125
    print("O dono é: ", dono, sobre, "\n Do rg", rg, "\n Cachorro: ", pet, "\n Da raça: ", raça, "\n De idade: ", idade,"anos", "\n De peso: ",peso ,"kg", "\n O orçamento fica: R$ ", valor, " reias")
else: 
    print("digite um peso maior que 0")