class Curso:
    contador_codigos = 1  # contador global para gerar códigos automaticamente

    def __init__(self, nome):
        self.nome = nome
        self.codigo = f"C{Curso.contador_codigos:03d}"  # Ex: C001, C002, C003...
        Curso.contador_codigos += 1

    def __str__(self):
        return f"{self.codigo} - {self.nome}"