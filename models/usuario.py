# models/usuario.py

from treino import Treino

class Usuario:
    def __init__(self):
        self.treinos = []

    def criar_treino(self, nome):
        treino = Treino(nome)
        self.treinos.append(treino)
        return treino
