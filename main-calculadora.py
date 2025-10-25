import math  

def menu():
    print("\n=== CALCULADORA DE MATEMÁTICA BÁSICA E ESTATÍSTICA ===")
    print("1 - Média Aritmética")
    print("2 - Porcentagem")
    print("3 - Teorema de Pitágoras")
    print("4 - Sair")

def calcular_media():
    print("\n--- MÉDIA ARITMÉTICA ---")
    numeros = input("Digite os números separados por espaço: ").split()
    numeros = [float(n) for n in numeros]
    media = sum(numeros) / len(numeros)
    print(f"A média é: {media:.2f}")

def calcular_porcentagem():
    print("\n--- PORCENTAGEM ---")
    total = float(input("Digite o valor total: "))
    porcentagem = float(input("Digite a porcentagem (%): "))
    resultado = total * (porcentagem / 100)
    print(f"{porcentagem}% de {total} é {resultado:.2f}")

def teorema_pitagoras():
    print("\n--- TEOREMA DE PITÁGORAS ---")
    print("Escolha o que deseja calcular:")
    print("1 - Calcular a hipotenusa (c)")
    print("2 - Calcular um dos catetos (a ou b)")
    opcao = input("Opção: ")

    if opcao == "1":
        a = float(input("Digite o valor do cateto a: "))
        b = float(input("Digite o valor do cateto b: "))
        c = math.sqrt(a**2 + b**2)
        print(f"A hipotenusa (c) é: {c:.2f}")
    elif opcao == "2":
        c = float(input("Digite o valor da hipotenusa: "))
        cateto = float(input("Digite o valor do outro cateto: "))
        resultado = math.sqrt(c**2 - cateto**2)
        print(f"O valor do cateto faltante é: {resultado:.2f}")
    else:
        print("Opção inválida!")

# Programa principal
while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        calcular_media()
    elif escolha == "2":
        calcular_porcentagem()
    elif escolha == "3":
        teorema_pitagoras()
    elif escolha == "4":
        print("Encerrando a calculadora... Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")
