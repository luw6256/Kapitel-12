import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


zeit = time.time()
wartezeit = time.sleep("5")
name="ich"

# aktuelle Uhrzeit anzeigen
print("Die aktuelle Uhrzeit ist:", time.strftime("%H:%M", time.localtime(zeit)), " Uhr")

"""angabe wie viel Zeit gewartet wurde bis dieser Print ausgeführt wird"""
print(f"Wow es sind {wartezeit} Sekunden vergangen")

    print(f"Hallo ich_bin {name}")