# views.main_view.py
import flet as ft
from models.usuario import Usuario
from views.lista_treinos_view import lista_treinos_view

def main_view(page: ft.Page):
    usuario = Usuario()  # Carregar usuário a partir de dados salvos pode ser implementado aqui
    page.title = "Gym App"

    def atualizar_treinos():
        page.controls.clear()
        page.add(lista_treinos_view(page, usuario))
        page.update()

    atualizar_treinos()
