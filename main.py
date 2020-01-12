import sys
import skimage
from skimage import io

NOME_ARQUIVO_MINUCIAS_REFERENCIA = sys.argv[1].split(".tif")[0] + ".txt"
NOME_ARQUIVO_MINUCIAS_COMPARACAO = sys.argv[2].split(".tif")[0] + ".txt"

# abre imagem
def abreImagem(arquivo):
    caminho_arquivo = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + arquivo
    imagem = io.imread(caminho_arquivo)
    io.imshow(imagem, cmap='gray') 
    io.show()

# ler arquivo com as minúcias extraídas
def lerArquivosMinucias(arquivo):
    caminho_arquivo = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/arquivos_minucias/' + arquivo
    minucias = open(caminho_arquivo, "r")
    linhas = []

    for linha in minucias:
        linhasSeparadas = linha.split("\n")
        for item in linhasSeparadas:
            if item != "":
                linhas.append(item)
    
    valores_x = linhas[0].split("   ")
    valores_x.pop(0)

    valores_y = linhas[1].split("   ")
    valores_y.pop(0)

    angulo = linhas[2].split("   ")
    angulo.pop(0)

    tipo = linhas[3].split("   ")
    tipo.pop(0)


    return (valores_x, valores_y, angulo, tipo)

# transforma os valores de string para float
def transformaEmFloat(minutiae_parameter):
    float_minutiae = []
    for item in minutiae_parameter:
        float_minutiae.append(float(item))
    
    return float_minutiae

# forma tuplas com (x,y,theta)
def formaTuplas(valores_x, valores_y, angulos):
    tuplas = []
    for itemx in range(len(valores_x)):
        for itemy in range(len(valores_y)):
            for itema in range(len(angulos)):
                if (itemx == itemy):
                    if (itemx == itema):
                        tuplas.append([int(valores_x[itemx]), int(valores_y[itemy]), angulos[itema]])

    return tuplas

# forma matriz de deltas
def formaDeltas(tuplas_referencia, tuplas_comparacao):
    delta = []
    for item_referencia in tuplas_referencia:
        for item_comparacao in tuplas_comparacao:
            x = item_referencia[0] - item_comparacao[0]
            y = item_referencia[1] - item_comparacao[1]
            theta = item_referencia[2] - item_comparacao[2]
            delta.append([x,y,round(theta, 2)])

    return delta

abreImagem(sys.argv[1])
abreImagem(sys.argv[2])

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

delta = formaDeltas(tuplas_referencia, tuplas_comparacao)

for item in delta:
    print(item)