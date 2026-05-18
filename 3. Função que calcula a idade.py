def calcular_idade(ano_nascimento):
    ano_atual = 2026  # você pode trocar por um valor dinâmico se quiser
    return ano_atual - ano_nascimento


def main():
    ano = int(input("Digite o ano de nascimento: "))

    idade = calcular_idade(ano)
    print("Idade:", idade)


if __name__ == "__main__":
    main()