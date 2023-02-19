d = input("Digite o nome do Aluno: ")


def lernotas():
    n = float(input("Digite a nota aluno: "))
    return n


def lerresultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nome: ", d)
    print("Nota 1: %.2f " % n1)
    print("Nota 2: %.2f " % n2)
    print("Média final: %.2f " % media , "Resultado: ", end="")


    if media <= 7:
        print("Reprovado")
    else:
        print("Aprovado")

a = lernotas()
b = lernotas()
lerresultado(a,b)
