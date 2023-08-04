import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.local_dao  import crear_tabla, borrar_tabla
from model.local_dao import Local, guardar_local,listar,editar,eliminar
from mapas import mostrar_mapas


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)
    
    
    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)
    
    menu_inicio.add_command(label='Crear Registro en DB',command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command = root.destroy)
    
    barra_menu.add_cascade(label='Consulta')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')





class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 1080, height=720)
        self.root = root
        self.pack()
        self.config(bg= 'white')
        
        self.id_local = None
        
        self.local_comida()
        self.deshabilitar_campos()
        self.tabla_comida()
        
        
    def local_comida(self):
        
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font = ('Arial',12,'bold'))
        
        self.label_nombre.grid(row = 0, column= 0, padx =10, pady=10)
        
        self.label_ubicacion = tk.Label(self, text='Ubicación: ')
        self.label_ubicacion.config(font = ('Arial',12,'bold'))
        self.label_ubicacion.grid(row = 1, column= 0,padx =10, pady=10)
        
        self.label_puntuacion= tk.Label(self, text='Puntuación: ')
        self.label_puntuacion.config(font = ('Arial',12,'bold'))
    
        self.label_puntuacion.grid(row = 2, column= 0,padx =10, pady=10)
        
        self.label_ingredientes= tk.Label(self, text='evento: ')
        self.label_ingredientes.config(font = ('Arial',12,'bold'))
    
        self.label_ingredientes.grid(row = 4, column= 0,padx =10, pady=10)
        
        self.label_eventos = tk.Label(self, text='ingredientes: ')
        self.label_eventos.config(font = ('Arial',12,'bold'))
        
        self.label_eventos.grid(row = 5, column= 0,padx =10, pady=10)
    
    #Entradas de cada campo
        self.mi_nombre= tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width=50,font =('Arial', 12))
        self.entry_nombre.grid(row=0, column =1,padx =10, pady=10, columnspan = 2)
        
        self.mi_ubicacion= tk.StringVar()
        self.entry_ubicacion = tk.Entry(self, textvariable= self.mi_ubicacion)
        self.entry_ubicacion.config(width=50, font =('Arial', 12))
        self.entry_ubicacion.grid(row=1, column =1,padx =10, pady=10, columnspan = 2)
        
        self.mi_puntuacion= tk.StringVar()
        self.entry_puntuacion = tk.Entry(self, textvariable= self.mi_puntuacion)
        self.entry_puntuacion.config(width=50, font =('Arial', 12))
        self.entry_puntuacion.grid(row=2, column =1,padx =10, pady=10, columnspan = 2)
        
        self.mi_ingrediente= tk.StringVar()
        self.entry_ingredientes = tk.Entry(self, textvariable= self.mi_ingrediente)
        self.entry_ingredientes.config(width=50, font =('Arial', 12))
        self.entry_ingredientes.grid(row=5, column =1,padx =10, pady=10, columnspan = 2)
        
        self.mi_evento= tk.StringVar()
        self.entry_eventos = tk.Entry(self, textvariable= self.mi_evento)
        self.entry_eventos.config(width=50, font =('Arial', 12))
        self.entry_eventos.grid(row=4, column =1,padx =10, pady=10, columnspan = 2)
        
    #botones
        self.boton_nuevo=tk.Button(self, text='Nuevo ingreso', command= self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font=('Arial', 12, 'bold'),
                                fg='white',bg = '#70000B',
                                cursor ='hand2', activebackground = '#35BD6F')
        self.boton_nuevo.grid(row = 2, column=5,padx =10, pady=10)
        
        self.boton_guardar=tk.Button(self, text='Guardar',command=self.guardar_datos)
        self.boton_guardar.config(width = 20, font=('Arial', 12, 'bold'),
                                fg='white',bg = '#71E03A',
                                cursor ='hand2', activebackground = '#3586DF')
        self.boton_guardar.grid(row = 3, column=5,padx =10, pady=10)
        
        self.boton_cancelar=tk.Button(self, text='Cancelar', command= self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, font=('Arial', 12, 'bold'),
                                fg='white',bg = '#3B7FF5',
                                cursor ='hand2', activebackground = '#E15370')
        self.boton_cancelar.grid(row = 4, column=5,padx =10, pady=10)
        
        #Habilita los campos
    def habilitar_campos(self):
            self.entry_nombre.config(state='normal')
            self.entry_ubicacion.config(state='normal')
            self.entry_puntuacion.config(state='normal')
            self.entry_ingredientes.config(state='normal')
            self.entry_eventos.config(state='normal')
            
            self.boton_guardar.config(state= 'normal')
            self.boton_cancelar.config(state='normal')
        
    def deshabilitar_campos(self):
            self.id_local = None
            self.mi_nombre.set('')#metodo set envia los datos a los campos, en este caso envia datos vacios
            self.mi_ubicacion.set('')
            self.mi_puntuacion.set('')
            self.mi_ingrediente.set('')
            self.mi_evento.set('')
            self.entry_nombre.config(state='disabled')
            self.entry_ubicacion.config(state='disabled')
            self.entry_puntuacion.config(state='disabled')
            self.entry_ingredientes.config(state='disabled')
            self.entry_eventos.config(state='disabled')
            
            self.boton_guardar.config(state= 'disabled')
            self.boton_cancelar.config(state='disabled')
            
    def guardar_datos(self):
        local1= Local(
            self.mi_nombre.get(),
            self.mi_ubicacion.get(),
            self.mi_puntuacion.get(),
            self.mi_ingrediente.get(),
            self.mi_evento.get(),
        )
        if self.id_local== None:
            
            guardar_local(local1)
        else:
            editar(local1,self.id_local)
        
        self.tabla_comida()
        
        
        
        self.deshabilitar_campos()
        

    def tabla_comida(self):
        #recuperar lista
        self.lista_locales = listar()
        self.lista_locales.reverse() #la tabla se genera de forma ascendente, con este se realiza de forma descendente
        
        self.tabla = ttk.Treeview(self, 
        column = ('Nombre','Ubicacion','Puntuacion','Ingredientes','Eventos'))
        self.tabla.grid(row=6, column= 0, columnspan = 6, sticky = 'nse')
        
        #scroollbar para la tabla si excede 10 registros
        self.scroll =ttk.Scrollbar(self,
        orient = 'vertical', command= self.tabla.yview)
        self.scroll.grid(row = 6, column = 6, sticky = 'nse')
        self.tabla.config(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Ubicacion')
        self.tabla.heading('#3', text='Puntuacion')
        self.tabla.heading('#4', text='Ingrediente')
        self.tabla.heading('#5', text='Eventos')
        
        #iterar la lista de locales
        for l in self.lista_locales:
            
            self.tabla.insert('',0, text=l[0],
            values = (l[1], l[2], l[3], l[4], l[5]))
            
            
            
        #boton de ver mapas
        
        self.boton_mostrar_mapa=tk.Button(self, text='Mapas', command = mostrar_mapas)
        self.boton_mostrar_mapa.config(width = 20, font=('Arial', 12, 'bold'),
                                fg='white',bg = '#3B7FF5',
                                cursor ='hand2', activebackground = '#71E03A')
        self.boton_mostrar_mapa.grid(row = 7, column=2,padx =10, pady=10)
        
        
        
        #boton de editar
        
        self.boton_editar=tk.Button(self, text='Editar', command = self.editar_datos)
        self.boton_editar.config(width = 20, font=('Arial', 12, 'bold'),
                                fg='white',bg = '#71E03A',
                                cursor ='hand2', activebackground = '#35BD6F')
        self.boton_editar.grid(row = 7, column=0,padx =10, pady=10)
        
        
        #boton de eliminar
        self.boton_eliminar=tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.config(width = 20, font=('Arial', 12, 'bold'),
                                fg='white',bg = '#BD162E',
                                cursor ='hand2', activebackground = '#E15370')
        self.boton_eliminar.grid(row = 7, column=1,padx =10, pady=10)
        
        
        
    def editar_datos(self):
     
        try:
            self.id_local = self.tabla.item(self.tabla.selection()) ['text']
            self.nombre_local = self.tabla.item(self.tabla.selection()) ['values'][0]
            self.ubicacion_local = self.tabla.item(self.tabla.selection()) ['values'][1]
            self.puntuacion_local = self.tabla.item(self.tabla.selection()) ['values'][2]
            self.ingredientes_local = self.tabla.item(self.tabla.selection()) ['values'][3]
            self.eventos_local = self.tabla.item(self.tabla.selection()) ['values'][4]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0,self.nombre_local)
            self.entry_ubicacion.insert(0,self.ubicacion_local)
            self.entry_puntuacion.insert(0,self.puntuacion_local)
            self.entry_ingredientes.insert(0,self.ingredientes_local)
            self.entry_eventos.insert(0,self.eventos_local)
        except:
            titulo='Edicion de datos'
            mensaje =' No se ah seleccionado ningun dato'
            messagebox.showerror(titulo, mensaje)
            
    def eliminar_datos(self):
        try:
            self.id_local = self.tabla.item(self.tabla.selection()) ['text']
            eliminar(self.id_local)
        
            self.tabla_comida()
            self.id_local = None
        
        except:
            titulo ='Eliminar un Registro'
            mensaje='No se ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
            
