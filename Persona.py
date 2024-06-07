##################################################
 ################ HERENCIA SIMPLE ###############
##################################################

#SUPER CLASE
class Persona:
    def __init__(self,
                 nombre,
                 edad,
                 nacionalidad):

        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def toString(self):
        print(self.nombre, self.edad, self.nacionalidad)

    def Saludar(self):
        print(self.nombre, "Esta Saludando!")

perso = Persona("nico","17","arg")


print(perso.toString())
#Fin de clase Persona

#CLASE Hija con herencia simple
class Empleado(Persona):# <-Se asigna la clase a cual heredar
    #Se declara el super para los atributos de la superclase
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

emple = Empleado("Roberto","22", "Germany", "Programador", "400k")

print(emple.Saludar())


#CLASE Hija con herencia simple
class Estudiante(Persona):# <-Se asigna la clase a cual heredar
    #Se declara el super para los atributos de la superclase
    def __init__(self, nombre, edad, nacionalidad, universidad, notas):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.notas = notas

    def Datos(self):
        return [self.nombre, self.edad , self.nacionalidad,
              self.universidad, self.notas]

estu = Estudiante("Damian","24", "Arg",
                  "UNNE", 8.57)

print(estu.Saludar())
print(estu.Datos())



##################################################
 ################ HERENCIA MULTIPLE ###############
##################################################
class Artista:
    def __init__(self,
                 habilidad,):
        self.habilidad = habilidad

    def Mostrar_Habilidad(self):
        print(self.habilidad)

#Creacion de empleadoArtista
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, instrumento):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)

        self.instrumento = instrumento

    def presentarse(self):
        #Utilizamos super para usar metodos del padre,
        #   si quiero utilizar metodos de mi clase hija
        #   solo utilizo self
        print("ARTISTA:")
        return super().toString(), super().Mostrar_Habilidad()

artista = EmpleadoArtista("Gustavo","77","arg",
                          "Cantar","Microfono")

artista.presentarse()












