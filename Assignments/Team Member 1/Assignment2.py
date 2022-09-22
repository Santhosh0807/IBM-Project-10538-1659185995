import random
import time

def CheckTemp(temperature):
    if temperature>70:
        print("Temperature is high")

temp = random.randint(-40,100)
humid = random.randint(0,100)

while True:
    temp = random.randint(-40,100)
    humid = random.randint(0,100)
    print("Temperature = "+str(temp))
    print("Humidity = "+str(humid))
    CheckTemp(temp)
    time.sleep(1)