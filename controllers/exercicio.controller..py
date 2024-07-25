# controllers.py

from models.models import Exercicio, Treino, Usuario

def adicionar_exercicio(treino, nome, series, repeticoes):
    exercicio = Exercicio(nome, series, repeticoes)
    treino.adicionar_exercicio(exercicio)


