import time
import random

"""Variablen Deklaration"""
zeit = time.time()
wartezeit = time.sleep("5")
name="ich"

"""
# aktuelle Uhrzeit anzeigen
print("Die aktuelle Uhrzeit ist:", time.strftime("%H:%M", time.localtime(zeit)), " Uhr")

#angabe wie viel Zeit gewartet wurde bis dieser Print ausgeführt wird#
print(f"Wow es sind {wartezeit} Sekunden vergangen")

      print(f"Hallo ich bin {name}")
"""

def random_numbers():
    seed = random.seed()
    print(seed)














































































#hatte gehofft das reicht um diese Funktion zu verstecken
def errormessages():
    try:
        random_numbers()
        print("Ooh Baby, i feel like, The code sounds better without an Error ")
    except Exception as inst:
        print("Ooops i did it again. i played with your Code, and have a problem again.")
        print(type(inst))
        print(inst.args)
        print(inst)
        print("Ooops i did it again. i played with your Code, and have a problem again.")

random_numbers()
errormessages()









































