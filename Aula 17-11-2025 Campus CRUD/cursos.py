class Curso:
    # Dicionário global: nome_do_curso -> código
    codigos_gerados = {}
    proximo_codigo = 1

    def __init__(self, nome):
        self.nome = nome
        self.codigo = self.obter_codigo(nome)
        self.alunos = []  # Lista de alunos do curso

    @classmethod
    def obter_codigo(cls, nome):
        # Se o curso já tiver código, apenas retorna.
        if nome in cls.codigos_gerados:
            return cls.codigos_gerados[nome]

        # Se for um curso novo, gerar código no formato CXXX
        codigo = f"C{cls.proximo_codigo:03d}"
        cls.codigos_gerados[nome] = codigo
        cls.proximo_codigo += 1

        return codigo

    # Métodos de gerenciamento de alunos
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                return True
        return False

    def listar_alunos(self):
        if not self.alunos:
            print(f"Nenhum aluno cadastrado em {self.nome}.")
            return
        print(f"Alunos do curso {self.nome}:")
        for aluno in self.alunos:
            print(f"- {aluno}")

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.matricula} - {self.nome}"
