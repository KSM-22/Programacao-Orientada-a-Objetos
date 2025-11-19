class Campus:
    def __init__(self, nome, cursos):
        self.nome = nome
        self.cursos = cursos  # <-- AQUI ESTÁ A CORREÇÃO

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def remover_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                self.cursos.remove(curso)
                return True
        return False

    def buscar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def __str__(self):
        return f"Campus: {self.nome} ({len(self.cursos)} cursos)"