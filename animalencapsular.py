class Animal:
    def __init__ (self,nombre, edad, raza, historial,datosDuenios) :
      self.nombre=nombre
      self.edad=edad
      self.raza=raza
      self.historial=historial
      self.datosDuenios=datosDuenios

    def nomostrar(self):#condiciona al mostrar para que lo vean ciertas personas, metodo publico #solo esta puede llamar a mostrar
        self.__mostrar()#metodo privado no accesible para los externos
        
    def mostrar(self):
     print(f"NOMBRE {self.nombre}, edad:{self.edad}, raza: {self.raza}, historial: {self.historial}, datosDuenios: {self. datosDuenios}")
    #f es una abrevaciòn del print para no poner tantas comillas
    
    

class Gato(Animal):
 def __init__ (self,nombre, edad, raza, historial,datosDuenios,orejas,cola, unias):
  super().__init__ (nombre, edad, raza, historial,datosDuenios)
  self.orejas=orejas
  self.cola=cola
  self.unias=unias

 def mostrar(self):
   super().mostrar()
   print(f" Orejas: {self.orejas } COLA:{self.cola}, Unias:{self.unias}")


a1=Animal("pepe",2,"belga","garrapatas","juam telefon: 304945855")
#no va "a1.mostrar()" pq va a salir error
a1.nomostrar()
#hace falta llamar a la función nomostrar para enseñar toda la informacion

g1=Gato("pepito",2,"siames","garrapatas y pulgas", "juana teléfono: 304945345", 2, 1, "filosas" )
g1.mostrar() #incorrecto
g1.nomostrar() #correcto
