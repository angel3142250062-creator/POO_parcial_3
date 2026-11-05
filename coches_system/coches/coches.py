class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._asientos=asientos
    def acelerar(self):
        self._velocidad+=1
        print(f"La velocidad ahora es: {self._velocidad}")
    def frenar(self):
        self._velocidad-=1
        print(f"La velocidad ahora es: {self._velocidad}")
############################################################################
    def getMarca(self):
        return self._marca
    def setMarca(self,marca):
        self._marca=marca

    def getVelocidad(self):
        return self._velocidad
    def setVelocidad(self,velocidad):
        self._velocidad=velocidad

    def getColor(self):
        return self._color
    def setColor(self,color):
        self._color=color
        
    def getModelo(self):
        return self._modelo
    def setModelo(self,modelo):
        self._modelo=modelo
        
    def getPotencia(self):
        return self._potencia
    def setPotencia(self,potencia):
        self._potencia=potencia
        
    def getAsientos(self):
        return self._asientos
    def setAsientos(self,asientos):
        self._asientos=asientos

