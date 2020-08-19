import math
import numpy as np

from normalizaMinuciasAngulo import normalizaMinuciasAngulo

def montaMatrizAcumuladora(limites, x_referencia, x_comparacao, y_referencia, y_comparacao,
  angulo_referencia, angulo_comparacao):

  nx = round((limites["max_dx"] - limites["min_dx"]) / limites["step_x"] + 1)
  ny = round((limites["max_dx"] - limites["min_dx"]) / limites["step_x"] + 1)
  nr = round((limites["max_rot"] - limites["min_rot"]) / limites["step_rot"] + 1)

  A = np.zeros((ny, nx, nr))
  print("Tamanho da matriz A -->", A.shape)

  diferenca_angulo_minucias = normalizaMinuciasAngulo(angulo_comparacao - angulo_referencia)

  theta = diferenca_angulo_minucias * math.pi / 180

  translacao_x = x_comparacao - np.multiply(
    x_referencia, np.cos(theta)) - np.multiply(
      y_referencia, np.sin(theta))
  translacao_y = y_comparacao + np.multiply(
    x_referencia, np.sin(theta)) - np.multiply(
      y_referencia, np.cos(theta))

  index_x = np.rint((translacao_x - limites["min_dx"]) / limites["step_x"] + 1)
  index_y = np.rint((translacao_y - limites["min_dx"]) / limites["step_x"] + 1)
  index_r = np.rint((diferenca_angulo_minucias - limites["min_rot"]) / limites["step_rot"] + 1)

  valores_dentro_limite = np.where(
    (index_x > 0) & (
      index_x <= nx) & (
        index_y > 0) & (
          index_y <= ny) & (
            abs(diferenca_angulo_minucias) < limites["max_rot"]))

  for i in range(0, len(valores_dentro_limite[0] - 1)):
    idx_x = int(index_x[valores_dentro_limite[0][i], valores_dentro_limite[1][i]])
    idx_y = int(index_y[valores_dentro_limite[0][i], valores_dentro_limite[1][i]])
    idx_r = int(index_r[valores_dentro_limite[0][i], valores_dentro_limite[1][i]])
    A[idx_y, idx_x, idx_r] = A[idx_y, idx_x, idx_r] + 1

  total_minucias_A_nonzero = list(zip(A.nonzero()[0], A.nonzero()[1], A.nonzero()[2]))
  print("Total de valores encontrados em A diferente de zero -->", len(total_minucias_A_nonzero))
  index_maior_valor_A = np.unravel_index(np.argmax(A, axis=None), A.shape)
  print("Maior valor encontrado em A -->", np.max(A))
  print("Posição do maior valor encontrado em A -->", index_maior_valor_A)
  print("\n--------------------------\n")

  return index_maior_valor_A
