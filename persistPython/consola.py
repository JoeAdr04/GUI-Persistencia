from Empleado import Empleado
from ArchivoEmpleado import ArchivoEmpleado


class Main():
    print("hola")
    
    archivo = ArchivoEmpleado("hola.dat")
    archivo.crear()
    e1 = Empleado(2,"tarqui", "gutierez", "Joel")
    archivo.adicionar(e1)
    #archivo.eliminar_todo()
    vec= archivo.listarTodo()
    for i in range(len(vec)):
        print(vec[i])
    print("-----------")
    print(archivo.buscarItem(2))
    
if __name__ == "__main__":
    app = Main()