import unittest
from funcionRadio import area
from math import pi


class TestArea(unittest.TestCase):
    def test_area(self):
        print('----test valores de resultado conocido ')
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0) 
        self.assertAlmostEqual(area(3), pi*(3**2)) 
        self.assertRaises(ValueError, area ,  -1)
        self.assertRaises(ValueError, area, 'hola')
        self.assertRaises(ValueError, area, 2+3j)
        #Test de valores negativos 
    def test_negativos(self): 
      
        print('-----Test de valores negativos-----') 
         #Indicamos el tipo de excepción, la función y el valor esperado. 
        self.assertRaises(ValueError, area, -1) 
    def test_tipos(self):

        print( '-----Test de tipos no compatibles-----')
         #Indicamos el tipo de excepción, la función y el valor esperado.
        self.assertRaises(ValueError, area, 'hola')
        self.assertRaises(ValueError, area, 2+3j)


         
       

if __name__ == '__main__':
    unittest.main()