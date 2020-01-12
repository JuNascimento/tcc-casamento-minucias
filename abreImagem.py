import skimage
from skimage import io

def abreImagem(arquivo):
    caminho_arquivo = '/Users/julia.nascimento/Julia/uerj/10_periodo/tcc/tcc-casamento-minucias/imagens_minucias/' + arquivo
    imagem = io.imread(caminho_arquivo)
    io.imshow(imagem, cmap='gray') 
    io.show()