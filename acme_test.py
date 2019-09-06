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
        for x in range(len(generate_products())):
            names.append(generate_products()[x].name)

        for x in range(len(names)):
            self.assertIn(ADJECTIVES, names[x])
            self.assertIn(NOUNS, names[x])

if __name__ == '__main__':
    unittest.main()
