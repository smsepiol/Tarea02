# TAREA 02
# MAIN 

from clases_01 import Lista
from clases_01 import Binaria_recursiva
from clases_01 import Lista_vacia
from clases_01 import Mergesort

def muestra_menu():
    print("Menú Principal:")
    print("0-Imprimir lista.") # opcion para comprobar los cambios que le vamos haciendo a la lista
    print("1-Revisar si la lista esta vacia")
    print("2-Limpiar la lista")
    print("3-Obtener el tamaño de la lista")
    print("4-Eliminar elemento minimo")
    print("5-Eliminar elemento máximo")
    print("6-Agregar elemento")
    print("7-Buscar elemento")
    print("8-Obtener cantidad de presencias de un elemento")
    print("9-Obtener subcoleccion a partir de cierto elemento")
    print("10-Obtener subcoleccion en un rango ")
    print("11-Obtener subcoleccion sin repeticion")
    print("12-Remplazar elemento por uno nuevo")
    print("13-Comparar dos colecciones")
    print("14-Imprimir ascendente")
    print("15-Imprimir descendente")
    print("16-Terminar programa.")

try:
    print("TAREA 02")
    print()

    lista1=list(range(10))+[9]+[0] # 0,1,2,...,9
    obj_ordenamiento = Mergesort() # Utiliza algoritmo de ordenamiento Mergesort
    obj_elimina_repetidos = Lista_vacia() # Utiliza algoritmo de lista vacia
    obj_busqueda=Binaria_recursiva() # Utiliza algoritmo de busqueda binaria

    obj_lista = Lista(lista1,obj_ordenamiento,obj_busqueda,obj_elimina_repetidos) 

    muestra_menu()
    print()
    print(f"Lista 1: {lista1}")
    decision=int(input("Ingresa el numero que deseas realizar: "))
    print()

    while decision!=16:

        if decision==0:
            print(obj_lista._lista)
        
        elif decision==1:
            print(f"Revisando si la lista esta vacia: {obj_lista.esta_vacia()}")

        elif decision == 2:
            print("Limpiando la colección...")
            obj_lista.limpiar()
            print("Listo!")

        elif decision == 3:
            print(f"Tamaño de la lista: {obj_lista.tamanio(obj_lista._lista)}") 
            
        elif decision == 4:
            print("Eliminando elemento minimo...")
            obj_lista.eliminar_min()
            print("Listo!")

        elif decision == 5:
            print("Eliminando elemento maximo...")
            obj_lista.eliminar_max()
            print("Listo!")
                
        elif decision == 6:
            elemento_agregado=int(input("Ingresa el elemento que deseas agregar: "))
            obj_lista.agregar(elemento_agregado) 
            print("Listo!")

        elif decision == 7:
            elemento_buscado=int(input("Ingresa el elemento que deseas buscar: "))
            print(f"El indice donde se encuentra {elemento_buscado} es {obj_lista.buscar_elemento(elemento_buscado)}") 

        elif decision == 8:
            elemento_ocurrencias=int(input("Ingresa el elemento del que deseas contar sus ocurrencias: "))
            print(obj_lista.cuantos(elemento_ocurrencias))

        elif decision == 9:
            elemento_inicial=int(input("Ingresa el elemento inicial de la nueva sublista: "))
            print(obj_lista.obtener_subcoleccion(elemento_inicial)) 

        elif decision == 10:
            elemento_inicial=int(input("Ingresa el elemento inicial de la nueva sublista: "))
            elemento_final=int(input("Ingresa el elemento final de la nueva sublista: "))
            print(obj_lista.obtener_subcoleccion_rango(elemento_inicial,elemento_final))

        elif decision == 11:
            print("Obteninendo subcoleccion sin repetición...")
            print(obj_lista.subcoleccion_sin_repeticion())

        elif decision == 12:
            elemento_remplazado=int(input("Ingresa el elemento a remplazar: "))
            elemento_nuevo=int(input("Ingresa el nuevo elemento: "))
            print(obj_lista.remplazar(elemento_remplazado,elemento_nuevo))

        elif decision == 13:
            lista2=[0,1,4,7,2]
            print(f"Lista 2: {lista2}")
            print(f"Revisando si lista 1 y lista 2 son iguales: {obj_lista.__eq__(lista2)} ")

        elif decision == 14:
            print("Imprimiendo lista 1 ascendentemente:")
            obj_lista.imprimir_ascendente()

        elif decision == 15:
            print("Imprimiendo lista 1 descentendemente:")
            obj_lista.imprimir_descendente()

        else:
            print("Opcion invalida.")

        print()
        decision=int(input("Ingresa el numero (operacion) que deseas realizar: "))

except ValueError:
    print()
    print("No existe esa sublista.")
    print("Alguno de los elementos no se encuentra en la lista.")

except Exception:
    print()
    print("Ups.")

finally:
    print()
    print("Gracias por participar.")
    print("FIN DEL PROGRAMA.")
