from graphviz import Digraph

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if nodo is None:
                return NodoArbol(valor)
            elif valor < nodo.valor:
                nodo.izquierdo = _insertar(nodo.izquierdo, valor)
            else:
                nodo.derecho = _insertar(nodo.derecho, valor)
            return nodo
        
        if self.esVacio():
            self.raiz = NodoArbol(valor)
        else:
            _insertar(self.raiz, valor)

    def mostrarArbol(self, nodo=None, nivel=0):
        if nodo is not None:
            self.mostrarArbol(nodo.derecho, nivel + 1)
            print("    " * nivel + str(nodo.valor))
            self.mostrarArbol(nodo.izquierdo, nivel + 1)

    def graficarArbol(self):
        dot = Digraph()
        def _graficar(nodo):
            if nodo is not None:
                dot.node(str(nodo.valor))
                if nodo.izquierdo:
                    dot.edge(str(nodo.valor), str(nodo.izquierdo.valor))
                    _graficar(nodo.izquierdo)
                if nodo.derecho:
                    dot.edge(str(nodo.valor), str(nodo.derecho.valor))
                    _graficar(nodo.derecho)

        _graficar(self.raiz)
        dot.render('arbol_binario', format='png', view=True)

    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None or nodo.valor == valor:
                return nodo
            elif valor < nodo.valor:
                return _buscar(nodo.izquierdo, valor)
            else:
                return _buscar(nodo.derecho, valor)
        return _buscar(self.raiz, valor)

    def preOrden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preOrden(nodo.izquierdo)
            self.preOrden(nodo.derecho)

    def inOrden(self, nodo):
        if nodo:
            self.inOrden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inOrden(nodo.derecho)

    def postOrden(self, nodo):
        if nodo:
            self.postOrden(nodo.izquierdo)
            self.postOrden(nodo.derecho)
            print(nodo.valor, end=" ")

    def eliminar(self, valor, modo="sucesor"):
        def _minimo(nodo):
            while nodo.izquierdo is not None:
                nodo = nodo.izquierdo
            return nodo
        
        def _maximo(nodo):
            while nodo.derecho is not None:
                nodo = nodo.derecho
            return nodo

        def _eliminar(nodo, valor, modo):
            if nodo is None:
                return nodo
            if valor < nodo.valor:
                nodo.izquierdo = _eliminar(nodo.izquierdo, valor, modo)
            elif valor > nodo.valor:
                nodo.derecho = _eliminar(nodo.derecho, valor, modo)
            else:
                if nodo.izquierdo is None:
                    return nodo.derecho
                elif nodo.derecho is None:
                    return nodo.izquierdo
                
                if modo == "sucesor":
                    temp = _minimo(nodo.derecho)
                else:
                    temp = _maximo(nodo.izquierdo)

                nodo.valor = temp.valor
                if modo == "sucesor":
                    nodo.derecho = _eliminar(nodo.derecho, temp.valor, modo)
                else:
                    nodo.izquierdo = _eliminar(nodo.izquierdo, temp.valor, modo)
            
            return nodo

        self.raiz = _eliminar(self.raiz, valor, modo)

    def recorrerPorNiveles(self):
        if self.esVacio():
            return
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(nodo.valor, end=" ")
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

    def altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

    def contarHojas(self, nodo):
        if nodo is None:
            return 0
        elif nodo.izquierdo is None and nodo.derecho is None:
            return 1
        else:
            return self.contarHojas(nodo.izquierdo) + self.contarHojas(nodo.derecho)

    def contarNodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contarNodos(nodo.izquierdo) + self.contarNodos(nodo.derecho)

    def esArbolBinarioCompleto(self):
        if self.esVacio():
            return True
        cola = [self.raiz]
        vacio_encontrado = False
        while cola:
            nodo = cola.pop(0)
            if nodo is None:
                vacio_encontrado = True
            else:
                if vacio_encontrado:
                    return False
                cola.append(nodo.izquierdo)
                cola.append(nodo.derecho)
        return True

    def esArbolBinarioLleno(self, nodo):
        if nodo is None:
            return True
        if nodo.izquierdo is None and nodo.derecho is None:
            return True
        if nodo.izquierdo is not None and nodo.derecho is not None:
            return self.esArbolBinarioLleno(nodo.izquierdo) and self.esArbolBinarioLleno(nodo.derecho)
        return False

    def eliminarArbol(self):
        def _eliminarNodos(nodo):
            if nodo:
                _eliminarNodos(nodo.izquierdo)
                _eliminarNodos(nodo.derecho)
                nodo.izquierdo = None
                nodo.derecho = None

        _eliminarNodos(self.raiz)
        self.raiz = None

