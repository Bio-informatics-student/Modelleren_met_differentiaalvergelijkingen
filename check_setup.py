
import numpy as np
import scipy
import pandas as pd
import matplotlib
import pytest
import jupyter

print("=== Projectcontrole ===")

print("NumPy werkt:", np.__version__)
print("SciPy werkt:", scipy.__version__)
print("Pandas werkt:", pd.__version__)
print("Matplotlib werkt:", matplotlib.__version__)
print("Pytest werkt:", pytest.__version__)
print("Jupyter werkt:", jupyter.__name__)

# Test een eenvoudige berekening
getallen = np.array([1, 2, 3, 4, 5])
gemiddelde = np.mean(getallen)

print("\nGemiddelde:", gemiddelde)

assert gemiddelde == 3.0

print("\nAlle controles geslaagd!")
