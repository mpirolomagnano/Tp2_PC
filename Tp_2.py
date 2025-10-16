print("Hola")
print("tp")
print("aprobar")
import os
from PIL import Image
import numpy as np
import random

def distancia_euclideana(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def distancia_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
