import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_principal import Panelprincipal
from main_datos import main

class App:
    
    
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == "mostaza" and password == "1234") :
            self.ventana.destroy()
            main()
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")           
                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#FA291B')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)
        
        logo =utl.leer_imagen("imagenes/logo.png", (200, 200))
     #LOGO EDICION  
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#FFFFFF')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#FFFFFF' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#FA291B')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        
      #Primer frame de inicio deseion
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#FA291B",bg='#FFFFFF',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
       

       
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")
#Boton de inicio de sesion
        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#FA291B', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))
        
        self.ventana.mainloop()
        
if __name__ == "__main__":
   App()