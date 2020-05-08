import math
import matplotlib.pyplot as plt

def transladaMatrizes(dados_minucias, index_maior_valor_A, limites):
  delta_x = (index_maior_valor_A[0] - 1) * limites["step_x"]  + limites["min_dx"]
  delta_y = (index_maior_valor_A[1] - 1) * limites["step_x"]  + limites["min_dx"]
  delta_angulo = (index_maior_valor_A[2] - 1) * limites["step_rot"] + limites["min_rot"]

  val_x_referencia_list = dados_minucias["imagem_referencia"]["valores_minucias"][0]
  val_y_referencia_list = dados_minucias["imagem_referencia"]["valores_minucias"][1]

  val_x_comparacao_list = dados_minucias["imagem_comparacao"]["valores_minucias"][0]
  val_y_comparacao_list = dados_minucias["imagem_comparacao"]["valores_minucias"][1]

  x_linha_referencia = []
  y_linha_referencia = []

  quantidade_pontos_referencia = len(val_x_referencia_list)
  for i in range(quantidade_pontos_referencia):
    valor_x_linha_referencia = \
      val_x_referencia_list[i] * math.cos(delta_angulo) +  \
        val_y_referencia_list[i] * math.sin(delta_angulo) + delta_x * 1
    valor_y_linha_referencia = \
      (-1) * val_x_referencia_list[i] * math.sin(delta_angulo) + \
        val_y_referencia_list[i] * math.cos(delta_angulo) + delta_y * 1
    x_linha_referencia.append(valor_x_linha_referencia)
    y_linha_referencia.append(valor_y_linha_referencia)

  x_linha_comparacao = []
  y_linha_comparacao = []

  quantidade_pontos_comparacao = len(val_x_comparacao_list)
  for i in range(quantidade_pontos_comparacao):
    valor_x_linha_comparacao = \
      val_x_comparacao_list[i] * math.cos(delta_angulo) +  \
        val_y_comparacao_list[i] * math.sin(delta_angulo) + delta_x * 1
    valor_y_linha_comparacao = \
      (-1) * val_x_comparacao_list[i] * math.sin(delta_angulo) + \
        val_y_comparacao_list[i] * math.cos(delta_angulo) + delta_y * 1
    x_linha_comparacao.append(valor_x_linha_comparacao)
    y_linha_comparacao.append(valor_y_linha_comparacao)

  referencia_linha = []
  for i in range(0, quantidade_pontos_referencia):
    referencia_linha.append([x_linha_referencia[i], y_linha_referencia[i]])

  comparacao_linha = []
  for i in range(0, quantidade_pontos_comparacao):
    comparacao_linha.append([x_linha_comparacao[i], y_linha_comparacao[i]])

  grafico_2d_minucias = plt.figure()
  grafico_2d_minucias.suptitle("socorro")
  plt.scatter(
    x_linha_referencia,
    y_linha_referencia,
    c='g',
    marker='o')
  plt.scatter(x_linha_comparacao, y_linha_comparacao, c='b', marker='x')
  plt.show()


  return (quantidade_pontos_referencia,
    quantidade_pontos_comparacao, referencia_linha, comparacao_linha)
