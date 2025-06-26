import time



zeit = time.time()
wartezeit = time.sleep("5")
name="ich"

# aktuelle Uhrzeit anzeigen
print("Die aktuelle Uhrzeit ist:", time.strftime("%H:%M", time.localtime(zeit)), " Uhr")

"""angabe wie viel Zeit gewartet wurde bis dieser Print ausgeführt wird"""
print(f"Wow es sind {wartezeit} Sekunden vergangen")

    print(f"Hallo ich bin {name}")

