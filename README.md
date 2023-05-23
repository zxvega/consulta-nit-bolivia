# Consultas del Estado del NIT - Bolivia

[![PyPI version][pypi-version]][pypi]

El sitio oficial de Impuestos Nacionales de Bolivia a traves de su Oficina Virtual pone a disposicion como Servicio al Ciudadano un sitio web para Consultas del Estado del NIT.

Sitio Web: https://pbdw.impuestos.gob.bo:8080/gob.sin.padron.web/#/verificar/estadoContribuyente

Este paquete le permite realizar la misma verificacion haciendo uso de los mismos servicios con el fin de poder integrar dicha verificacion en sus desarrollo; por ejemplo validando el NIT en el formulario de registro de una persona juridica.


## Ejemplo

```python

from consultanit import ConsultaNIT

consulta = ConsultaNIT()
resultado = consulta.verificar_contribuyente("1003579028")

if resultado is not None:
    # Procesar el resultado de acuerdo a tus necesidades
    # ...
    print(resultado)

```

## Salida de Ejemplo NIT Existente

```json
{"ok":true,"mensajes":[],"nit":1003579028,"razonSocial":"SERVICIO DE IMPUESTOS NACIONALES","estado":"ACTIVO","fechaUltimoEstado":"12/05/2015"}
```

## Salida de Ejemplo NIT Inexistente
```json
{"ok":false,"mensajes":[{"codigo":null,"descripcion":"NIT Inexistente","tipo":"ERROR"}],"nit":null,"razonSocial":null,"estado":null,"fechaUltimoEstado":null}
```

## Disclaimer

El paquete funcionara siempre y cuando Impuestos Nacionales siga permitiendo que el servicio sea de acceso publico y sin autenticacion.


[pypi-version]: https://img.shields.io/pypi/v/consulta-nit-bolivia
[pypi]: https://pypi.org/project/consulta-nit-bolivia