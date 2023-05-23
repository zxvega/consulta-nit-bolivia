import requests

class ConsultaNIT:
    def verificar_contribuyente(self, nit):
        # URL del endpoint con el parámetro nit
        url = f"https://pbdw.impuestos.gob.bo:8080/gob.sin.padron.servicio.web/consulta/verificarContribuyente?nit={nit}"

        try:
            # Realizar la petición GET
            response = requests.get(url)

            # Verificar si la petición fue exitosa (código de estado 200)
            if response.status_code == 200:
                # Obtener los datos de la respuesta en formato JSON
                data = response.json()
                # Retornar la respuesta
                return data
            else:
                # Retornar None en caso de una respuesta no exitosa
                print("La petición GET no fue exitosa. Código de estado:", response.status_code)
                return None

        except requests.exceptions.RequestException as e:
            # Manejar errores de conexión u otros errores de la petición
            print("Error en la petición GET:", e)
            return None