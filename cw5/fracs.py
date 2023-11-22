import math

def najmniejszaWspolnaWielokrotnosc(a, b):
    return (a * b) / math.gcd(a, b)

def add_frac(frac1, frac2):       # frac1 + frac2
    mianownik = najmniejszaWspolnaWielokrotnosc(frac1[1], frac2[1])
    licznik = frac1[0] * (mianownik / frac1[1]) + frac2[0] * (mianownik / frac2[1])
    return [licznik, mianownik]

def sub_frac(frac1, frac2):       # frac1 - frac2
    mianownik = najmniejszaWspolnaWielokrotnosc(frac1[1], frac2[1])
    licznik = frac1[0] * (mianownik / frac1[1]) - frac2[0] * (mianownik / frac2[1])
    return [licznik, mianownik]

def mul_frac(frac1, frac2):        # frac1 * frac2
    licznik = frac1[0] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    gcd = math.gcd(licznik, mianownik)
    return [licznik / gcd, mianownik / gcd]
def div_frac(frac1, frac2):        # frac1 / frac2
    if is_zero(frac2): raise ZeroDivisionError
    return mul_frac(frac1, frac2[::-1])

def is_positive(frac):             # bool, czy dodatni
    return frac[0] > 0 and frac[1] > 0 or frac[0] < 0 and frac[1] < 0

def is_zero(frac):                 # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    mianownik = najmniejszaWspolnaWielokrotnosc(frac1[1], frac2[1])
    licznik1 = frac1[0] * (mianownik / frac1[1])
    licznik2 = frac2[0] * (mianownik / frac2[1])

    if licznik1 > licznik2:
        return 1
    elif licznik1 < licznik2:
        return -1
    else:
        return 0

def frac2float(frac):              # konwersja do float
    return frac[0] / frac[1]


import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([-1, 2], [-1, 3]), [-1, 6])
        self.assertEqual(sub_frac([0, 1], [23, 100]), [-23, 100])
    def test_mul_frac(self):
        self.assertEqual(mul_frac([1,23],[2,64]),[1,736])
        self.assertEqual(mul_frac([0,23],[2,64]),[0,1])

    def test_div_frac(self):
        self.assertEqual(div_frac([43, 12], [21, 11]), [473, 252])
        self.assertRaises(ZeroDivisionError,div_frac,[1,1],[0,1])

    def test_is_positive(self):
        self.assertEqual(is_positive([1,1]),True)
        self.assertEqual(is_positive([-1,1]),False)
        self.assertEqual(is_positive([1,-1]),False)

    def test_is_zero(self):
        self.assertEqual(is_zero([1,-1]),False)
        self.assertEqual(is_zero([0,0]),True)
        self.assertEqual(is_zero([0,1]),True)
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,2],[2,3]),-1)
        self.assertEqual(cmp_frac([2,2],[2,3]),1)
        self.assertEqual(cmp_frac([2,3],[2,3]),0)
        self.assertEqual(cmp_frac([0,3],[0,13]),0)
    def test_frac2float(self):
        self.assertEqual(frac2float([8,40]),0.2)
        self.assertEqual(frac2float([0,4]),0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy