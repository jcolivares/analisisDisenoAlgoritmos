import math as m

class Triangulo:

  def areaTriangulo(A, B, C):
      S = (A+B+C)/2
      area = m.sqrt(S*(S-A)*(S-B)*(S-C))
      return area
