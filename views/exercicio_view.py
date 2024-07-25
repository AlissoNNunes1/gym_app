import flet as ft
from models.exercicio import Exercicio

def exercicio_view(page: ft.Page, treino_selecionado):
    exercicio_name_input = ft.TextField(label="Nome do Exercício")
    series_input = ft.TextField(label="Séries")
    repeticoes_input = ft.TextField(label="Repetições")
    exercicios_list_view = ft.ListView()

    def adicionar_exercicio(treino, nome, series, repeticoes):
        exercicio = Exercicio(nome, series, repeticoes)
        treino.adicionar_exercicio(exercicio)
        exercicios_list_view.controls.append(ft.Text(f"Exercício: {exercicio.nome}, Séries: {exercicio.series}, Repetições: {exercicio.repeticoes}"))
        page.update()

    adicionar_exercicio_button = ft.ElevatedButton(
        text="Adicionar Exercício",
        on_click=lambda e: adicionar_exercicio(treino_selecionado, exercicio_name_input.value, series_input.value, repeticoes_input.value)
    )

    return ft.Column([
        ft.Text("Adicionar Exercícios ao Treino Selecionado"),
        exercicio_name_input,
        series_input,
        repeticoes_input,
        adicionar_exercicio_button,
        exercicios_list_view
    ])