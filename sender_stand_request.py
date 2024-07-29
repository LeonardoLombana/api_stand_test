import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección url completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())



def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         # Concatenación de URL base y ruta.
                         json=products_ids,  # Datos a enviar en la solicitud.
                         headers=data.headers)  # Encabezados de solicitud.


response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())  # Muestra del resultado en la consola


