# Crea un programa en Python que mantenga un historial de 
# tareas pendientes. El programa debe permitir al usuario 
# agregar una tarea al inicio de la lista, eliminar una tarea 
# del final de la lista y 
# mostrar todas las tareas en la lista en orden inverso al
# que se agregaron. Además, el programa debe contar la cantidad 
# total de tareas en la lista y mostrar ese número al usuario

import listaSimple

def historialTareas():
    historialTareas = listaSimple.ListaEnlazada()
    def menu():
        print('''
        ............. Historial de tareas ...........
        [1]: Agregar tarea 
        [2]: Eliminar tarea
        [3]: Mostrar tarea
        [4]: Salir
        ''')
        val = input('Opcion: -> ')
        return val

    def agregarTarea(tarea):
        historialTareas.agregarInicio(tarea)

    def eliminarTarea(tarea):
        historialTareas.eliminar(tarea)
    
    def mostrarTareas():
        cont = 0
        cadena = ''
        lista = historialTareas
        actual = lista.primero

        while actual != None:
            cadena +=  f'Tarea {cont + 1}: {actual.dato}'
            cadena += '\n'
            actual = actual.siguiente
            cont += 1
        if cont == 0:
            cadena += 'No hay tareas para mostrar'

        return cadena

    # +++++++++++++++++++ Programa principal +++++++++++++++++++

    ultTarea = ''
    while True:
        val = menu()
        if val == '1':
            tarea = input("Ingrese una tarea: ")
            agregarTarea(tarea)
            ultTarea = tarea

        elif val == '2':
            eliminarTarea(ultTarea)

        elif val == '3':
            cadena = mostrarTareas()
            print(cadena)

        elif val == '4':
            break

        else:
            print('Ingrese una opción válida')
            pass

if __name__ == "__main__":
    historialTareas()
