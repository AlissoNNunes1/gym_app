# models/treino.py

class Treino:
    def __init__(self, nome):
        self.nome = nome
        self.exercicios = []

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)
