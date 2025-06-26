import time   #nicht in requirements.txt ist schon in python integriert
import random #2.0.1
import pandas


"""Variablen Deklaration"""
zeit = time.time()
wartezeit = 5
name="ich"
seed = random.seed()

"""
# aktuelle Uhrzeit anzeigen
print("Die aktuelle Uhrzeit ist:", time.strftime("%H:%M", time.localtime(zeit)), " Uhr")
time.sleep(wartezeit)
#angabe wie viel Zeit gewartet wurde bis dieser Print ausgeführt wird#
print(f"Wow es sind {wartezeit} Sekunden vergangen")

      print(f"Hallo ich bin {name}")
"""

def random_numbers():

    for i in range(10, random.randint(10, 100)):
        yield i

def number_prediction():
    wins = 0
    looses = 0
    for j in random_numbers():
        prediction = random.randint(10,100)
        if j == prediction:
            print(f"hurra ich hatte Recht. Es war meine Lieblingszahl die {prediction}")
            wins += 1
        else:
            looses += 1
    print(f"Siege: {wins}, Verloren: {looses}")












































































#hatte gehofft das reicht um diese Funktion zu verstecken
def errormessages():
    try:
        random_numbers()
        number_prediction()
        print(f"Ooh Baby {time.sleep(1)}\n i feel like {time.sleep(1)}\n This Message sounds better than an Error ")
    except Exception as inst:
        print("Ooops i did it again. i played with your Code, and have a problem again.")
        print(type(inst))
        print(inst.args)
        print(inst)
        print("Ooops i did it again. i played with your Code, and have a problem again.")

errormessages()









































