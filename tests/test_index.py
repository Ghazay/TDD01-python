from unittest import TestCase

from index import ma_fonction


class Test(TestCase):
    def test_ma_fonction(self):
        self.assertEqual(ma_fonction(), "Bienvenue à TDD01")
