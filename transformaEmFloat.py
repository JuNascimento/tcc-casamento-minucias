def transformaEmFloat(minutiae_parameter):
  float_minutiae = []
  for item in minutiae_parameter:
    float_minutiae.append(round(float(item)))

  return float_minutiae
