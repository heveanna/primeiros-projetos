import pandas as pd
import numpy as np

class Livro:
    def __init__(self, marca, editora, ano, autor):
        self.__marca = marca
        self.editora = editora
        self.ano = ano

        self.__peso = None
        self.autor = autor
