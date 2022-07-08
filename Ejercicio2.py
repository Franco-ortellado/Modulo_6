import time

hora = time.strftime("%H")
min = time.strftime("%M")

if (int(hora) >= 19):
    print("ve a casa")
else:
    print("falta {}hs y {}min. para ir a casa".format(18-int(hora),59-int(min)))