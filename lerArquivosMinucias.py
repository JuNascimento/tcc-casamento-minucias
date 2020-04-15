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

    if (len(valores_x) == len(valores_y) and len(valores_x) == len(angulo) and len(valores_y) == len(tipo)):
        return (valores_x, valores_y, angulo, tipo)
    else:
        return False

