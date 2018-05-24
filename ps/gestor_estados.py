class GestorEstados(object):

    '''Clase que gestiona todos los estados del juego'''

    '''Constructor
        Inicializa todos los elementos necesarios'''
    def __init__(self):
        self.estados = {}
        self.estadoActual = ""

    '''Actualiza el estado seleccionado actualmente
        delta: Tiempo de juego, necesario para llevar a cabo algunas acciones'''
    def actualizar(self, delta):
        self.estados[self.estadoActual].actualizar(delta)

    '''Dibuja el estado seleccionado actualmente
        pantalla: Superficie donde se dibujara el estado'''
    def dibujar(self, pantalla):
        self.estados[self.estadoActual].dibujar(pantalla)
        
    '''Anadie un nuevo estado a la lista de estados
        clave: Clave del estado que se anadira
        estado: Estado que se anadira'''
    def addEstado(self, clave, estado):
        self.estados[clave] = estado

    '''Cambia el estado actual
        clave: Clave del estado al que se quiere cambiar'''
    def cambiarEstado(self, clave):
        self.estadoActual = clave
