
import serial as conn

arduino = conn.Serial(port="",baudrate=9600,timeout=1)
print("conexion con arduino exitosa")

x = [i for i in range(100)]
y = [0 for i in range(100)]
i = 0

from matplotlib import  pyplot as plt

while True:
    a = arduino.readline().decode().strip()
    y.pop(0)
    y.append(int(a))
    plt.plot(x,y)
    plt.grid = True
    plt.show()

