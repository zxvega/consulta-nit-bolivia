from consultanitbolivia import ConsultaNIT

consulta = ConsultaNIT()
resultado = consulta.verificar_contribuyente("1003579028")

if resultado is not None:
    # Procesar el resultado de acuerdo a tus necesidades
    # ...
    print(resultado)