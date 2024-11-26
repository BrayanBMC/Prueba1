# **Solución al Ejercicio de Análisis de Logs**

## **Descripción del problema**
El objetivo es desarrollar un script en Python que lea un archivo de logs llamado `access.log` y extraiga la siguiente información:

1. **Las 5 IPs más frecuentes** en los registros.
2. **El total de errores 404** registrados en el archivo.

Cada línea del archivo `access.log` tiene el siguiente formato:
```
192.168.1.1 - - [10/Nov/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 4523
```

### **Estructura de un log**
- `192.168.1.1`: Dirección IP del cliente.
- `[10/Nov/2024:13:55:36 +0000]`: Fecha y hora de la solicitud.
- `"GET /index.html HTTP/1.1"`: Solicitud HTTP realizada.
- `200`: Código de estado HTTP (por ejemplo, `404` indica un error).
- `4523`: Tamaño de la respuesta en bytes.

---

## **Solución**
### **1. Generación de un archivo de logs aleatorios**
El primer paso fue crear un archivo `access.log` con datos simulados utilizando Python. Esto facilita las pruebas del script.

#### Código para generar `access.log`:
```python
import random
from datetime import datetime

ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5", "192.168.1.6", "192.168.1.7",
        "192.168.1.8", "192.168.1.9"]
statuses = [200, 404]
urls = ["/index.html", "/notfound", "/login"]

with open("access.log", "w") as file:
    for _ in range(50):
        ip = random.choice(ips)
        status = random.choice(statuses)
        url = random.choice(urls)
        size = random.randint(100, 5000)
        log = f'{ip} - - [{datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {url} HTTP/1.1" {status} {size}\n'
        file.write(log)
```

#### Salida simulada de `access.log`:
```
192.168.1.1 - - [10/Nov/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 4523
192.168.1.2 - - [10/Nov/2024:14:01:05 +0000] "GET /notfound HTTP/1.1" 404 243
...
```

---

### **2. Análisis del archivo de logs**
Una vez generado el archivo, se desarrolló un script para leerlo, procesarlo y extraer los datos solicitados.

#### Funcionalidades del script:
- Leer el archivo `access.log`.
- Extraer las direcciones IP y los códigos de estado HTTP.
- Contar las ocurrencias de cada IP.
- Calcular el total de errores `404`.
- Mostrar los resultados de forma clara y ordenada.

#### Código:
```python
from collections import Counter

def leer(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {ruta_archivo} no se encontró.")
    except Exception as e:
        raise RuntimeError(f"Ocurrió un error al leer el archivo: {e}")

def extraer_ip_estado(linea):
    partes = linea.split()
    ip = partes[0]
    estado = partes[-2]
    return ip, estado

def contar_ips_errores(lineas):
    ip_contador = Counter()
    errores_404 = 0
    
    for linea in lineas:
        ip, estado = extraer_ip_estado(linea)
        ip_contador[ip] += 1
        if estado == "404":
            errores_404 += 1
    
    return ip_contador, errores_404

def mostrar_resultados(ip_contador, errores_404):
    cinco_ips = ip_contador.most_common(5)
    print("Las 5 IPs más frecuentes:")
    for ip, cantidad in cinco_ips:
        print(f"{ip}: {cantidad} veces")
    print(f"\nTotal de errores 404: {errores_404}")

def ejecutar():
    ruta_archivo = "access.log"
    
    def procesar_archivo(ruta, leer_func, contar_func, mostrar_func):
        try:
            lineas = leer_func(ruta)
            ip_contador, errores_404 = contar_func(lineas)
            mostrar_func(ip_contador, errores_404)
        except Exception as e:
            print(e)

    procesar_archivo(ruta_archivo, leer, contar_ips_errores, mostrar_resultados)

ejecutar()
```

---

## **Cómo usar**
1. **Crear el archivo de logs**:
   Ejecuta el script para generar `access.log` con datos aleatorios.

2. **Analizar los logs**:
   Ejecuta el script de análisis para obtener las IPs más frecuentes y el total de errores `404`.

3. **Resultados esperados**:
   - Una lista con las 5 direcciones IP más frecuentes.
   - Un total acumulado de errores `404`.

---

## **Tecnologías utilizadas**
- **Lenguaje:** Python 3
- **Módulos:** `random`, `datetime`, `collections.Counter`

---
