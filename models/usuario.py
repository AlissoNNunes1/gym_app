# models/usuario.py

from models.treino import Treino

class Usuario:
    def __init__(self):
        self.treinos = []

    def criar_treino(self, nome, grupos_musculares):
        treino = Treino(nome, grupos_musculares)
        self.treinos.append(treino)
        return treino