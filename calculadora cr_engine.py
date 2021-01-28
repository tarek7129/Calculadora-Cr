import materias
ra = []
busca = 0

def MenuPrincipal(materia):
    print("[1]: Adicionar RA | [2]: Consultar RA | [3]: Relatório das matérias | [0]: Sair")

    menu = int(input())
    while menu != 0:
        if menu >= 4 or menu < 0:
            print("vai toma no seu cu filha da putinha")
            for x in range(1000):
                print("te conheço nessa porra?")
            break
        if menu == 1:
            print("Digite seu RA:")
            ra.append(int(input()))


        elif menu == 2:
            print("Digite seu RA:")
            busca = int(input())
            for i in range(0,len(ra),1):
                if busca == ra[i]:
                    print ("carai junin ta aki")
                    break
                elif i == len(ra)-1 :
                    print ("nao achamo")

        elif menu == 3:
            for i in range(len(materias.materia)):
                print(f"materia: {materias.materia[i]} /// num de creditos: {materias.creditos[i]}")


        print("[1]: Adicionar RA | [2]: Consultar RA | [3]: Relatório das matérias | [0]: Sair")
        menu = int(input())


def SegundoMenu(materia):
    print("[1]: Adicionar Matéria | [2]: Relatório das matérias | [0]: Sair")

def SegundoMenuCompleto(materia):
    print(" [1]: Adicionar Matéria | [2]: Deletar Matéria | [3]: Listar matérias cursadas"
                 "\n[4]: Listar matérias restantes | [5]: Calcular CR | [6]: Relatório das matérias | [0]: Sair")





