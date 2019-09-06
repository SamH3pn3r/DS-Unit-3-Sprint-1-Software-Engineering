import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test')
        self.assertEqual(prod.weight, 20)

    def test_product_weight(self):
        prod = Product('Test instance', weight=50)
        self.assertEqual(prod.explode(), "...boom")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        names = []
        prod_list = generate_products()
        adj_noun = ADJECTIVES + NOUNS
        for prod in prod_list:
            words = prod.name.split()
            for word in words:
                self.assertIn(word, adj_noun)

if __name__ == '__main__':
    unittest.main()
