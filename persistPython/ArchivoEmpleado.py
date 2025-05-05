import pickle
import os

class ArchivoEmpleado:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def crear(self):
        #Crea un archivo vacío si no existe.
        try:
            #Pregunta si el archivo existe
            if not os.path.exists(self.nombre_archivo):
                
                with open(self.nombre_archivo, 'wb') as f:
                    pickle.dump([], f)#carga una lista vacia al archivo
            print("Archivo creado o ya existente.")
        except Exception as e: #tambien manejamos excepciones
            print(f"Error al crear archivo: {e}")

    def adicionar(self, empleado):
        """Agrega un empleado al archivo."""
        try:
            empleados = self.listarTodo()  # Leer los existentes
            empleados.append(empleado)
            with open(self.nombre_archivo, 'wb') as f:
                pickle.dump(empleados, f)
            print("Empleado agregado.")
        except Exception as e:
            print(f"Error al adicionar empleado: {e}")

    def listarTodo(self):
        """Devuelve la lista de todos los empleados."""
        try:
            if not os.path.exists(self.nombre_archivo):
                return []
            with open(self.nombre_archivo, 'rb') as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []
        except Exception as e:
            print(f"Error al leer empleados: {e}")
            return []
            
    def eliminar(self, item):
        try:
            empleados = self.listarTodo()
            empleados_filtrados = []
            print(f"entrada de texto{item}")
            for i in range(len(empleados)):
                if(empleados[i].getItem() != int(item)):
                    print(empleados[i].getItem())
                    empleados_filtrados.append(empleados[i])
            with open(self.nombre_archivo, 'wb') as f:
                pickle.dump(empleados_filtrados, f)
        except Exception as e:
            raise Exception(f"Error al eliminar: {e}")
        
    def editarEmp(self, item, emp):
        try:
            empleados = self.listarTodo()
            empleados_filtrados = []
            print(f"entrada de texto{item}")
            for i in range(len(empleados)):
                if(empleados[i].getItem() != int(item)):
                    #print(empleados[i].getItem())
                    empleados_filtrados.append(empleados[i])
                else:
                    empleados_filtrados.append(emp)
                    
            with open(self.nombre_archivo, 'wb') as f:
                pickle.dump(empleados_filtrados, f)
        except Exception as e:
            raise Exception(f"Error al eliminar: {e}")