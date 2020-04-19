import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def descobreDadosImagens(dadosMinucias):
    caminho_arquivo1 = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + dadosMinucias["imagem_referencia"]["nome_arquivo"]
    caminho_arquivo2 = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + dadosMinucias["imagem_comparacao"]["nome_arquivo"]
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

    print("\n--------------------------\n")

    print("Número de minúcias encontradas na imagem de referência -->", len(dadosMinucias["imagem_referencia"]["valores_minucias"][0]))
    print("Número de minúcias encontradas na imagem de comparação -->", len(dadosMinucias["imagem_comparacao"]["valores_minucias"][0]))

    print("\n--------------------------\n")

    # plot de dois gráficos com as minúcias marcadas de cada imagem
    grafico_2d_minucias = plt.figure()
    grafico_referencia = grafico_2d_minucias.add_subplot(1,2,1)
    grafico_referencia.scatter(dadosMinucias["imagem_referencia"]["valores_minucias"][0], dadosMinucias["imagem_referencia"]["valores_minucias"][1], c='g', marker='o')
    grafico_comparacao = grafico_2d_minucias.add_subplot(1,2,2)
    grafico_comparacao.scatter(dadosMinucias["imagem_comparacao"]["valores_minucias"][0], dadosMinucias["imagem_comparacao"]["valores_minucias"][1], c='g', marker='o')
    plt.show()