import math as m
from statistics import mean


def diag(a:int, b:int, c:int) -> float:
    return m.sqrt(a**2 + b**2 + c**2)

def volume(a:int, b:int, c:int) -> int:
    return a * b * c

def surface_area(a:int, b:int, c:int) -> int:
    return 2 * (a * b + a * c + b * c)

def alpha(a:int, diag:float) -> float:
    return m.degrees(m.acos(a / diag))

def beta(b:int, diag:float) -> float:
    return m.degrees(m.acos(b / diag))

def gamma(c:int, diag:float) -> float:
    return m.degrees(m.acos(c / diag))

def radius_desc_sph(diag:float) -> float:
    return diag / 2

def volume_desc_sph(radius:float) -> float:
    return (4 / 3) * m.pi * radius**3

def average(lst: list) -> float:
    return mean(lst)
