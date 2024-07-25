# controllers/exercicio.controller.py

from models.exercicio import Exercicio


def adicionar_exercicio(treino, nome, series, repeticoes):
    exercicio = Exercicio(nome, series, repeticoes)
    treino.adicionar_exercicio(exercicio)


