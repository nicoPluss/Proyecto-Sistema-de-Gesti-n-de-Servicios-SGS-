import socket
import json

# Definir puerto del servidor
PORT = 5000

# Crear socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincular el socket a la dirección y el puerto
    s.bind(("localhost", PORT))
    s.listen(5)

    # Aceptar conexiones de clientes
    while True:
        conn, addr = s.accept()
        with conn:
            # Recibir mensaje del cliente
            mensaje_json = conn.recv(1024).decode("utf-8")
            mensaje = json.loads(mensaje_json)

            # Procesar la solicitud del cliente
            if mensaje["accion"] == "obtener_atributos":
                # Cargar datos de atributos (por ejemplo, desde una base de datos)
                atributos = [
                    {"nombre": "Funcionalidad", "valor": 80, "descripcion": "Nivel de funcionalidad del software"},
                    {"nombre": "Eficiencia", "valor": 75, "descripcion": "Eficiencia del software en términos de uso de recursos"},
                    {"nombre": "Compatibilidad", "valor": 90, "descripcion": "Compatibilidad del software con diferentes plataformas y sistemas operativos"},
                    # ... agregar más atributos ...
                ]

                # Enviar respuesta al cliente
                respuesta = {
                    "accion": "atributos_obtenidos",
                    "atributos": atributos,
                }
                respuesta_json = json.dumps(respuesta)
                conn.sendall(respuesta_json.encode("utf-8"))
            else:
                # Enviar mensaje de error al cliente
                respuesta = {
                    "accion": "error",
                    "mensaje": "Solicitud no válida",
                }
                respuesta_json = json.dumps(respuesta)
                conn.sendall(respuesta_json.encode("utf-8"))
