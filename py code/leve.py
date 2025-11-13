import pandas as pd 
import numpy as np

class Pessoa:
    def __init__(self, idade, altura, nome, sobrenome):
        self.idade = idade
        self.__altura = altura
        self.nome = nome
        self.sobrenome = sobrenome

    def peso_pesso(self, peso, cabelo):
        self.peso = peso
        self.cabelo = cabelo

        