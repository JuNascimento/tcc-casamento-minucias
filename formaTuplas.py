def formaTuplas(valores_x, valores_y, angulos):
    tuplas = []
    for itemx in range(len(valores_x)):
        for itemy in range(len(valores_y)):
            for itema in range(len(angulos)):
                if (itemx == itemy):
                    if (itemx == itema):
                        tuplas.append([int(valores_x[itemx]), int(valores_y[itemy]), angulos[itema]])

    return tuplas