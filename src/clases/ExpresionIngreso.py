class ExpresionIngreso:
    def __init__(self, Expresion):
        self.Lista = Expresion.split()
        self.Diccionario = {}
        self.max = 0
        self.min = len(self.Lista)
        self.ExpresionFinal = ""

    def Procesar(self):
        for limite in self.Lista:
            self.Diccionario[limite] = self.Lista.count(limite)
            Numero = self.Lista.count(limite)
            if (Numero > self.max):
                self.max = Numero
                self.ExpresionFinal = limite
            elif (Numero < self.min):
                self.min = Numero
