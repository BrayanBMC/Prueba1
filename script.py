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