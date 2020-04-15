import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def abreImagem(arquivo1, arquivo2):
    caminho_arquivo1 = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + arquivo1
    caminho_arquivo2 = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + arquivo2
    imagem1 = plt.imread(caminho_arquivo1)
    imagem2 = plt.imread(caminho_arquivo2)
    if (imagem1.shape == imagem2.shape):
        print("Tamanho das imagens --> ", imagem1.shape)
    else: 
        print("Tamanho da imagem de referência--> ", imagem1.shape)
        print("Tamanho da imagem de comparação--> ", imagem2.shape)

    figura, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    figura.suptitle('Imagens a serem comparadas')
    ax1.set_title('Imagem de referência')
    ax1.imshow(np.rot90(imagem1,2), cmap='gray')
    ax2.set_title('Imagem de comparação')
    ax2.imshow(np.rot90(imagem2,2), cmap='gray')

    plt.show(block=True)

    return (imagem1.shape, imagem2.shape)