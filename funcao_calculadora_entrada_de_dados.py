"""Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. """


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


while True:
    operacao = int(input(
        "Escolha a operação: 1. Soma, 2. Subtração, 3. Multiplicação, 4. Divisão, ou aperte qualquer 0 para sair: "))
    if operacao == 0:
        break
    elif operacao in [1, 2, 3, 4]:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        resultado = calculadora(num1, num2, operacao)
        print("O resultado é: ", resultado)
    else:
        print("Essa opção não existe")
