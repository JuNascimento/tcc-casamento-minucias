import sys
import skimage
import numpy as np
from skimage import io

from abreImagem import abreImagem
from lerArquivosMinucias import lerArquivosMinucias
from transformaEmFloat import transformaEmFloat
from formaTuplas import formaTuplas
from formaDeltas import formaDeltas

NOME_ARQUIVO_MINUCIAS_REFERENCIA = sys.argv[1].split(".tif")[0] + ".txt"
NOME_ARQUIVO_MINUCIAS_COMPARACAO = sys.argv[2].split(".tif")[0] + ".txt"

(dimensao_imagem_referencia, dimensao_imagem_comparacao) = abreImagem(sys.argv[1], sys.argv[2])

print("\n--------------------------\n")

(valores_x_referencia, valores_y_referencia, angulo_referencia, tipo_referencia) = lerArquivosMinucias(NOME_ARQUIVO_MINUCIAS_REFERENCIA)

valores_x_referencia = transformaEmFloat(valores_x_referencia)
valores_y_referencia = transformaEmFloat(valores_y_referencia)
angulo_referencia = transformaEmFloat(angulo_referencia)

(valores_x_comparacao, valores_y_comparacao, angulo_comparacao, tipo_comparacao) = lerArquivosMinucias(NOME_ARQUIVO_MINUCIAS_COMPARACAO)

valores_x_comparacao = transformaEmFloat(valores_x_comparacao)
valores_y_comparacao = transformaEmFloat(valores_y_comparacao)
angulo_comparacao = transformaEmFloat(angulo_comparacao)

tuplas_referencia = formaTuplas(valores_x_referencia, valores_y_referencia, angulo_referencia)
tuplas_comparacao = formaTuplas(valores_x_comparacao, valores_y_comparacao, angulo_comparacao)
