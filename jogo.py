import time
from jogador import Jogador2,ComputadorPlayer

class JogoDaVelha:
    def __init__(self):
        self.quadro = ['' for _ in range(9)]
        self.vencedor = None

    def mostrar_quadro(self):
        for linha in[self.quadro[i*3:(i+1)*3] for i in range(3)]:
            print('| ' +' | '.join(linha) + ' |')

    @staticmethod
    def mostrar_numero_no_quadro():
        numero_no_quadro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in numero_no_quadro:
            print('| ' +' | '.join(linha) + ' |')
    
    def movimentos_disponiveis():
        return [i for i, local in enumerar(self.quadro) if spot == ' ']
    
    def quadros_vazios(self):
        return ' ' in self.quadro
    
    def numero_quadro_vazio(self):
        return self.quadro.count(' ')
    
    def fazer_movimento(self, quadro, letra):
        if self.quadro[quadrado] == ' ':
            self.quadro[quadrado] =letra
            if self.ganhador(quadrado, letra):
                self.vencedor = letra
            return True
        return False
    
    def ganhador(self, quadrado, letra):

        linha_ind = quadrado // 3
        linha = self.quadro[linha_ind*3 : (linha_ind + 1) *3]
        if all([local == letra for local in linha]):
            return True
        
        coluna_ind = quadrado % 3 
        coluna = [self.quadro[coluna_ind+i*3] for i in range(3)]
        if all([local == letra for local in coluna]):
            return True
        
        if quadrado % 2 == 0:
            diagonal_1 = [self.quadro[i] for i in [0, 4, 8]]
            if all([local == letra for local in diagonal_1]):
                return True 
            diagonal_2 = [self.quadro[i] for i in [2, 4, 6]] 
            if all([local == letra for local in diagonal_2]):
                return True
                    
        return False

def jogar(jogo, x_jogador, o_jogador,mostrar_jogo=True):
    if mostrar_jogo:
        jogo.mostrar_numero_no_quadro()
        letra = 'X' 
        while jogo.quadros_vazios():
            if letra == 'O':
                quadro == o_jogador.get_movimento(jogo)
            else:
                quadro = x_jogador.get_movimento(jogo)

            if jogo.fazer_movimento(quadrado, letra):
                if mostrar_jogo:
                    print(letra + f' Faça um movimento no quadro {quadrado}')
                    jogo.mostrar_quadro()
                print('')

            if jogo.vencedor:
                if mostrar_jogo:
                        print(letra +' venceu!')
                return letra                
                
            letra = 'O' if letra == 'X' else 'X'

        time.sleep(0.8)
    if mostrar_jogo:
        print('Empate')

if __name__ == '__main__':
    x_jogador = Jogador2('X')
    o_jogador = ComputadorPlayer('O')
    v = JogoDaVelha()
    jogar(v,x_jogador,o_jogador, mostrar_jogo=True)