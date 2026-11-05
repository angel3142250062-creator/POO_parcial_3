from conexionBD import conexion, cursor
class Estudiantes:
    def __init__(self, nombre="", nota=""):
        self._nombre = nombre
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def insertar(self):
        try:
            sql = "INSERT INTO estudiantes (nombre, nota) VALUES (%s, %s)"
            valores = (self.nombre, self.nota)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except:
            print(f"\nError al insertar ")
            return False

    @staticmethod
    def consultar():
        try:
            sql = "SELECT id, nombre, nota FROM estudiantes"
            cursor.execute(sql)
            registros = cursor.fetchall()
            return registros
        except:
            print(f"\nError al consultar")
            return []

    def actualizar(self, id_estudiante):
        try:
            sql = "UPDATE estudiantes SET nombre = %s, nota = %s WHERE id = %s"
            valores = (self.nombre, self.nota, id_estudiante)
            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount > 0  
        except :
            print(f"\nError al actualizar")
            return False

    @staticmethod
    def eliminar(id_estudiante):
        try:
            sql = "DELETE FROM estudiantes WHERE id = %s"
            cursor.execute(sql, (id_estudiante,))
            conexion.commit()
            return cursor.rowcount > 0  
        except:
            print(f"\nError al eliminar")
            return False