def menu():
    arbol = ArbolBinario()
    while True:
        print("\n--- Menú de Árbol Binario ---")
        print("[0] Salir")
        print("[1] Insertar elemento")
        print("[2] Mostrar árbol completo")
        print("[3] Graficar árbol completo")
        print("[4] Buscar un elemento en el árbol")
        print("[5] Recorrer el árbol en PreOrden")
        print("[6] Recorrer el árbol en InOrden")
        print("[7] Recorrer el árbol en PostOrden")
        print("[8] Eliminar un nodo del árbol (Predecesor)")
        print("[9] Eliminar un nodo del árbol (Sucesor)")
        print("[10] Recorrer el árbol por niveles")
        print("[11] Altura del árbol")
        print("[12] Cantidad de hojas del árbol")
        print("[13] Cantidad de nodos del árbol")
        print("[15] Revisa si es un árbol binario completo")
        print("[16] Revisa si es un árbol binario lleno")
        print("[17] Eliminar el árbol")

        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion == "1":
            valor = int(input("Ingresa el valor a insertar: "))
            arbol.insertar(valor)
        elif opcion == "2":
            print("Árbol completo:")
            arbol.mostrarArbol(arbol.raiz)
        elif opcion == "3":
            arbol.graficarArbol()
        elif opcion == "4":
            valor = int(input("Ingresa el valor a buscar: "))
            nodo = arbol.buscar(valor)
            print("Elemento encontrado" if nodo else "Elemento no encontrado")
        elif opcion == "5":
            print("Recorrido PreOrden:")
            arbol.preOrden(arbol.raiz)
            print()
        elif opcion == "6":
            print("Recorrido InOrden:")
            arbol.inOrden(arbol.raiz)
            print()
        elif opcion == "7":
            print("Recorrido PostOrden:")
            arbol.postOrden(arbol.raiz)
            print()
        elif opcion == "8":
            valor = int(input("Ingresa el valor a eliminar: "))
            arbol.eliminar(valor, modo="predecesor")
            print(f"Nodo {valor} eliminado usando predecesor.")
        elif opcion == "9":
            valor = int(input("Ingresa el valor a eliminar: "))
            arbol.eliminar(valor, modo="sucesor")
            print(f"Nodo {valor} eliminado usando sucesor.")
        elif opcion == "10":
            print("Recorrido por niveles:")
            arbol.recorrerPorNiveles()
            print()
        elif opcion == "11":
            print("Altura del árbol:", arbol.altura(arbol.raiz))
        elif opcion == "12":
            print("Cantidad de hojas:", arbol.contarHojas(arbol.raiz))
        elif opcion == "13":
            print("Cantidad de nodos:", arbol.contarNodos(arbol.raiz))
        elif opcion == "15":
            print("El árbol es binario completo." if arbol.esArbolBinarioCompleto() else "El árbol no es binario completo.")
        elif opcion == "16":
            print("El árbol es binario lleno." if arbol.esArbolBinarioLleno(arbol.raiz) else "El árbol no es binario lleno.")
        elif opcion == "17":
            arbol.eliminarArbol()
            print("El árbol ha sido eliminado.")
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()
