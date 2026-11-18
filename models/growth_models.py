import math 

def linear_growth(t, V, c):
"""
Bereken de groeisnelheid volgens het lineaire groeimodel.

Parameters:
    t: tijd
    V: huidige tumorvolume
    c: groeiconstante

    Returns:
        De constante groeisnelheid van het tumorvolume

"""

    return c



def exponential_growth(t, V, c):
    """
    Bereken de groeisnelheid volgens het exponentiële groeimodel.

    Parameters:
        t: tijd
        V: huidig tumorvolume
        c: groeiconstante

    Returns:
        De groeisnelheid dV/dt
    """
    return c * V



def logistic_growth(t, V, c, Vmax):
    """
    Berekent de groeisnelheid volgens
    het logistische groeimodel.

    Parameters:
        t: tijd
        V: huidig tumorvolume
        c: groeiconstante
        Vmax: maximaal tumorvolume

    Returns:
        Groeisnelheid dV/dt
    """
    return c * V * (Vmax - V)




def gompertz_growth(t, V, c, Vmax):
    """
    Berekent de groeisnelheid van een tumor
    volgens het Gompertz-groeimodel.

    Parameters:
        t: tijd
        V: huidig tumorvolume
        c: groeiconstante
        Vmax: maximaal tumorvolume

    Returns:
        Groeisnelheid dV/dt
    """
    return c * V * math.log(Vmax / V)
