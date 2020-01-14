import matplotlib
import matplotlib.pyplot as plt

def abreImagem(arquivo):
    caminho_arquivo = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + arquivo
    imagem = plt.imread(caminho_arquivo)
    print("Tamanho da imagem --> ", imagem.shape)
    plt.title(arquivo)
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.imshow(imagem, cmap='gray')
    plt.show()