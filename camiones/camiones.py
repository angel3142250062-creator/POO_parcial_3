from coches import coches
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexionBD import conexion, cursor
class Camiones(coches.Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self._eje = eje
        self._capacidadCarga  = capacidadCarga
        
    @property
    def eje(self):
        return self._eje
    @eje.setter
    def eje(self,eje):
        self._eje =eje
    @property
    def capacidadCarga(self):
        return self._eje
    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self._capacidadCarga =capacidadCarga
    
    def insertar (self):
        try:
            cursor.execute("insert into camiones values (null,%s,%s,%s,%s,%s,%s,%s,%s)",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,self._eje,self._capacidadCarga))
            conexion.commit()
            return True
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False
    @staticmethod
    def consultar():
        try: 
            cursor.execute("select * from camiones")
            
            return cursor.fetchall()
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return []
    staticmethod
    def eliminar(id):
        try: 
            cursor.execute("delete from camiones where id=%s",(id,))
            conexion.commit()
            return True
        except: 
            return False 
    def actualizar(self,id):
        try:
            cursor.execute("update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s, eje=%s, capacidadCarga=%s where id=%s",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,self._eje,self._capacidadCarga,id))

            conexion.commit()
            return True 
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return False