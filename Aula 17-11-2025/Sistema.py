from cursos import Curso
from campus import Campus


class SistemaUFC:
    def __init__(self):
        # Transformei os campus iniciais em OBJETOS Campus
        self.campus_list = [
            Campus("Campus do Benfica"),
            Campus("Campus do Pici"),
            Campus("Campus de Porangabuçu"),
            Campus("Campus de Sobral"),
            Campus("Campus de Quixadá"),
            Campus("Campus de Crateús"),
            Campus("Campus de Russas"),
            Campus("Campus do Itapajé")
        ]

    # CAMPUS CRUD
    def criar_campus(self, nome):
        self.campus_list.append(Campus(nome))

    def listar_campus(self):
        if not self.campus_list:
            print("Nenhum campus cadastrado.")
            return
        for i, campus in enumerate(self.campus_list):
            print(f"{i+1}. {campus.nome}")

    def buscar_campus(self, nome):
        for campus in self.campus_list:
            if campus.nome.lower() == nome.lower():
                return campus
        return None

    def buscar_campus_por_indice(self, indice):
        if indice.isdigit():
            indice = int(indice)
            if 1 <= indice <= len(self.campus_list):
                return self.campus_list[indice - 1]
        return None

    def remover_campus_por_indice(self, indice):
        campus = self.buscar_campus_por_indice(indice)
        if campus:
            self.campus_list.remove(campus)
            return True
        return False

    # CURSOS CRUD
    def adicionar_curso_no_campus(self, indice_campus, nome_curso):
        campus = self.buscar_campus_por_indice(indice_campus)
        if campus:
            campus.adicionar_curso(Curso(nome_curso))
            return True
        return False

    def listar_cursos_do_campus(self, indice_campus):
        campus = self.buscar_campus_por_indice(indice_campus)
        if campus:
            print(f"Cursos do {campus.nome}:")
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
                return
            for curso in campus.cursos:
                print(f"- {curso}")
        else:
            print("Campus inválido.")

    def remover_curso_do_campus(self, indice_campus, codigo):
        campus = self.buscar_campus_por_indice(indice_campus)
        if campus:
            return campus.remover_curso(codigo)
        return False


# ----------- MENU INTERATIVO ------------
def menu():
    sistema = SistemaUFC()

    while True:
        print("\n===== SISTEMA UFC =====")
        print("1. Criar Campus")
        print("2. Listar Campus")
        print("3. Remover Campus (por número)")
        print("4. Adicionar Curso a Campus (por número)")
        print("5. Listar Cursos de um Campus (por número)")
        print("6. Remover Curso de um Campus (por número)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if not opcao.isdigit():
            print("Entrada inválida. Digite um número.")
            continue

        # CAMPUS
        if opcao == "1":
            nome = input("Nome do novo Campus: ").strip()
            if nome == "":
                print("Nome inválido.")
            else:
                sistema.criar_campus(nome)
                print("Campus criado!")

        elif opcao == "2":
            sistema.listar_campus()

        elif opcao == "3":
            sistema.listar_campus()
            indice = input("Digite o número do campus para remover: ")
            if sistema.remover_campus_por_indice(indice):
                print("Campus removido.")
            else:
                print("Número inválido.")

        # CURSOS
        elif opcao == "4":
            sistema.listar_campus()
            indice = input("Escolha o número do campus: ")
            nome_curso = input("Nome do Curso: ").strip()

            if sistema.adicionar_curso_no_campus(indice, nome_curso):
                print("Curso adicionado!")
            else:
                print("Número inválido.")

        elif opcao == "5":
            sistema.listar_campus()
            indice = input("Número do campus: ")
            sistema.listar_cursos_do_campus(indice)

        elif opcao == "6":
            sistema.listar_campus()
            indice = input("Número do campus: ")
            codigo = input("Código do curso: ").strip().upper()

            if sistema.remover_curso_do_campus(indice, codigo):
                print("Curso removido.")
            else:
                print("Campus ou código inválido.")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
