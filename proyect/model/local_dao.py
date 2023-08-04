from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE locales(
        id_local INTEGER,
        nombre VARCHAR(100),
        ubicacion VARCHAR(100),
        puntuacion VARCHAR(2),
        ingredientes VARCHAR(100),
        eventos VARCHAR(100),
        PRIMARY KEY(id_local AUTOINCREMENT)
        
    )'''
    
    try:
         conexion.cursor.execute(sql)
         conexion.cerrar()
         titulo= 'Crear Registro'
         mensaje='Se creo la tabla en la base de datos'
         messagebox.showinfo(titulo, mensaje)
    
    except:
         titulo= 'Crear Registro'
         mensaje='La tabla ya esta creada'
         messagebox.showwarning(titulo, mensaje)
    
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql= 'DROP TABLE locales'
    
    try:
         conexion.cursor.execute(sql)
         conexion.cerrar()
         titulo= 'Borrar Registro'
         mensaje= 'La tabla de la base de datos se borro con exito'
         messagebox.showinfo(titulo, mensaje)
    
    except:
         titulo= 'Borrar Registro'
         mensaje='No hay tabla para borrar'
         messagebox.showerror(titulo, mensaje)
    
    
    
    

class Local:
    def __init__(self, nombre, ubicacion, puntuacion, ingredientes, eventos):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.puntuacion = puntuacion
        self.ingredientes = ingredientes
        self.eventos = eventos

# Ahora, crearemos la función para guardar datos en la tabla "locales"
def guardar_local(local):
    conexion = ConexionDB()

    sql = f'''INSERT INTO locales (nombre, ubicacion, puntuacion, ingredientes, eventos)
              VALUES('{local.nombre}', '{local.ubicacion}', '{local.puntuacion}', 
                     '{local.ingredientes}', '{local.eventos}')'''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Guardar Registro'
        mensaje = 'Los datos se guardaron correctamente en la tabla.'
        messagebox.showinfo(titulo, mensaje)
    except Exception as e:
        titulo = 'Guardar Registro'
        mensaje = f'Error al guardar datos en la tabla: {str(e)}'
        messagebox.showerror(titulo, mensaje)
        
def listar(): 
    #Recopilamos los datos de la lista
    conexion = ConexionDB()
    
    lista_locales=[]
    sql = 'SELECT * FROM locales'
    
    try:
        conexion.cursor.execute(sql)
        lista_locales = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
        
    return lista_locales
        
def editar(local, id_local):
    conexion = ConexionDB()

    sql = f"""UPDATE locales
            SET nombre = '{local.nombre}', ubicacion = '{local.ubicacion}',
                puntuacion = '{local.puntuacion}', ingredientes = '{local.ingredientes}',
                eventos = '{local.eventos}' 
            WHERE id_local = {id_local}"""

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()
        conexion.cerrar()
        messagebox.showinfo("Edicion de datos", "Registro editado correctamente")
    except Exception as e:
        messagebox.showerror("Edicion de datos", f"No se ha podido editar este registro: {str(e)}")
        
def eliminar(id_local):
    conexion = ConexionDB()
    sql = f'DELETE FROM locales WHERE id_local = {id_local}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()
        conexion.cerrar()
    except:
        titulo='Eliminar Datos'
        mensaje ='No se pudo eliminar el registro'
        messagebox.showerror(titulo,mensaje)
    









