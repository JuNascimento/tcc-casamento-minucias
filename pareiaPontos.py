from scipy import spatial

def pareiaPontos(quantidade_pontos_referencia, quantidade_pontos_comparacao,
  referencia_linha, comparacao_linha, distancia):

  pontos_x_dentro_limite = []
  pontos_y_dentro_limite = []
  contador = 0
  for i in range(0, quantidade_pontos_referencia):
    for j in range(0, quantidade_pontos_comparacao):
      distancia = spatial.distance.euclidean(referencia_linha[i], comparacao_linha[j])
      if distancia < distancia["x_y"]:
        pontos_x_dentro_limite.append(referencia_linha[i])
        pontos_y_dentro_limite.append(comparacao_linha[j])
        contador = contador + 1

  print("Distância máxima aceita entre (x, y) -->", distancia["x_y"])
  print("Quantidade de duplas pareadas -->", contador)
  print("\n--------------------------\n")
