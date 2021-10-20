from src.clases.ExpresionFinal import ExpresionFinal

expresion = input("Ingresé expresion ha revisar: ")

Ingreso = ExpresionFinal(expresion)
Ingreso.Procesar()

print("Lista: " + Ingreso.ArchivosLista() + "\n")
print("Expresion Repetida:" + Ingreso.ArchivosDuplicado() + "\n")
print("Diccionario: " + Ingreso.ArchivosDiccionario() + "\n")
print("Cantidad Repeticiones: " + Ingreso.CantDuplicados() + "\n")
