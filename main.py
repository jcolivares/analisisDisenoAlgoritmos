import unittest
import math as m

class Triangulo:

  def areaTriangulo(A, B, C):
      S = (A+B+C)/2
      area = m.sqrt(S*(S-A)*(S-B)*(S-C))
      return area


class TestTriangulo(unittest.TestCase):
    def testEscaleno(self):
        A,B,C = 3,4,5
        areaEsperada = 6
        areaObtenida = Triangulo.areaTriangulo(A,B,C)
        self.assertEqual(areaEsperada, areaObtenida)

    def testNoTriangulo(self):
        A,B,C = 1,2,3
        areaEsperada = 0
        areaObtenida = Triangulo.areaTriangulo(A,B,C)
        self.assertEqual(areaEsperada, areaObtenida)


if __name__ == "__main__":
    unittest.main()