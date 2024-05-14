import socket
import json

# Definir dirección y puerto del servidor
HOST = "localhost"  # Cambiar por la dirección IP del servidor si es necesario
PORT = 5000

# Crear socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar al servidor
    s.connect((HOST, PORT))

    # Enviar mensaje al servidor
    mensaje = {
        "accion": "obtener_atributos",
    }
    mensaje_json = json.dumps(mensaje)
    s.sendall(mensaje_json.encode("utf-8"))

    # Recibir respuesta del servidor
    respuesta_json = s.recv(1024).decode("utf-8")
    respuesta = json.loads(respuesta_json)

    # Procesar la respuesta
    if respuesta["accion"] == "atributos_obtenidos":
        atributos = respuesta["atributos"]
        for atributo in atributos:
            print(f"Nombre: {atributo['nombre']}")
            print(f"Valor: {atributo['valor']}")
            print(f"Descripción: {atributo['descripcion']}")
            print("-" * 20)
    else:
        print("Error al obtener atributos")
