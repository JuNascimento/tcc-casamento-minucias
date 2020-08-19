import numpy as np

def transformaMinuciasEmMatrizes(minucias):
  minucias_em_numpy = np.array(minucias)
  quantidade_minucias = len(np.array(minucias))

  valores = np.reshape(minucias_em_numpy, (quantidade_minucias, 1))

  return valores
