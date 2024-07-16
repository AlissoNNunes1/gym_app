import flet as ft
from components.navbar import Navbar
from components.cronometro import Cronometro
def main(page: ft.Page):
    Cronometro(page)
    Navbar(page)
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)
