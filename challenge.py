#Challenge - Moodle

class Persona:
 def __init__(self, nombre, apellido, telefono, direccion):
 self.nombre = nombre
 self.apellido = apellido
 self.telefono = telefono
 self.direccion = direccion
 def getPersona(self):
 return self.nombre + ' ' + self.apellido + ' ' + self.telefono + ' ' + self.direccion
class Nodo:

 def __init__(self, value=None, izq=None, der=None):

 self.value = value
 self.izq = izq
 self.der = der
 
 def __str__(self):
 return self.value.getPersona()
 def tieneHijoIzquierdo(self):
 return self.izq != None
 def tieneHijoDerecho(self):
 return self.der != None

class aBinarios:

 def __init__(self):
 self.raiz = None

 def agregar(self, elemento):
 if self.raiz == None:
 self.raiz = elemento
 else:
 aux = self.raiz
 padre = None
 while aux != None:
 padre = aux
 if aux.tieneHijoIzquierdo():
 aux = aux.der
 else:
 aux = aux.izq

 if padre:
 padre.der = elemento
 else:
 padre.izq = elemento
 
 #Preorden
 def preorden(self, elemento):
 if elemento != None:
 print(elemento)

 def postorden(self, elemento):
 if elemento != None:
 self.postorden(elemento.izq)
 self.postorden(elemento.der)
 print(elemento)
 
 #Inorden
 def inorden(self, elemento):
 if elemento != None:
 self.inorden(elemento.izq)
 print(elemento)
 self.inorden(elemento.der)
 
 def getRaiz(self):
 return self.raiz

#Menu
if __name__ == "__main__":

 ab = aBinarios()
 while(True):
 
 print("Arboles_Binarios\n"+
 "1. Agregar\n"+
 "2. Preorden\n"+
 "3. Postorden\n"+
 "4. Inorden\n"+
 "5. Level\n"+
 "6. Salir")
 num = input("ingrese la opcion: ")
 if num == "1":
 nombre = input("Ingrese el nombre: ")
 apellido = input("Ingrese el apellido: ")
 telefono = input("Ingrese el telefono: ")
 direccion = input("Ingrese el direccion: ")
 persona = Persona(nombre, apellido, telefono, direccion)
 nod = Nodo(persona)
 ab.agregar(nod)
 elif num == "2":
 print("Preorden")
 ab.preorden(ab.getRaiz())
 elif num == "3":
 print("postorden")
 ab.postorden(ab.getRaiz())
 elif num == "4":
 print("inorden")
 ab.inorden(ab.getRaiz())
 elif num == "5":
 print("encontrar")
 ab.get
 elif num == "6":
 exit()