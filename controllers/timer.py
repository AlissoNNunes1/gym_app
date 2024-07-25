# controllers.py
import time

class Cronometro:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
    
    def iniciar(self):
        self.start_time = time.time()
    
    def encerrar(self):
        if self.start_time:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None
    
    def resetar(self):
        self.start_time = None
        self.elapsed_time = 0
    
    def tempo_decorrido(self):
        if self.start_time:
            return time.time() - self.start_time + self.elapsed_time
        return self.elapsed_time
