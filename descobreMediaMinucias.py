import numpy as np


def descobreMediaMinucias(minucias_x, minucias_y, tipo_minucia):
  media_minucias_x = int(np.mean(minucias_x))
  media_minucias_y = int(np.mean(minucias_y))

  print("Média das minúcias de", tipo_minucia, "em x -->", media_minucias_x)
  print(
    "Média das minúcias de", tipo_minucia, "em y -->", media_minucias_y, "\n"
  )

  return (media_minucias_x, media_minucias_y)
