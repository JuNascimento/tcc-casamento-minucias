import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from descobreDadosImagens import descobreDadosImagens
from lerArquivosMinucias import lerArquivosMinucias
from transformaEmFloat import transformaEmFloat
from formaTuplas import formaTuplas
from transformaMinuciasEmMatrizes import transformaMinuciasEmMatrizes
from descobreMediaMinucias import descobreMediaMinucias

NOME_ARQUIVO_MINUCIAS_REFERENCIA = sys.argv[1].split(".tif")[0] + ".txt"
NOME_ARQUIVO_MINUCIAS_COMPARACAO = sys.argv[2].split(".tif")[0] + ".txt"

(valores_x_referencia, valores_y_referencia, angulo_referencia, tipo_referencia) = lerArquivosMinucias(NOME_ARQUIVO_MINUCIAS_REFERENCIA, "referência")

valores_x_referencia = transformaEmFloat(valores_x_referencia)
valores_y_referencia = transformaEmFloat(valores_y_referencia)
angulo_referencia = transformaEmFloat(angulo_referencia)

(valores_x_comparacao, valores_y_comparacao, angulo_comparacao, tipo_comparacao) = lerArquivosMinucias(NOME_ARQUIVO_MINUCIAS_COMPARACAO, "comparação")

valores_x_comparacao = transformaEmFloat(valores_x_comparacao)
valores_y_comparacao = transformaEmFloat(valores_y_comparacao)
angulo_comparacao = transformaEmFloat(angulo_comparacao)

dados_minucias = {
    "imagem_referencia": {
        "nome_arquivo": sys.argv[1],
        "valores_minucias": [valores_x_referencia, valores_y_referencia, angulo_referencia]
    },
    "imagem_comparacao": {
        "nome_arquivo": sys.argv[2],
        "valores_minucias": [valores_x_comparacao, valores_y_comparacao, angulo_comparacao]
    },
}

descobreDadosImagens(dados_minucias)

valores_x_referencia = transformaMinuciasEmMatrizes(valores_x_referencia)
valores_y_referencia = transformaMinuciasEmMatrizes(valores_y_referencia)
angulo_referencia = transformaMinuciasEmMatrizes(angulo_referencia)

valores_x_comparacao = transformaMinuciasEmMatrizes(valores_x_comparacao)
valores_y_comparacao = transformaMinuciasEmMatrizes(valores_y_comparacao)
angulo_comparacao = transformaMinuciasEmMatrizes(angulo_comparacao)

(media_minucias_x_referencia, media_minucias_y_referencia) = descobreMediaMinucias(valores_x_referencia, valores_y_referencia, "referência")
(media_minucias_x_comparacao, media_minucias_y_comparacao) = descobreMediaMinucias(valores_x_comparacao, valores_y_comparacao, "comparação")