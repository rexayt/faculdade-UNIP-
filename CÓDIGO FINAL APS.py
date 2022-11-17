resultado_tonelada = []
def carus():
    g=d=a=0
    impacto_gasolina = 0.16666666666666666666666666666667
    impacto_gasolina1 = impacto_diesel = 0.25
    impacto_gasolina2 = 0.33333333333333333333333333333333
    impacto_alcool = 0.08333333333333333333333333333333
    emissão=0
    escolha = str(input("Seu carro é movido a:\n Gasolina [1] \n Diesel [2] \n Álcool [3] \n Sua escolha: "))
    while escolha not in "123":
        escolha = str(input("Comando inválido digite: \n Gasolina [1] \n Diesel[2] \n Álcool [3] \n Sua escolha: "))
    if escolha == "1":
        carrog = str(input("Seu carro é de: \n 1,4L[1] \n 1,5 - 2,0 [2] \n Maior que 2,0 [3]\n Sua escolha: "))
        while carrog not in "123":
            carrog = str(input("Comando inválido digite: \n 1,4L [1] \n 1,5 - 2,0 [2] \n Maior que 2,0 [3]\n Sua escolha: "))
        if carrog == "1":
            comb = int(input("Digite quantos L você usa por mês: "))
            consumo = comb*12
            emissão = (comb*12)*impacto_gasolina
            print(f"Seu carro gasta {consumo}L de gasolina por ano")
            print('')
            resultado_tonelada.append(emissão)
        elif carrog == "2":
            comb = int(input("Digite quantos L você usa por mês: "))
            consumo = comb*12
            emissão = (comb*12)*impacto_gasolina1
            print(f"Seu carro gasta {consumo}L de gasolina por ano")
            print('')
            resultado_tonelada.append(emissão)
        else:
            comb = int(input("Digite quantos L você usa por mês: "))
            consumo = comb*12
            emissão = (comb*12)*impacto_gasolina2
            print(f"Seu carro gasta {consumo}L de gasolina por ano")
            print('')
            resultado_tonelada.append(emissão)
    elif escolha == "2":
        comb = int(input("digite quantos L você usa por mês: "))
        consumo = comb*12
        emissão = (comb*12)*impacto_diesel
        print(f"Seu carro gasta {consumo} L de diesel por ano")
        print('')
        resultado_tonelada.append(emissão)
    elif escolha == "3":
        comb = int(input("digite quantos L você usa por mês: "))
        consumo = comb*12
        emissão = (comb*12)*impacto_alcool
        print(f"Seu carro gasta {consumo} L de álcool por ano")
        print('')
        resultado_tonelada.append(emissão)
def sim_não(variável):
    while variável not in "SN":
        variável = str(input("Comando inválido, digite 'S' ou 'N': ")).strip().upper()
        print('')
def energia():
    impacto_kwh = 0.0125
    #Impacto em Co2 1 Kwh = 0,0125
    consumo_kwh = int(input("Digite o seu consumo de energia mensal: "))
    #Consumo do usuário em KHW
    consumo_anual_energia = consumo_kwh*12
    #Consumo de energia que o usuário teria no ano inteiro
    emissão = (consumo_kwh*impacto_kwh)*12
    #O cálculo de quanto o usuário emite em um ano
    print(f"você usa {consumo_anual_energia} Kwh de energia por ano")
    resultado_tonelada.append(emissão)
    print('')
print("Bem vindo à calculadora de Crédito de Carbono")
print("Vamos calcular o seu consumo de energia por ano, se você tiver carro, e moto, vamos calcular quantos litros você usa por ano")
print("E transformaremos em Toneladas de Co²")
print('')
carro = str(input("Você possui carro digite 'S' ou 'N': ")).strip().upper()
sim_não(carro)
if carro in "S":
    carros = int(input("Possui quantos? "))
    print('')
    if carros == 1:
        carus()
    else:
        for c in range(0, carros+1):
            carus()
moto = str(input("Você possui moto? digite 'S' ou 'N': ")).strip().upper()
sim_não(moto)
if moto in "S":
    impacto_alcool = 0.08333333333333333333333333333333
    comb = int(input("digite quantos L você usa por mês: "))
    consumo = comb*12
    emissão_moto = (comb*12)*impacto_alcool
    resultado_tonelada.append(emissão_moto)
    print(f"Sua moto consome {consumo}L de álcool por ano")
    print('')
print(' ')
energia()
Toneladas = sum(resultado_tonelada)/1000
print(Toneladas)
compensação = Toneladas/0.095
arveres = compensação*28.5
linha = "="*10
resultado = linha+"RESULTADO"+linha
print(' ')
print(resultado.center(50))
print('')
print(f"Você produz {Toneladas:.2f} Ton CO²(Toneladas de CO²) por ano\nVocê precisaria plantar {round(compensação)} árvores para compensar o que você produz\n'Todas as mudas das árvores custariam {arveres:.2f}")

