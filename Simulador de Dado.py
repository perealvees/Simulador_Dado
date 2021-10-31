import random

class SimuladordeDados:
       def __init__(self):
           self.valor_minimo = 1
           self.valor_maximo = 6
           self.mensagem = 'Você gostaria de jogar o dado novamente?'

       def iniciar(self):
           print(self.mensagem)
