import pygame as py
from pygame.locals import QUIT

from gestor_estados import GestorEstados

class Nucleo(object):
    '''Nucleo del motor'''
    
    '''Constructor, inicia todos los componentes necesarios para ejecutar el juego
        titulo: Titulo de la pantalla
        swidth: Anchura de la pantalla
        sheight: Altura de la pantalla
        nfps: FPS del juego
        clear: Color usado para limpiar la pantalla'''
    def __init__(self, titulo, swidth, sheight, nfps, limpiar):
        py.init()
        self.pantalla = py.display.set_mode((swidth, sheight))
        py.display.set_caption(titulo)

        self.exit = False
        self.limpiar = limpiar
        self.fps = py.time.Clock()
        self.delta = self.fps.tick(nfps)
        self.nfps = nfps
        self.gestorEstados = GestorEstados()

    '''Inicia el bucle del juego'''
    def iniciar(self):
        while not self.exit:
            for event in py.event.get():
                if event.type == QUIT:
                    self.exit = True
            self.pantalla.fill(self.limpiar)
            
            self.gestorEstados.actualizar(self.delta)
            self.gestorEstados.dibujar(self.pantalla)
            
            py.display.update()
            self.delta = self.fps.tick(self.nfps)
        py.quit()
        return 0
