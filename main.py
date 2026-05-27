filmes = []

def cadastrar_filme():
    nome = input("Digite o nome do filme: ")
    genero = input("Digite o gênero do filme: ")
    nota = float(input("Digite a nota do filme (0 a 10): "))

    filme = {
        "nome": nome,
        "genero": genero,
        "nota": nota
    }

    filmes.append(filme)

    print(f"\nFilme '{nome}' cadastrado com sucesso!")
    print(f"Nota registrada: {nota:.1f}\n")

def listar_filmes():
    if len(filmes) == 0:
        print("\nNenhum filme cadastrado.\n")
    else:
        print("\n===== LISTA DE FILMES =====")

        for i, filme in enumerate(filmes):
            print(f"{i+1} - {filme['nome']} | Gênero: {filme['genero']} | Nota: {filme['nota']}")

        print()

def classificar_filme():
    nome = input("Digite o nome do filme: ")

    encontrado = False

    for filme in filmes:
        if filme["nome"].lower() == nome.lower():

            if filme["nota"] >= 8:
                print(f"\n{filme['nome']} é um FILMAÇO!\n")

            elif filme["nota"] >= 6:
                print(f"\n{filme['nome']} é um filme BOM\n")

            elif filme["nota"] >= 4:
                print(f"\n{filme['nome']} é um filme MEDIANO\n")

            else:
                print(f"\n{filme['nome']} é um filme RUIM\n")

            encontrado = True

    if not encontrado:
        print("\nFilme não encontrado.\n")


def media_notas():
    if len(filmes) == 0:
        print("\nNenhum filme cadastrado.\n")

    else:
        soma = 0

        for filme in filmes:
            soma += filme["nota"]

        media = soma / len(filmes)

        print(f"\nA média das notas dos filmes é: {media:.2f}\n")

opcao = 0

while opcao != 5:

    print("===== SISTEMA DE FILMES =====")
    print("1 - Cadastrar filme")
    print("2 - Listar filmes")
    print("3 - Classificar filme")
    print("4 - Média das notas")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_filme()

    elif opcao == 2:
        listar_filmes()

    elif opcao == 3:
        classificar_filme()

    elif opcao == 4:
        media_notas()

    elif opcao == 5:
        print("\nEncerrando o sistema...")

    else:
        print("\nOpção inválida!\n")