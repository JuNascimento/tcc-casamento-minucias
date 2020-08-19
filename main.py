import sys
import pprint as pp
import numpy as np

from descobreDadosImagens import descobreDadosImagens
from leArquivosMinucias import leArquivosMinucias
from transformaEmFloat import transformaEmFloat
from transformaMinuciasEmMatrizes import transformaMinuciasEmMatrizes
from descobreMediaMinucias import descobreMediaMinucias
from reposicionaMatriz import reposicionaMatriz
from montaMatrizAcumuladora import montaMatrizAcumuladora
from transladaMatrizes import transladaMatrizes
from pareiaPontos import pareiaPontos

np.set_printoptions(
  threshold=sys.maxsize,
  precision=2,
  suppress=True,
  linewidth=200)

(valores_x_referencia, valores_y_referencia, angulo_referencia) = leArquivosMinucias(sys.argv[1])

valores_x_referencia = transformaEmFloat(valores_x_referencia)
valores_y_referencia = transformaEmFloat(valores_y_referencia)
angulo_referencia = transformaEmFloat(angulo_referencia)

(valores_x_comparacao, valores_y_comparacao, angulo_comparacao) = leArquivosMinucias(sys.argv[2])

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
  valores_x_referencia, valores_y_referencia, "referência"
)
(media_minucias_x_comparacao, media_minucias_y_comparacao) = descobreMediaMinucias(
  valores_x_comparacao, valores_y_comparacao, "comparação"
)

print("\n--------------------------\n")

(matriz_reposicionada_x_referencia, matriz_reposicionada_x_comparacao) = \
  reposicionaMatriz(valores_x_referencia,
    valores_x_comparacao, media_minucias_x_referencia, media_minucias_x_comparacao
)

(matriz_reposicionada_y_referencia, matriz_reposicionada_y_comparacao) = \
  reposicionaMatriz(valores_y_referencia,
    valores_y_comparacao, media_minucias_y_referencia, media_minucias_y_comparacao
)
(matriz_reposicionada_angulo_referencia, matriz_reposicionada_angulo_comparacao) = \
  reposicionaMatriz(angulo_referencia, angulo_comparacao, 0, 0
)

limites = {
  "min_dx": -600, "max_dx": 600, "step_x": 10, "min_rot": -100, "max_rot": 100, "step_rot": 10,
}

index_maior_valor_A = montaMatrizAcumuladora(limites, matriz_reposicionada_x_referencia,
  matriz_reposicionada_x_comparacao, matriz_reposicionada_y_referencia,
  matriz_reposicionada_y_comparacao, matriz_reposicionada_angulo_referencia,
  matriz_reposicionada_angulo_comparacao
)

(quantidade_pontos_referencia, quantidade_pontos_comparacao,
  referencia_linha, comparacao_linha) = \
    transladaMatrizes(dados_minucias, index_maior_valor_A, limites)

distancia = {
  "x_y": 30,
  "rotacao": 20
}

pareiaPontos(quantidade_pontos_referencia, quantidade_pontos_comparacao,
  referencia_linha, comparacao_linha, distancia)
