# TAREA 02
# CLASES

from typing import List
from interfaces_01 import Estructuras_organizadas_abstract
from interfaces_01 import Algoritmos_ordenamiento_abstract
from interfaces_01 import Algortimos_busqueda_abstract
from interfaces_01 import Algoritmos_repeticcion_abstract

class Lista(Estructuras_organizadas_abstract):
    """Implementacion de listas [] del TDA 'Estructuras_organizadas_abstract'. 

    Methods: 
    esta_vacia
    limpiar
    tamanio
    eliminar_min
    eliminar_max
    agregar
    buscar_elemento
    cuantos
    obtener_subcoleccion
    obtener_subcoleccion_rango
    subcoleccion_sin_repeticion
    remplazar
    __eq__
    imprimir_ascendente
    imprimir_descendente
    """

    def __init__(self,lista: List,ordenamiento: Algoritmos_ordenamiento_abstract,busqueda: Algortimos_busqueda_abstract,repeticion: Algoritmos_repeticcion_abstract) -> None:
        # Nota la relacion de composicion entre clases respetando SOLID
        self._lista=lista
        self._ordenamiento=ordenamiento
        self._busqueda=busqueda
        self._repeticion=repeticion

    def esta_vacia(self) -> bool: 
        """Indica si la coleccion tiene o no elementos.    
    
        Returns: 
        bool - Regresa True si no hay elementos en la coleccion, False en otro caso.
        """
        return self.tamanio(self._lista)==0 

    def limpiar(self) -> None: 
        """Elimina todos los elementos de una coleccion."""
        self._lista=[]
    
    def tamanio(self,lista) -> int: # agregamos parametro 'lista' para poder reutilizar metodo  
        """Cuenta los elementos en la coleccion.    

        Args:
        lista: []list - Recibe una lista de numeros reales

        Returns: 
        int - Regresa el numero total de elementos en la coleccion.
        """
        self._lista=lista
        # iniciamos 'size' fuera del ciclo for para que aun si la lista esta vacia no truene (tecnicamente para eso esta el metodo esta_vacia)
        size=0 
        for _ in self._lista: # omitimos variable de control ya que no se ocupa
            size+=1
        return size

    def eliminar_min(self) -> None: 
        """Elimina de una coleccion al elemento mas pequeño (todas las presencias)."""
        self._lista=[i for i in self._ordenamiento.ordenar(self._lista) if i>self._ordenamiento.ordenar(self._lista)[0]]
                        
    def eliminar_max(self) -> None: 
        """Elimina de una coleccion al elemento mas grande (todas las presencias)."""
        self._lista=[i for i in self._ordenamiento.ordenar(self._lista) if i<self._ordenamiento.ordenar(self._lista)[len(self._lista)-1]]

    def agregar(self,elemento_agregado) -> None:    
        """Se agrega un elemento a la coleccion manteniendo el orden.    
        
        Args: 
        elemento_agregado: float - Recibe un numero real
        """
        self._elemento_agregado=elemento_agregado
        self._lista.append(self._elemento_agregado) # agregamos elemento y volvemos a ordenar
        self._lista=self._ordenamiento.ordenar(self._lista)
        
    def buscar_elemento(self,elemento) -> int:
        """Busca un elemento dentro de una coleccion.    
        
        Args: 
        elemento: float - Recibe un elemento de la coleccion (un numero real)

        Returns: 
        int - Devuelve el indice en donde se encuentra la primera presencia de elemento en la coleccion o -1 si no se encuentra
        """
        self._elemento=elemento
        return self._busqueda.buscar_alternativa(self._lista,self._elemento) # busca elemento dentro de la lista
        
    def cuantos(self,elemento) -> int:  
        """Cuenta las veces que aparece un elemento en la coleccion.    
        
        Args: 
        elemento: float - Recibe un elemento de la lista (un numero real)

        Returns: 
        int - Devuelve la cantidad de veces que aparece el elemento en la coleccion.
        """
        self._elemento=elemento
        contador=0 # iniciamos fuera del ciclo for por si el elemento no se encuentra en la lista
        for i in self._lista:
            if i==self._elemento:
                contador+=1 
        return contador 
       
    def obtener_subcoleccion(self,elemento) -> list: 
        """Obtiene una subcoleccion que contiene a los elementos a partir de cierto elemento de la coleccion.    
        
        Args: 
        elemento: float - Recibe el primer elemento de la nueva coleccion (numero real en la lista inicial)

        Returns: 
        list - Regresa la subcoleccion a partir del elemento indicado, o una excepcion si el elemento no se encuentra en la lista inicial

        Raises:
        ValueError: Levanta excepcion si 'elemento' no se encuentra en la lista.

        """
        self._elemento=elemento
        if self._elemento in self._lista:
            return [i for i in self._lista if i >= self._elemento]
        else:
            raise ValueError
    
    def obtener_subcoleccion_rango(self,primer_elemento,segundo_elemento) -> list: 
        """Regresa una subcoleccion que contiene a los elementos entre un rango indicado por dos elementos de la lista.    
        
        Args: 
        primer_elemento: float - Recibe el primer elemento de la subcoleccion (numero real en la lista inicial)
        segundo_elemento: float - Recibe el ultimo elemento de la subcoleccion (numero real en la lista inicial)

        Returns: 
        list - Regresa la subcoleccion desde el primer _elemento hasta el segundo_elemento, o una excepcion si los elementos no se encuentran

        Raise:
        ValueError: Levanta excepcion si alguno de los elementos no se encuentra en la lista.
        """
        self._primer_elemento=primer_elemento
        self._segundo_elemento=segundo_elemento
        if self._primer_elemento in self._lista and self._segundo_elemento in self._lista:
            return [i for i in self._lista if i>=self._primer_elemento and i<=self._segundo_elemento]
        else:
            raise ValueError
        
    def subcoleccion_sin_repeticion(self) -> list: 
        """Elimina de una subcoleccion (de la coleccion original) los elementos repetidos.    

        Returns: 
        list - Regresa la subcoleccion sin elementos repetidos.
        """
        return self._repeticion.eliminar_rep(self._lista) # elimina repetidos de la lista

    def remplazar(self,elemento, nuevo) -> list: 
        """Reemplaza todas las presencias de un elemento por uno nuevo manteniendo el orden.    
        
        Args: 
        elemento: float - Recibe el elemento de la coleccion por reemplazar
        nuevo: float - Recibe el nuevo elemento que reemplazara al otro

        Returns: 
        list - Regresa la lista ordenada con el reemplazo de elementos.
        """
        self._elemento=elemento
        self._nuevo=nuevo
        self._lista=self._ordenamiento.ordenar([self._nuevo if i==self._elemento else i for i in self._lista]) # ordena lista con el remplazo hecho
        return self._lista 
    
    def __eq__(self,otra) -> bool: 
        """Compara dos colecciones.    
        
        Args: 
        otra: []list - Recibe una lista de numeros reales

        Returns:
        bool - Devuelve True si dos colecciones son iguales, es decir si contienen los mismos elementos y la misma cantidad de ellos, False en otro caso.
        """
        self._otra=otra
        if isinstance(self._lista,list) and isinstance(self._otra,list) and self.tamanio(self._lista)==self.tamanio(self._otra): 
        # confirmamos que se trata de listas de la misma longitud
            lista_original=self._ordenamiento.ordenar(self._lista) # ordenamos ambas listas
            lista_otra=self._ordenamiento.ordenar(self._otra)
            for i in lista_otra:
                if lista_otra[i]!=lista_original[i]: 
                    return False    
            return True 

        return False
    
    def imprimir_ascendente(self) -> str: 
        """Imprime los elementos de la coleccion de menor a mayor, sin incluir los none.    

        Returns: 
        str - Regresa los elementos de la coleccion de menor a mayor (sin los none).
        """
        for i in self._ordenamiento.ordenar(self._lista):
            if i!=None:
                print(i)
    
    def imprimir_descendente(self) -> str: 
        """Imprime los elementos de la coleccion de mayor a menor, sin incluir los none.    

        Returns: 
        str - Regresa los elementos de la coleccion de mayor a menor (sin los none).
        """
        for i in range(len(self._lista)-1,0,-1): # recorre indices hacia atras empezando con el ultimo
            if self._ordenamiento.ordenar(self._lista)[i]!=None:
                print(self._ordenamiento.ordenar(self._lista)[i])

