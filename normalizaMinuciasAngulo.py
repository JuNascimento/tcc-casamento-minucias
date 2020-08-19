import numpy as np


def normalizaMinuciasAngulo(minucias_angulo):
  matriz_modulo = np.mod(minucias_angulo, 360)
  indices_maiores_180 = np.where(matriz_modulo > 180)
  lista_indices_maiores_180 = list(
    zip(indices_maiores_180[0], indices_maiores_180[1]))
  for item in lista_indices_maiores_180:
    matriz_modulo[item[0], item[1]] = matriz_modulo[item[0], item[1]] - 360

  return matriz_modulo
