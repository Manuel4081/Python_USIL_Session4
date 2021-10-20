from src.clases.ExpresionFinal import ExpresionFinal


def test_archivos_diccionario():
    expdic = ExpresionFinal(
        'hola a todos, tenemos luz verde para el trabajo, hola, trabajo, verde, trabajo')

    assert expdic.ArchivosDiccionario()


def test_archivos_lista():
    expdic2 = ExpresionFinal(
        'hola a todos, tenemos luz verde para el trabajo, hola, trabajo, verde, trabajo')

    assert expdic2.ArchivosLista()


def test_archivos_duplicado():
    expdic3 = ExpresionFinal(
        'hola a todos, tenemos luz verde para el trabajo, hola, trabajo, verde, trabajo')

    assert expdic3.ArchivosDuplicado()


def test_cant_duplicados():
    expdic4 = ExpresionFinal(
        'hola a todos, tenemos luz verde para el trabajo, hola, trabajo, verde, trabajo')

    assert expdic4.CantDuplicados()
