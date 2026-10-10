import unittest

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestEsPrimo(unittest.TestCase):
    def test_numeros_no_primos(self):
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(9))

    def test_numeros_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(7))

if __name__ == '__main__':
    unittest.main()