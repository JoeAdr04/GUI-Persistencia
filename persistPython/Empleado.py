class Empleado:
    def __init__(self, item=0, paterno="", materno="", nombre=""):
        self.__item = item
        self.__paterno = paterno
        self.__materno = materno
        self.__nombre = nombre
    
    def getItem(self):
        return self.__item
    def getPaterno(self):
        return self.__paterno
    def getMaterno(self):
        return self.__materno
    def getNombre(self):
        return self.__nombre

    def setItem(self, item):
        self.__item = item
    def setPaterno(self, paterno):
        self.__paterno = paterno
    def setMaterno(self, materno):
        self.__materno = materno
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def __str__(self):
        return (f"Item: {self.__item}Paterno: {self.__paterno}, Materno: {self.__materno}, Nombre: {self.__nombre}")