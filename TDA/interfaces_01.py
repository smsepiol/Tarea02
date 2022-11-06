# TAREA 02
# INTERFACES DEL EJERCICIO 01

from abc import ABC, abstractmethod
from typing import List

class Estructuras_organizadas_abstract(ABC):
    """Coleccion de datos organizados (TDA). 

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

    def __init__(self) -> None:
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Indica si la coleccion tiene o no elementos.    
    
        Returns:
        bool - Regresa True si no hay elementos en la coleccion, False en otro caso. #####################################################################
        """
        pass

    @abstractmethod
    def limpiar(self) -> None:
        """Elimina todos los elementos de una coleccion."""
        pass
    
    @abstractmethod
    def tamanio(self) -> int:
        """Calcula el tamanio de una coleccion.    

        Returns:
        int - Regresa el numero total de elementos en la coleccion.
        """
        pass

    @abstractmethod
    def eliminar_min(self) -> None:
        """Elimina de una coleccion al elemento mas pequeño (todas las presencias)."""
        pass
    
    @abstractmethod
    def eliminar_max(self) -> None:
        """Elimina de una coleccion al elemento mas grande (todas las presencias)."""
        pass
    
    @abstractmethod
    def agregar(self,elemento_agregado) -> None:
        """Se agrega un elemento a la coleccion manteniendo el orden.    
        
        Args: 
        elemento_agregado: float - Recibe un numero real
        """
        pass
    
    @abstractmethod
    def buscar_elemento(self,elemento) -> int:
        """Busca un elemento dentro de una coleccion.    
        
        Args: 
        elemento: float - Recibe un elemento de la coleccion (un numero real)

        Returns:
        int - Decuelve el indice en donde se encuentra la primera presencia de elemento en la coleccion o -1 si no se encuentra
        """
        pass
    
    @abstractmethod
    def cuantos(self,elemento) -> int:
        """Cuenta las veces que aparece un elemento en la coleccion.    
        
        Args: 
        elemento: float - Recibe un elemento de la lista (un numero real)

        Returns:
        int - Devuelve la cantidad de veces que aparece el elemento en la coleccion.
        """
        pass

    @abstractmethod
    def obtener_subcoleccion(self,elemento) -> list:
        """Obtiene una subcoleccion que contiene a los elementos a partir de cierto elemento de la coleccion.    
        
        Args: 
        elemento: float - Recibe el primer elemento de la nueva coleccion (numero real en la lista inicial)

        Returns:
        list - Regresa la subcoleccion a partir del elemento indicado, o una excepcion si el elemento no se encuentra en la lista inicial
        """
        pass
    
    @abstractmethod
    def obtener_subcoleccion_rango(self,primer_elemento,segundo_elemento) -> list:
        """Obtiene una subcoleccion que contiene a los elementos entre un rango indicado por dos elementos de la lista.    
        
        Args: 
        primer_elemento: float - Recibe el primer elemento de la subcoleccion (numero real en la lista inicial)
        segundo_elemento: float - Recibe el ultimo elemento de la subcoleccion (numero real en la lista inicial)

        Returns:
        list - Regresa la subcoleccion desde el primer _elemento hasta el segundo_elemento, o una excepcion si los elementos no se encuentran
        """
        pass

    @abstractmethod
    def subcoleccion_sin_repeticion(self) -> list:
        """Obtiene una subcoleccion (de la coleccion original) sin los elementos repetidos.    

        Returns:
        list - Regresa la subcoleccion sin elementos repetidos.
        """
        pass
    
    @abstractmethod
    def remplazar(self,elemento,nuevo) -> list:
        """Reemplaza todas las presencias de un elemento por uno nuevo manteniendo el orden.    
        
        Args: 
        elemento: float - Recibe el elemento de la coleccion por reemplazar
        nuevo: float - Recibe el nuevo elemento que reemplazara al otro

        Returns:
        list - Regresa la lista ordenada con el reemplazo de elementos.
        """
        pass

    @abstractmethod
    def __eq__(self,otra) -> bool:
        """Compara dos colecciones y regresa si son iguales.    
        
        Args: 
        otra: []list - Recibe una lista de numeros reales

        Returns:
        bool - Devuelve True si dos colecciones son iguales, es decir si contienen los mismos elementos, y False en otro caso.
        """
        pass
    
    @abstractmethod
    def imprimir_ascendente(self) -> str:
        """Imprime los elementos de la coleccion de menor a mayor, sin incluir los none.    

        Returns:
        str - Regresa los elementos de la coleccion de menor a mayor (sin los none).
        """
        pass
    
    @abstractmethod
    def imprimir_descendente(self) -> str:
        """Imprime los elementos de la coleccion de mayor a menor, sin incluir los none.    

        Returns:
        str - Regresa los elementos de la coleccion de mayor a menor (sin los none).
        """
        pass

class Algoritmos_ordenamiento_abstract(ABC):
    """Algoritmos que ordenan ascendentemente una coleccion.
    
    Methods:
    ordenar
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def ordenar(self,lista:List) -> list:
        """Ordena ascendentemente la coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales

        Returns:
        list - Regresa la lista ordenada
        """
        pass

class Algoritmos_repeticcion_abstract(ABC):
    """Algoritmos que eliminan elementos repetidos de una coleccion.

    Methods:
    eliminar_rep
    """

    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def eliminar_rep(self,lista:List) -> list:
        """Elimina elementos repetidos de una coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales

        Returns:
        list - Regresa la lista sin elementos repetidos
        """
        pass

class Algortimos_busqueda_abstract(ABC):
    """Algoritmos que buscan un elemento dentro de una coleccion.
    
    Methods:
    buscar
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def buscar(self,lista:List,elemento) -> int:
        """Busca elemento dentro de una coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales
        elemento: []float - Recibe un numero real

        Returns:
        int - Regresa el indice de la ultima presencia del elemento buscado o -1 si no esta en la coleccion
        """
        pass

    @abstractmethod
    def buscar_alternativa(self,lista:List,elemento) -> int:
        """Busca elemento dentro de una coleccion.
        
        Args:
        lista: []list - Recibe una lista de numeros reales
        elemento: []float - Recibe un numero real

        Returns:
        int - Regresa el indice de la primera presencia del elemento buscado o -1 si no esta en la coleccion
        """
        pass

