# components/cronometro.py

import flet as ft
import time
import threading

class Cronometro:
    def __init__(self, page: ft.Page):
        self.page = page
        self.running = False
        self.reset = True
        self.time_elapsed = 0
        self.interval = 5  # Default interval in seconds for the sound to play

        self.sound = ft.Audio(src="https://github.com/AlissoNNunes1/gym_app/raw/main/assets/blip.mp3")
        page.overlay.append(self.sound)

        self.timer_label = ft.Text(value="00:00:00", size=30)
        self.start_button = ft.FloatingActionButton(icon=ft.icons.PLAY_ARROW, on_click=self.start_timer)
        self.pause_button = ft.FloatingActionButton(icon=ft.icons.PAUSE, on_click=self.pause_timer)
        self.stop_button = ft.FloatingActionButton(icon=ft.icons.STOP, on_click=self.stop_timer)
        self.interval_input = ft.TextField(label="Interval (seconds)", value=str(self.interval), on_change=self.update_interval)

        self.layout = ft.Column([
            self.timer_label,
            ft.Row([self.start_button, self.pause_button, self.stop_button]),
            self.interval_input
        ])

        self.page.add(ft.SafeArea(self.layout))

        # Aplicando alinhamento ao cronômetro
        self.layout.alignment = ft.alignment.top_center  # Top center alignment

    def update_timer_label(self):
        hours, remainder = divmod(self.time_elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.value = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        self.page.update()

    def timer_thread(self):
        while self.running:
            time.sleep(1)
            self.time_elapsed += 1
            self.update_timer_label()
            if self.time_elapsed % self.interval == 0:
                self.sound.play()

    def start_timer(self, e):
        if self.reset:
            self.time_elapsed = 0
            self.reset = False
        self.running = True
        threading.Thread(target=self.timer_thread).start()
        self.start_button.enabled = False
        self.pause_button.enabled = True
        self.stop_button.enabled = True
        self.page.update()

    def pause_timer(self, e):
        self.running = False
        self.start_button.enabled = True
        self.pause_button.enabled = False
        self.page.update()

    def stop_timer(self, e):
        self.running = False
        self.reset = True
        self.time_elapsed = 0
        self.update_timer_label()
        self.start_button.enabled = True
        self.pause_button.enabled = False
        self.stop_button.enabled = False
        self.page.update()

    def update_interval(self, e):
        try:
            self.interval = int(e.control.value)
        except ValueError:
            self.interval = 5  # Reset to default if input is invalid
        self.page.update()