import tkinter as tk
from controller.controlador_principal import ControladorPrincipal

def mostrar_mapas():
    root = tk.Tk()
    root.title("Locales en la Zona")
    controlador = ControladorPrincipal(root)
    root.mainloop()
    
if __name__ =='__main__':
    mostrar_mapas()