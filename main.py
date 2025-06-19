# OO E MÉTODO CONSTRUTOR

class Gato:
    def __init__ (self, nome):
        self.nome = nome
        print('Seu gato se chama', self.nome)

    def peso_gato (self, peso):
        self.peso = peso
        if (self.peso > 5.0):
            print ('Seu gato está gordinho!')
        elif (self.peso > 3.5):
            print ('Peso noraml!')
        else:
            print('O animal está abaixo do peso!')

    def _dieta_especial_gato(self):
        self.msg = 'Tudo ok!'
        if (self.peso < 3.5 ):
            self.msg =  'Aumente a ração do felino'
        if (self.peso >= 5.0):
            self.msg = 'Diminiu a ração do felino'
        return self.msg
    
    def dados_gato (self):
        print ('\n O gato', self.nome, 'está com', self.peso)
        print (self._dieta_especial_gato())

    def altura_gato (self, altura):
        self.altura_gato = altura
        print

nome_gato = input('Digite o nome do seu gato: ')
g1 = Gato (nome_gato)

peso = float(input('\n Qual o peso do sei gato, em kg?'))
g1.peso_gato(peso)

g1.dados_gato()