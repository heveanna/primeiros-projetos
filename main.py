# OO E MÉTODO CONSTRUTOR

class Pessoa:
    ''' classe pessoaas'''
    def __int__(self, idade):
        self.idade = idade
        print ('A idade da pessoa é', self.idade)

idade_pessoa = input('Digite a sua idade: ')
p1 = Pessoa (idade_pessoa)

class Gato:
    def __init__ (self, nome):
        self.nome = nome
        print('Seu gato se chama', self.nome)

nome_gato = input('Digite o nome do seu gato: ')
g1 = Gato (nome_gato)