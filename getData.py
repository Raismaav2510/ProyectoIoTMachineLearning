import os
import pandas as pd
import urllib.error
from urllib import request
from bs4 import BeautifulSoup

hdr = {
    'User-Agent': 'Wget/1,14 (linux-gnu)',
    'Accept': '*/*'
}
csv_filename = 'datos_climaticos.csv'


def datos_climaticos():
    for year in range(1978, 2024):
        for month in range(1, 13):
            try:
                formatted_month = str(month).zfill(2)
                url = f'https://www.tutiempo.net/clima/{formatted_month}-{year}/ws-766120.html'
                req = request.Request(url, headers=hdr)
                html_noticia = request.urlopen(req).read().decode('utf8')

                data_html = BeautifulSoup(html_noticia, 'html.parser')

                table = data_html.find('table', {'class': 'medias mensuales numspan'})

                filas = table.find_all('tr')

                data = []
                for fila in filas:
                    columnas = fila.find_all(['th', 'td'])
                    fila_datos = [columna.text.strip() for columna in columnas]
                    data.append(fila_datos)

                # Crear un DataFrame de pandas
                df = pd.DataFrame(data)
                df.insert(0, 'mes', month)
                df.insert(0, 'año', year)

                # Verificar si el archivo CSV ya existe
                if os.path.exists(csv_filename):
                    # Si existe, agregar datos al final del archivo
                    df.to_csv(csv_filename, mode='a', index=False, header=False)
                else:
                    # Si no existe, crear el archivo CSV y agregar datos
                    df.to_csv(csv_filename, index=False, header=True)

                print(f'URL abierta {url}')
            except urllib.error.HTTPError as e:
                print(f'Error al abrir la URL {url}: {e}')
            except urllib.error.URLError as e:
                print(f'Error de conexión al abrir la URL {url}: {e}')
            except Exception as e:
                print(f'Otro error al abrir la URL {url}: {e}')