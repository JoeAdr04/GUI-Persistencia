from Empleado import Empleado
from ArchivoEmpleado import ArchivoEmpleado
import tkinter as tk
from tkinter import ttk, messagebox

archivo = ArchivoEmpleado("empleados.dat")
archivo.crear()

#---------------Empieza la llamada a los archivos-------------

def actualizar():
    #archivo = ArchivoEmpleado("empleados.dat")
    tabla.delete(*tabla.get_children())
    try:
        vec = archivo.listarTodo()
        for i in range(len(vec)):
            tabla.insert("","end", values=(vec[i].getItem(),
                                        vec[i].getPaterno(),
                                        vec[i].getMaterno(),
                                        vec[i].getNombre())
                        )   
    except Exception as e:
        messagebox.showerror("Error", str(e))

def agregar():    
    try:
        emple =Empleado(int(txtItem.get()), txtPaterno.get(), txtMaterno.get(), txtNombre.get())
        archivo.adicionar(emple)
        txtPaterno.delete(0, tk.END)
        txtMaterno.delete(0, tk.END)
        txtNombre.delete(0, tk.END)
        txtPaterno.delete(0, tk.END)
        txtItem.delete(0, tk.END)
        messagebox.showinfo("Exito!", "Empleado agregado con exito")
    except Exception as e:
        messagebox.showerror("error", str(e))

def eliminar():
    try:
        archivo.eliminar(int(identificador.get()))
        messagebox.showinfo("Mensaje:", "empelado eliminado")
    except Exception as e:
        messagebox.showerror("Error de eliminacion", str(e))

def editar():
    def aceptar():
        paterno = newPatern.get()
        materno = newMatern.get()
        nombre = newNomb.get()
        try:
            emp = Empleado(int(identificador.get()), newPatern.get(), newMatern.get(), newNomb.get())
            archivo.editarEmp(int(identificador.get()),emp)
        except Exception as e:
            messagebox.showerror("Error durante la edicion", str(e))

        messagebox.showinfo("Datos ingresados", f"Paterno: {paterno}\nMaterno: {materno}\nNombre: {nombre}")
        nueva.destroy()
        
    nueva = tk.Toplevel()
    nueva.title("Ingresar datos")
    nueva.geometry("400x300")
    # Etiquetas y campos de entrada
    tk.Label(nueva, text="Paterno:").pack(pady=5)
    newPatern = tk.Entry(nueva)
    newPatern.pack(pady=5)
    tk.Label(nueva, text="Materno:").pack(pady=5)
    newMatern = tk.Entry(nueva)
    newMatern.pack(pady=5)
    tk.Label(nueva, text="Nombre:").pack(pady=5)
    newNomb = tk.Entry(nueva)
    newNomb.pack(pady=5)
    # Botón Aceptar
    btn_aceptar = tk.Button(nueva, text="Aceptar", command=aceptar)
    btn_aceptar.pack(pady=10)

#---------------Construnccion de la ventana-------------
ventana = tk.Tk()
ventana.title("Registro de trabajadores")
ventana.geometry("800x340")

caja = tk.Frame(ventana, padx = 10, pady = 10)
caja.pack(fill="both", expand=True)

tk.Label(caja, text="Paterno: ").grid(row=0, column=0, pady=5)
txtPaterno = tk.Entry(caja)
txtPaterno.grid(row = 0, column= 1, pady= 5)
tk.Label(caja, text="Materno: ").grid(row=1, column=0, pady=5)
txtMaterno = tk.Entry(caja)
txtMaterno.grid(row = 1, column= 1, pady= 5)
tk.Label(caja, text="Nombre: ").grid(row=2, column=0, pady=5)
txtNombre = tk.Entry(caja)
txtNombre.grid(row = 2, column= 1, pady= 5)
tk.Label(caja, text="Item: ").grid(row=3, column=0, pady=5)
txtItem = tk.Entry(caja)
txtItem.grid(row = 3, column= 1, pady= 5)

btnGuardar = tk.Button(caja, text="Guardar", bg="lime", width=10, command=agregar)
btnGuardar.grid(row=4, column=1, pady=5)

tk.Label(caja, text="Acciones(Item)").grid(row=5, column=0, pady=5)
identificador=tk.Entry(caja)
identificador.grid(row=5, column=1, pady=5)

btnEditar = tk.Button(caja, text="Editar", bg="yellow", width=10, command= editar)
btnEditar.grid(row=6, column=0, pady=5)

btnEliminar = tk.Button(caja, text="Eliminar", bg="red", width=10, command=eliminar)
btnEliminar.grid(row=6, column=1, pady=5)

btnActualizar = tk.Button(caja, text="Actualizar", bg="blue", command=actualizar)
btnActualizar.grid(row=6, column=2,sticky="e", pady=10)

tabla = ttk.Treeview(caja, columns=("item", "pat", "mat", "nom"), show="headings")
tabla.grid(row=0, column=2, rowspan=5, padx=15)
tabla.heading("item", text="ITEM")
tabla.column("item", width=88, stretch=True)
tabla.heading("pat", text="PATERNO")
tabla.column("pat", width=150, stretch=True)
tabla.heading("mat", text="MATERNO")
tabla.column("mat", width=150, stretch=True)
tabla.heading("nom", text="NOMBRE")
tabla.column("nom", width=150, stretch=True)





actualizar()

ventana.mainloop()


    
    
