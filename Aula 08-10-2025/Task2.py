import math
def circu():
    while True:
        try:
            raio = float(input('Digite o raio: '))
        except ValueError:
            print('Só é aceito Numeros')
            continue
        circunferencia = raio * 2 * math.pi
        print(f'A cincunfência de Raio {raio}cm é {circunferencia:.2f}cm.')
        break

circu()
