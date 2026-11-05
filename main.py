from tkinter import Tk, Label, Entry, Button, messagebox
from coches import coches
from camiones import camiones

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)
        self.main()
    
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text=":::MENU PRINCIPAL:::").pack(pady=20)
        Button(self.ventana, text="1- Coches", command=self.menu_acciones).pack(padx=10, pady=5)
        Button(self.ventana, text="2- Salir", command=self.ventana.quit).pack(padx=10, pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Coche"
        Label(self.ventana, text=f"...:::Menu de {tipo}:::...").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_coche_view).pack(pady=5)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_coche_view).pack(pady=5)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_coche_view).pack(pady=5)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_coche_view).pack(pady=5)
        Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=5)

    def insertar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese los datos del coche...").pack(pady=10)
        
        Label(self.ventana, text="Marca: ").pack(pady=2)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=2)
        
        Label(self.ventana, text="Color: ").pack(pady=2)
        self.color = Entry(self.ventana)
        self.color.pack(pady=2)
        
        Label(self.ventana, text="Modelo: ").pack(pady=2)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=2)
        
        Label(self.ventana, text="Velocidad: ").pack(pady=2)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=2)
        
        Label(self.ventana, text="Potencia: ").pack(pady=2)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=2)
        
        Label(self.ventana, text="# de Asientos: ").pack(pady=2)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=2)

        Button(self.ventana, text="Agregar", command=self.insertar_coche_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def eliminar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar el ID del coche que deseas borrar:").pack(pady=10)
        self.idBorrar = Entry(self.ventana)
        self.idBorrar.focus()
        self.idBorrar.pack(pady=5)

        Button(self.ventana, text="Borrar", command=self.eliminar_coche_controller).pack(pady=5)
        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=5)

    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::: Consultar Coches :::...").pack(pady=10)
        filas = self.consultar_coche_controller()
        Label(self.ventana, text=filas, justify="left").pack(pady=5)
        Button(self.ventana, text="::Regresar::", command=self.menu_acciones).pack(pady=10)

    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese el ID y los nuevos datos...").pack(pady=5)
                
        Label(self.ventana, text="ID a Modificar: ").pack(pady=2)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=2)
                
        Label(self.ventana, text="Marca: ").pack(pady=2)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady=2)
                
        Label(self.ventana, text="Color: ").pack(pady=2)
        self.color = Entry(self.ventana)
        self.color.pack(pady=2)
                
        Label(self.ventana, text="Modelo: ").pack(pady=2)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=2)
                
        Label(self.ventana, text="Velocidad: ").pack(pady=2)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=2)
                
        Label(self.ventana, text="Potencia: ").pack(pady=2)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=2)
                
        Label(self.ventana, text="# de Asientos: ").pack(pady=2)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=2)

        Button(self.ventana, text="Modificar", command=self.modificar_coche_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::", message="...¡Acción Realizada con Éxito!...")
        else:
            messagebox.showerror(title=":: Error ::", message="...¡Esta Acción no pudo realizarse!...")

    def insertar_coche_controller(self):
        coches1 = coches.Coches(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        respuesta = coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1

    def eliminar_coche_controller(self):
        id_coche = self.idBorrar.get()
        respuesta = coches.Coches.eliminar(id_coche)
        self.respuesta_sql(respuesta)

    def consultar_coche_controller(self):
        registro = coches.Coches.consultar()
        filas = ""
        if len(registro) > 0:
            for num, fila in enumerate(registro, 1):
                filas += f"Coche #{num} | ID: {fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo: {fila[3]} | Vel: {fila[4]} | Pot: {fila[5]} | Asientos: {fila[6]}\n"
        else:
            filas = "...¡No se encontró información en la BD!..."
        return filas

    def modificar_coche_controller(self):
        id_coche = self.id.get()
        coches1 = coches.Coches(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        respuesta = coches1.actualizar(id_coche)
        self.respuesta_sql(respuesta)
        del coches1

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()