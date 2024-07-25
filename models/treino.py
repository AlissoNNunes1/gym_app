# models/treino.py

class Treino:
    def __init__(self, nome, grupos_musculares):
        self.nome = nome
        self.grupos_musculares = grupos_musculares
        self.exercicios= []

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)
