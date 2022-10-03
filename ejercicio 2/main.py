from arbol import Arbol

if __name__ == "__main__":
    unArbol = Arbol()
    '''
    num = input("\nIngrese un elemento al arbol:")
    while num != "salir":
        unArbol.Insertar(unArbol.getRaiz(),int(num))
        num = input("\nIngrese otro elemento al arbol, 'salir' para finalizar:")
    unArbol.Inorder(unArbol.getRaiz())
    '''
    unArbol.Insertar(unArbol.getRaiz(),5)
    unArbol.Insertar(unArbol.getRaiz(),7)
    unArbol.Insertar(unArbol.getRaiz(),8)
    unArbol.Insertar(unArbol.getRaiz(),6)
    unArbol.Insertar(unArbol.getRaiz(),3)
    unArbol.Insertar(unArbol.getRaiz(),2)
    unArbol.Insertar(unArbol.getRaiz(),4)
    unArbol.Insertar(unArbol.getRaiz(),1)
    unArbol.Insertar(unArbol.getRaiz(),10)

    unArbol.Nodoterminal(unArbol.getRaiz())