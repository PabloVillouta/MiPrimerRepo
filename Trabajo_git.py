#Este codigo es para ordenar una lista de elementos
import random
Todo=[]
cuanto=True
while cuanto:
    cantidad=int(input("Ingrese la cantidad de elementos que va a ordenar "))
    if cantidad<=0:
         print("Valor invalido de elementos, porfavor intentelo de nuevo")
    else:
         cuanto=False
          
print("Escriba sus elementos:")
for elementos in range(cantidad):
    Todo.append(input("-"))

correcto=True
while correcto:
    print("¿Como quiere ordenarlo? menor a mayor (1), mayor a menor (2), aleatorio (3)")
    Modo=input()
    if Modo=="1":
            Todo.sort()
            correcto=False
    elif Modo=="2":
            Todo.sort(reverse=True)
            correcto=False
    elif Modo=="3":
        total=len(Todo)
        Copia=[]
        for item in Todo:
            antes_despues=random.randint(0,2)
            if antes_despues==1:
                Copia.append(item)
            else:
                Copia.insert(0,item)  
        Todo=Copia
        correcto=False
    else:
        print("Valor invalido, porfavor intente de nuevo")
print("Su lista a sido ordenada")
print(Todo)