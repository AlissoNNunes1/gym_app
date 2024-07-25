# views/timer_view.py
import flet as ft
from controllers.timer import Cronometro

def cronometro_view(page: ft.Page):
    cronometro_label = ft.Text("Tempo: 0s")
    cronometro = Cronometro()

    def iniciar_cronometro(e):
        cronometro.iniciar()
        page.update()
        atualizar_cronometro()

    def encerrar_cronometro(e):
        cronometro.encerrar()
        page.update()

    def atualizar_cronometro():
        if cronometro.start_time:
            cronometro_label.value = f"Tempo: {int(cronometro.tempo_decorrido())}s"
            page.update()
            page.window.schedule_callback(1, lambda: atualizar_cronometro())

    iniciar_cronometro_button = ft.ElevatedButton(text="Iniciar Treino", on_click=iniciar_cronometro)
    encerrar_cronometro_button = ft.ElevatedButton(text="Encerrar Treino", on_click=encerrar_cronometro)

    return ft.Column([
        cronometro_label,
        iniciar_cronometro_button,
        encerrar_cronometro_button
    ])