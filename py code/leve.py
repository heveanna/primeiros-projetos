import pandas as pd 

class Pessoa:
    def __init__(self, idade, altura, nome):
        self.idade = idade
        self.__altura = altura
        self.nome = nome

    def peso_pesso(self, peso, cabelo):
        self.peso = peso
        self.cabelo = cabelo


print ("Informa a idade da pessoa: ")
        
        