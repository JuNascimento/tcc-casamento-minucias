import sys
import math
import numpy as np

from descobreDadosImagens import descobreDadosImagens
from leArquivosMinucias import lerArquivosMinucias
from transformaEmFloat import transformaEmFloat
from transformaMinuciasEmMatrizes import transformaMinuciasEmMatrizes
from descobreMediaMinucias import descobreMediaMinucias
from normalizaMinuciasAngulo import normalizaMinuciasAngulo

np.set_printoptions(
  threshold=sys.maxsize,
  precision=2,
  suppress=True,
  linewidth=200)

NOME_ARQUIVO_MINUCIAS_REFERENCIA = sys.argv[1].split(".tif")[0] + ".txt"
NOME_ARQUIVO_MINUCIAS_COMPARACAO = sys.argv[2].split(".tif")[0] + ".txt"

(valores_x_referencia,
  valores_y_referencia,
  angulo_referencia,
  tipo_referencia) = lerArquivosMinucias(NOME_ARQUIVO_MINUCIAS_REFERENCIA)

valores_x_referencia = transformaEmFloat(valores_x_referencia)
valores_y_referencia = transformaEmFloat(valores_y_referencia)
angulo_referencia = transformaEmFloat(angulo_referencia)

(valores_x_comparacao,
  valores_y_comparacao,
  angulo_comparacao,
  tipo_comparacao) = lerArquivosMinucias(NOME_ARQUIVO_MINUCIAS_COMPARACAO)

valores_x_comparacao = transformaEmFloat(valores_x_comparacao)
valores_y_comparacao = transformaEmFloat(valores_y_comparacao)
angulo_comparacao = transformaEmFloat(angulo_comparacao)

dados_minucias = {
  "imagem_referencia": {
    "nome_arquivo": sys.argv[1],
    "valores_minucias": [
      valores_x_referencia,
      valores_y_referencia,
      angulo_referencia]},
  "imagem_comparacao": {
    "nome_arquivo": sys.argv[2],
    "valores_minucias": [
      valores_x_comparacao,
      valores_y_comparacao,
      angulo_comparacao]},
}

descobreDadosImagens(dados_minucias)

valores_x_referencia = transformaMinuciasEmMatrizes(valores_x_referencia)
valores_y_referencia = transformaMinuciasEmMatrizes(valores_y_referencia)
angulo_referencia = transformaMinuciasEmMatrizes(angulo_referencia)

valores_x_comparacao = transformaMinuciasEmMatrizes(valores_x_comparacao)
valores_y_comparacao = transformaMinuciasEmMatrizes(valores_y_comparacao)
angulo_comparacao = transformaMinuciasEmMatrizes(angulo_comparacao)

(media_minucias_x_referencia, media_minucias_y_referencia) = descobreMediaMinucias(
  valores_x_referencia, valores_y_referencia, "referência")
(media_minucias_x_comparacao, media_minucias_y_comparacao) = descobreMediaMinucias(
  valores_x_comparacao, valores_y_comparacao, "comparação")

print("\n--------------------------\n")

# reposicionamento e transformação em matriz da imagem de referencia
matriz_reposicionada_x_referencia = valores_x_referencia.dot(
  np.ones((1, valores_x_comparacao.shape[0]))) - media_minucias_x_referencia
matriz_reposicionada_y_referencia = valores_y_referencia.dot(
  np.ones((1, valores_y_comparacao.shape[0]))) - media_minucias_y_referencia
matriz_reposicionada_angulo_referencia = angulo_referencia.dot(
  np.ones((1, angulo_comparacao.shape[0])))

# reposicionamento e transformação em matriz da imagem de comparação
matriz_reposicionada_x_comparacao = np.ones(
  (valores_x_referencia.shape[0], 1)).dot(
    valores_x_comparacao.transpose()) - media_minucias_x_comparacao
matriz_reposicionada_y_comparacao = np.ones(
  (valores_y_referencia.shape[0], 1)).dot(
    valores_y_comparacao.transpose()) - media_minucias_y_comparacao
matriz_reposicionada_angulo_comparacao = np.ones(
  (angulo_referencia.shape[0], 1)).dot(
    angulo_comparacao.transpose())

# max que vai permitir de translacao
min_dx = -600
max_dx = 600
step_x = 10
min_rot = -100
max_rot = 100
step_rot = 10
nx = round((max_dx - min_dx) / step_x + 1)
ny = nx
nr = round((max_rot - min_rot) / step_rot + 1)

# montagem da matriz acumuladora
A = np.zeros((ny, nx, nr))
print("Tamanho da matriz A -->", A.shape)

diferenca_angulo_minucias = normalizaMinuciasAngulo(
  matriz_reposicionada_angulo_comparacao -
  matriz_reposicionada_angulo_referencia)

theta = diferenca_angulo_minucias * math.pi / 180

# define a translação considerando a rotação
translacao_x = matriz_reposicionada_x_comparacao - np.multiply(
  matriz_reposicionada_x_referencia, np.cos(theta)) - np.multiply(
    matriz_reposicionada_y_referencia, np.sin(theta))
translacao_y = matriz_reposicionada_y_comparacao + np.multiply(
  matriz_reposicionada_x_referencia, np.sin(theta)) - np.multiply(
    matriz_reposicionada_y_referencia, np.cos(theta))

index_x = np.rint((translacao_x - min_dx) / step_x + 1)
index_y = np.rint((translacao_y - min_dx) / step_x + 1)
index_r = np.rint((diferenca_angulo_minucias - min_rot) / step_rot + 1)

valores_dentro_limite = np.where(
  (index_x > 0) & (
    index_x <= nx) & (
      index_y > 0) & (
        index_y <= ny) & (
          abs(diferenca_angulo_minucias) < max_rot))

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
