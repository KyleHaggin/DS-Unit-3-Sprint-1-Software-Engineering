import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10, default weight being 20,
           default flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_steal_explode(self):
        '''Test generated product with price 7, weight 30, flammability 1 has
           stealability of Not so Stealable and explode of ...boom!'''
        prod = Product('Test Product', 7, 30, 1)
        self.assertEqual(prod.stealability(), 'Not so stealable')
        self.assertEqual(prod.explode(), '...boom!')

if __name__ == '__main__':
    unittest.main()
