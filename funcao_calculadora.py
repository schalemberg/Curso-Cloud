def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0


operacao = int(input(
    "Escolha a operação: 1. Soma, 2. Subtração, 3. Multiplicação, 4. Divisão: "))

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

resultado = calculadora(num1, num2, operacao)
print("O resultado é: ", resultado)