class Lista_vacia(Algoritmos_repeticcion_abstract):
    """Algoritmo que utiliza una lista vacia para eliminar repetidos de una coleccion.
    
    Methods:
    eliminar_rep
    """

    def __init__(self) -> None:
        pass

    def eliminar_rep(self,lista) -> list:
        """Elimina elementos repetidos de una coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales

        Returns:
        list - Regresa la lista sin elementos repetidos
        """
        self._lista=lista
        nueva_lista = []
        for elemento in self._lista: 
            if elemento not in nueva_lista:
                nueva_lista.append(elemento)
        return nueva_lista

class Mergesort(Algoritmos_ordenamiento_abstract):
    """Algoritmo de ordenamineto Mergesort (ascendente).
    
    Methods:
    ordenar
    merge_aux
    """

    def __init__(self) -> None:
        pass

    def ordenar(self,lista) -> list:
        """Ordena ascendentemente la coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales

        Returns:
        list - Regresa la lista ordenada
        """
        if(len(lista) <= 1):
            return lista

        indice_medio=len(lista)//2
        izq = [lista[i] for i in range(indice_medio)]
        der = [lista[i] for i in range(indice_medio,len(lista))]
        izq=self.ordenar(izq)
        der=self.ordenar(der)

        return self.merge_aux(izq,der)
 
    def merge_aux(self,izq,der) -> list:
        """Intercala los elementos de las divisiones.   

        Args: 
        izq: []list - Recibe los elementos de la lista lado izquierdo
        der: []list - Recibe los elementos de la lista lado derecho
    
        RETURN : #DESCRIPCION RETURN
        list - Regresa la lista ordenada 
        """
        lista,i,j =[],0,0

        while (i < len(izq) and j < len(der)):
            if (izq[i] <= der[j]):
                lista.append(izq[i])
                i += 1
            else:
                lista.append(der[j])
                j += 1
        while (i < len(izq)):
            lista.append(izq[i])
            i += 1
        while (j < len(der)):
            lista.append(der[j])
            j += 1

        return lista

