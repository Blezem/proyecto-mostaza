from PIL import ImageTk, Image

def leer_imagen(path, size):
    """Lee una imagen de un archivo y la escala a un tamaño específico.

    Args:
        path (str): La ruta al archivo de imagen.
        size (tuple): El tamaño de la imagen escalada en píxeles.

    Returns:
        ImageTk.PhotoImage: Una imagen escalada.
    """

    imagen = Image.open(path)
    imagen = imagen.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(imagen)


def centrar_ventana(ventana, ancho_aplicacion, alto_aplicacion):
    """Centrar una ventana en la pantalla.

    Args:
        ventana (Tk): La ventana a centrar.
        ancho_aplicacion (int): El ancho de la ventana en píxeles.
        alto_aplicacion (int): El alto de la ventana en píxeles.
    """

    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_aplicacion / 2))
    y = int((pantalla_alto / 2) - (alto_aplicacion / 2))
    ventana.geometry(f"{ancho_aplicacion}x{alto_aplicacion}+{x}+{y}")