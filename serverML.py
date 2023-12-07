import mysql.connector
import NeuralNetwork
from datetime import datetime

# Establecer la conexión con la base de datos
conection = mysql.connector.connect(
    host="localhost",
    port=33,
    user="root",
    password="",
    database="iot"
)

def consulta():
    # Crear un cursor para ejecutar consultas
    cursor = conection.cursor()

    # Obtener la fecha actual
    date_py = datetime.now().strftime('%Y-%m-%d')
    date_py = '2023-12-01'
    # Ejecutar una consulta para obtener los últimos datos de la base de datos
    query = f"SELECT humidityAir, temperature, date FROM information WHERE date = '{date_py}' ORDER BY datahour DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.execute(query)
    result = cursor.fetchall()

    # Cerrar la conexión y el cursor
    cursor.close()
    conection.close()

    # Hacer algo con los datos obtenidos
    if result is not None:
        print(result)
        humidityAir, temperature, date = result[0]
        date = int(date[5:7])

        # Crear la lista data
        data = [date, temperature, humidityAir]
        print(data)

        # Hacer prediccion con el modelo entrenado
        prediction = NeuralNetwork.eval_data(data, rounded=True)
        print(prediction)

