def info_nome():
    while True:  # loop
        nome_completo = input("Digite seu nome completo: ")
        try:  # tratamento de erro
            ano_nascimento = int(
                input("Digite seu ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:  # condição
                break  # interrompe o loop
            else:  # condição
                print("Erro: o ano de nascimento deve estar entre 1922 e 2021.")
        except ValueError:
            print("Erro: você deve digitar um número para o ano de nascimento.")
    return nome_completo, ano_nascimento  # retorna os valores


def calcula(ano_nascimento):  # definição da função
    ano_atual = 2023
    idade = ano_atual - ano_nascimento  # calculo
    return idade


nome_completo, ano_nascimento = info_nome()
idade = calcula(ano_nascimento)
print(f"Seu nome é: ",
      nome_completo,   " e você completou, ou completará, no ano atual (2023): ",  idade, " anos.")  # saída de dados
