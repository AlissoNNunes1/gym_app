# views/treino_view
import flet as ft
from views.exercicio_view import exercicio_view

def treino_view(page: ft.Page, treino):
    def adicionar_exercicio(e):
        page.controls.clear()
        page.add(exercicio_view(page, treino))
        page.update()

    lista_exercicios = ft.ListView()
    for exercicio in treino.exercicios:
        lista_exercicios.controls.append(ft.Text(f"Exercício: {exercicio.nome}, Séries: {exercicio.series}, Repetições: {exercicio.repeticoes}"))

    adicionar_exercicio_button = ft.ElevatedButton(text="Adicionar Exercício", on_click=adicionar_exercicio)

    return ft.Column([
        ft.Text(f"Treino: {treino.nome} - {treino.grupos_musculares}"),
        lista_exercicios,
        adicionar_exercicio_button,
        # Adicionar outras funcionalidades, como iniciar e encerrar treino
    ])