class Binaria_recursiva(Algortimos_busqueda_abstract):

    def __init__(self) -> None:
        pass

    def buscar_alternativa(self,lista: List, elemento) -> int:
        """Busca elemento dentro de una coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales
        elemento: []float - Recibe un numero real

        Returns:
        int - Regresa el indice de la primera presencia del elemento buscado o -1 si no esta en la coleccion
        """
        self._lista=lista
        self._elemento=elemento
        for i in range(self.buscar(self._lista,self._elemento)): # recorremos hasta el indice la ultima presencia del elemento buscado
            if self._lista[i]==self._elemento:
                return i 
        return self.buscar(self._lista,self._elemento) # si no hay presencia antes, el indice de la ultima presencia es el de la primera presencia

    def buscar(self, lista: List, elemento) -> int:
        """Busca elemento dentro de una coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales
        elemento: []float - Recibe un numero real

        Returns:
        int - Regresa el indice de la ultima presencia del elemento buscado o -1 si no esta en la coleccion
        """
        self._lista=lista
        self._elemento=elemento
        return self.divide(self._lista, self._elemento, 0, len(self._lista)-1)

    def divide(self,lista, elemento, inicio, fin) -> int:
        """Divide la lista para encontrar la posicion central.    

        Args: 
        lista: float[] - Recibe la lista de elementos
        elemento: float[] - Recibe lista temporal de tamaño predeterminado de la lista 
        inicio: float[] - Recibe el elemento inicial de la lista (elementos del lado izquierdo).
        fin: float[] - Recibe el elemento final de la lista (elemetos del lado derecho).
    
        Returns:
        int - Devuelve el elemento correspondiente a la posicion central
        """
        self._lista=lista
        self._elemento=elemento
        self._inicio=inicio
        self._fin=fin
        indice_medio = (self._inicio + self._fin) // 2
        
        if self._lista[indice_medio] == self._elemento:
            return indice_medio
        
        if self._inicio > self._fin:
            return -1
        
        if self._elemento < self._lista[indice_medio]:
            return self.divide(self._lista, self._elemento, self._inicio, indice_medio-1)
        
        else:
            return self.divide(self._lista, self._elemento, indice_medio+1,self._fin)
