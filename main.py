alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    aluno = {
        "nome": nome,
        "media": media
    }

    alunos.append(aluno)

    print(f"\nAluno {nome} cadastrado com sucesso!")
    print(f"Média final: {media:.2f}\n")

def listar_alunos():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.\n")
    else:
        print("\n===== LISTA DE ALUNOS =====")
        for i, aluno in enumerate(alunos):
            print(f"{i+1} - {aluno['nome']} | Média: {aluno['media']:.2f}")
        print()


def verificar_aprovacao():
    nome = input("Digite o nome do aluno: ")

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():

            if aluno["media"] >= 6:
                print(f"\n{aluno['nome']} foi APROVADO!\n")
            elif aluno["media"] >= 4:
                print(f"\n{aluno['nome']} está de RECUPERAÇÃO.\n")
            else:
                print(f"\n{aluno['nome']} foi REPROVADO.\n")

            encontrado = True

    if not encontrado:
        print("\nAluno não encontrado.\n")


def media_geral():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.\n")
    else:
        soma = 0

        for aluno in alunos:
            soma += aluno["media"]

        media = soma / len(alunos)

        print(f"\nA média geral da turma é: {media:.2f}\n")


opcao = 0

while opcao != 5:

    print("===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Verificar aprovação")
    print("4 - Média geral da turma")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        listar_alunos()

    elif opcao == 3:
        verificar_aprovacao()

    elif opcao == 4:
        media_geral()

    elif opcao == 5:
        print("\nEncerrando o sistema...")

    else:
        print("\nOpção inválida!\n")