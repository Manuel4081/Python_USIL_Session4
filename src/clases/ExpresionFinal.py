from .ExpresionIngreso import ExpresionIngreso


class ExpresionFinal(ExpresionIngreso):
    def ArchivosDiccionario(self):
        return str(self.Diccionario)

    def ArchivosLista(self):
        return str(self.Lista)

    def ArchivosDuplicado(self):
        return self.ExpresionFinal

    def CantDuplicados(self):
        return str(self.max)
