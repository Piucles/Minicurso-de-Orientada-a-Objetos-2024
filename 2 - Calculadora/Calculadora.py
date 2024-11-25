def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    if b == 0:
        return "Divisão por zero"
    return a / b

def divisaoInteira (a,b):
    return a // b

def resto (a,b):
    return a % b

def exppo (a,b):
    return a ** b

while True:
    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Divisão Inteira")
    print("6 - Resto")
    print("7 - Exponenciação")
    print("'Sair' - para encerrar")

    op = input("Digite a opção de 1 a 7 ou 'sair' para encerrar: ")

    if op == 'sair':
        print("Encerrando")
        exit()

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if op == '1':
        print(soma(n1,n2))
    elif op == '2':
        print(subtracao(n1,n2))
    elif op == '3':
        print(multiplicacao(n1,n2))
    elif op == '4':
        print(divisao(n1,n2))
    elif op == '5':
        print(divisaoInteira(n1,n2))
    elif op == '6':
        print(resto(n1,n2))
    elif op == '7':
        print(exppo(n1,n2))
    elif op == 'sair':
        print("Encerrando a calculadora")
        exit()
    else:
        print("Opção inválida")
