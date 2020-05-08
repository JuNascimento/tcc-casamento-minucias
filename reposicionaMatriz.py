import numpy as np

def reposicionaMatriz(valores_referencia,
  valores_comparacao, media_minucias_referencia, media_minucias_comparacao):
  matriz_reposicionada_referencia = \
    valores_referencia.dot(np.ones((1, valores_comparacao.shape[0]))) - media_minucias_referencia
  matriz_reposicionada_comparacao = \
    np.ones((valores_referencia.shape[0], 1)).dot(valores_comparacao.transpose()) - \
      media_minucias_comparacao

  return (matriz_reposicionada_referencia, matriz_reposicionada_comparacao)
