class Ponto():
    def __init__(self):
        self.x = float(input('Digite a coordenada x: '))
        self.y = float(input('Digite a coordenada y: '))
    def texto(self):
        return f'({self.x}, {self.y})'

def calcular_distancia(ponto_a, ponto_b):
    return ((ponto_a.x - ponto_b.x)**2 + (ponto_a.y - ponto_b.y)**2)**0.5

ponto_a = Ponto()
ponto_b = Ponto()

print('Distancia',calcular_distancia(ponto_a, ponto_b))