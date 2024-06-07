class A:
    def hablar(self):
        print("Hola desde A")
class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()

#print(D.mro())

B.hablar(d)#Devuelve Hola desde "B"
# Porque ejecuto el metodo de B pero le paso
#por parametro el objeto d.