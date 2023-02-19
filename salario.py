def salario():
    n = float(input("Digite o salário: "))
    #Hora extra
    return n


def resultado(n1,n2):
    inss = (n1+n2)*0.1
    vt = (n1+n2)*0.06
    s = (n1+n2)-(inss+vt)
    d = input("Nome do funcionário: ")
    print("Nome: ", d)
    print("Descontos: %.2f "% inss)
    print("Vale Transporte: %.2f "% vt)
    print("Salário total: %.2f "% s)

    if s <= 1500.00:
        print("Necessita de aumento")
    else:
        print("Não necessita de aumento")


a = salario()
b = salario()
resultado(a,b)
