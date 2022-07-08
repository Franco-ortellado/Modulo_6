import time

hora = time.strftime("%H")
min = time.strftime("%M")

if (int(hora) >= 23):
    print("ve a casa")
else:
    print("falta {}hs y {}min. para ir a casa".format(22-int(hora),59-int(min)))