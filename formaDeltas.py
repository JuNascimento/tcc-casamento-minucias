def formaDeltas(tuplas_referencia, tuplas_comparacao):
    delta = []
    for item_referencia in tuplas_referencia:
        for item_comparacao in tuplas_comparacao:
            x = item_referencia[0] - item_comparacao[0]
            y = item_referencia[1] - item_comparacao[1]
            theta = item_referencia[2] - item_comparacao[2]
            delta.append([x,y,round(theta, 2)])

    return delta