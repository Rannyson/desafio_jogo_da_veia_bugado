import math
import random

class Jogador:
    def __init__(self, letra):
        self.letra = letra

    def Mover(self,jogo):
        pass

class ComputadorPlayer(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
    
    def Mover(self, jogo):
        quadrado = random.choice(jogo.movimentos_disponiveis())
        return quadrado

class Jogador2(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
    
    def Mover(self, jogo):
        quadrados_validos = False
        valor = None
        while not quadrados_validos:
            valor = input(self.letra + '\'s Movimentos de entrada(0-9):')

            try:
                valor = int(quadrado)
                if valor not in jogo.movimentos_disponiveis():
                    raise ValueError
                quadrados_validos = True
            except ValueError:
                print('Quadrado inválido, Tente Novamente.')
        
        return valor