import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexionBD import conexion, cursor
class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos ):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos  = asientos    
    
    def acelerar(self):
        self._velocidad+=1
    def frenar(self):
        self._velocidad-=1
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad  
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca= marca
    @property    
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color= color
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo= modelo    
    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self,potencia):
        self._potencia = potencia
    @property 
    def asientos(self):
        return self._asientos
    @asientos.setter
    def asientos(self,asientos):
        self._asientos = asientos
        
    def insertar (self):
        try:
            cursor.execute("insert into coches values (null,%s,%s,%s,%s,%s,%s)",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos))
            conexion.commit()
            return True
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False
    @staticmethod
    def consultar():
        try: 
            cursor.execute("select * from coches")
            
            return cursor.fetchall()
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return []
    staticmethod
    def eliminar(id):
        try: 
            cursor.execute("delete from coches where id=%s",(id,))
            conexion.commit()
            return True
        except: 
            return False 
    def actualizar(self,id):
        try:

            cursor.execute("update coches set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s where id=%s",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,id))

            conexion.commit()
            return True 
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return False


