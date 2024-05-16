import serial
import time

# Configura la conexión serial (reemplaza 'COM3' con el puerto correspondiente si es necesario)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Espera 2 segundos para asegurarse de que la conexión se establezca correctamente

def mover_servo(angulo):
    arduino.write(f"{angulo}\n".encode())  # Envía el ángulo al Arduino
    time.sleep(0.02)  # Espera un corto periodo de tiempo

try:
    while True:
        # Mueve el servo de 0 a 180 grados
        for angulo in range(0, 181):
            mover_servo(angulo)
            time.sleep(0.02)
        time.sleep(1)  # Espera 1 segundo al llegar a 180 grados

        # Mueve el servo de 180 a 0 grados
        for angulo in range(180, -1, -1):
            mover_servo(angulo)
            time.sleep(0.02)
        time.sleep(1)  # Espera 1 segundo al llegar a 0 grados

except KeyboardInterrupt:
    print("Programa interrumpido")
finally:
    arduino.close()  # Cierra la conexión serial al final del programa
