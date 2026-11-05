from Proyecto_estudiantes.coches_system.coches.cochesBD import CochesBD
from tkinter import Tk,Label,Entry,Button,messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        App.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    
    def menu_acciones(tipo):
        print(f"\n\t Menu de {tipo}\n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\n\t Elige una opción: ").strip().lower()
        return opcion


    def respuesta_sql(respuesta):
        if respuesta:
            input("\n\t ...ACCION EXITOSA...")
        else:
            input("\n\t ...Esta acción no se puede realizar en este momento...")

    
    def datos_coches(tipo):
        App.borrarPantalla()
        print(f"\n\t\tIngresar datos del tipo: {tipo}")
        cochesitos = {}
        cochesitos['marca'] = input(f"\n\tNombre: ").upper().strip()
        cochesitos['color'] = input(f"\tColor: ").upper().strip()
        cochesitos['modelo'] = input(f"\tModelo: ").upper().strip()
        cochesitos['velocidad'] = int(input(f"\tVelocidad: ").strip())
        cochesitos['potencia'] = int(input(f"\tPotencia: ").strip())
        cochesitos['asientos'] = int(input(f"\tNúmero de asientos: ").strip())
        return cochesitos

    def menu_coche():
        opcion = True
        while opcion:
            App.borrarPantalla()
            opcion = App.menu_acciones("Coches")
            match opcion:
                case '1':
                    App.borrarPantalla()
                    cochesitos = App.datos_coches("Coche")
                    coche1 = CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.insertar()
                    App.respuesta_sql(respuesta)
                    
                case '2':
                    App.borrarPantalla()
                    id = input("\n\tIngresa el ID del coche a eliminar: ").strip()
                    respuesta = CochesBD.eliminar(id)
                    App.respuesta_sql(respuesta)
                    
                case '3':
                    App.borrarPantalla()
                    id = input("Ingresa el ID del coche a actualizar: ").strip()
                    cochesitos = App.datos_coches("Coche")
                    coche1 = CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.actualizar(id)
                    App.respuesta_sql(respuesta)
                    
                case '4':
                    App.borrarPantalla()
                    registros = CochesBD.consultar()
                    if len(registros) > 0:
                        num_coches =+1
                        for fila in registros:
                            print(f"\n\tCoche # {num_coches}\n\t ID: {fila[0]}\n\t Marca: {fila[1]} \n\t Color: {fila[2]} \n\t Modelo: {fila[3]} \n\t Velocidad: {fila[4]} \n\t Potencia: {fila[5]} \n\t # Asientos: {fila[6]}")
                            num_coches += 1
                        App.espereTecla()
                    else:
                        print("\n\n\tNo existen datos que mostrar por el momento")
                        App.espereTecla()
                        
                case '5':
                    opcion = False
                case _:
                    input("\n\n\t...Opción Inválida... Ingrese de nuevo porfis")

    def menu_camion():
        opcion = True
        while opcion:
            App.borrarPantalla()
            opcion = App.menu_acciones("Camiones")
            match opcion:
                case '1':
                    cochesitos = App.datos_coches("Camión")
                    coche1 = CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.insertar()
                    App.respuesta_sql(respuesta)
                case '2':
                    App.borrarPantalla()
                    id = input("\n\tIngresa el ID del camión a eliminar: ").strip()
                    respuesta = CochesBD.eliminar(id)
                    App.respuesta_sql(respuesta)
                case '3':
                    App.borrarPantalla()
                    id = input("Ingresa el ID del camión a actualizar: ").strip()
                    cochesitos = App.datos_coches("Camión")
                    coche1 = CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.actualizar(id)
                    App.respuesta_sql(respuesta)
                case '4':
                    App.borrarPantalla()
                    registros = CochesBD.consultar()
                    if len(registros) > 0:
                        num_coches+1
                        for fila in registros:
                            print(f"\n\t\tCamión # {num_coches}\n\t ID: {fila[0]}\n\t Marca: {fila[1]} \n\t Color: {fila[2]} \n\t Modelo: {fila[3]} \n\t Velocidad: {fila[4]} \n\t Potencia: {fila[5]} \n\t Asientos: {fila[6]}")
                            num_coches += 1
                        App.espereTecla()
                    else:
                        print("\n\n\tNo existen datos que mostrar por el momento")
                        App.espereTecla()
                case '5':
                    opcion = False
                case _:
                    input("\n\n\t...Opción Inválida... Ingrese de nuevo porfis")


    def menu_camioneta():
        opcion = True
        while opcion:
            App.borrarPantalla()
            opcion = App.menu_acciones("Camioneta")
            match opcion:
                case '1':
                    cochesitos = App.datos_coches("Camioneta")
                    coche1 = CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.insertar()
                    App.respuesta_sql(respuesta)
                case '2':
                    App.borrarPantalla()
                    id = input("\n\tIngresa el ID del camión a eliminar: ").strip()
                    respuesta = CochesBD.eliminar(id)
                    App.respuesta_sql(respuesta)
                case '3':
                    App.borrarPantalla()
                    id = input("Ingresa el ID del camión a actualizar: ").strip()
                    cochesitos = App.datos_coches("Camión")
                    coche1 = CochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                    respuesta = coche1.actualizar(id)
                    App.respuesta_sql(respuesta)
                case '4':
                    App.borrarPantalla()
                    registros = CochesBD.consultar()
                    if len(registros) > 0:
                        num_coches+1
                        for fila in registros:
                            print(f"\n\t\tCamión # {num_coches}\n\t ID: {fila[0]}\n\t Marca: {fila[1]} \n\t Color: {fila[2]} \n\t Modelo: {fila[3]} \n\t Velocidad: {fila[4]} \n\t Potencia: {fila[5]} \n\t Asientos: {fila[6]}")
                            num_coches += 1
                        App.espereTecla()
                    else:
                        print("\n\n\tNo existen datos que mostrar por el momento")
                        App.espereTecla()
                case '5':
                    opcion = False
                case _:
                    input("\n\n\t...Opción Inválida... Ingrese de nuevo porfis")






    @staticmethod
    def main():
        opcion = True
        while opcion:
            App.borrarPantalla()
            opcion = input("\n\t\t\t...::: MENU PRINCIPAL :::... \n\n \t 1.- Coches \n\t 2.- Camiones \n\t 3.- Camionetas \n\t 4.- Salir \n\n\t Elige una opción: ").strip().lower()
            match opcion:
                case '1':
                    App.menu_coche()
                case '2':
                    App.menu_camion() 
                case '3':
                    App.menu_camioneta() 
                case '4':
                    App.borrarPantalla()
                    print("\n\t Salir del Sistema")
                    opcion = False
                case _:
                    input("\n\t...Opción Inválida... Ingrese de nuevo porfis")

if __name__ == "__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
