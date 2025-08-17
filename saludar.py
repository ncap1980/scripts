import tkinter as tk

def saludar():
    texto['text'] =  "Hola amigo"
	
def despedir():
    texto['text'] = "Hasta la vista"
	
principal = tk

##principal.wm_title("programa de prueba")

texto = tk.messagebox.message(principal, text="Saluda")

boton_saluda = tk.button(principal, text="hola", command=saludar)

boton_despide = tk.button(principal, text="Adios", command=despedir)

texto.pack()
boton_saluda.pack()
boton_despide.pack()

principal.mainloop()
