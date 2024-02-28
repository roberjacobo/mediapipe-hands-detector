import cv2

def encontrar_indice_dispositivo_video(max_dispositivos=10):
    indice = -1
    for i in range(max_dispositivos):
        captura = cv2.VideoCapture(i)
        if captura.read()[0]:  # Intenta leer un cuadro para verificar si el dispositivo está disponible
            indice = i
            captura.release()  # Libera el dispositivo
            break  # Sale del bucle si encuentra un dispositivo
    return indice

indice_camara = encontrar_indice_dispositivo_video()
print(f"El índice de tu cámara es: {indice_camara}")
