import unittest
from mobile_factory import MobileFactory

class TestMobileFactory(unittest.TestCase):
    def test_validate_order(self):
        components_valid = ['A', 'I', 'F', 'D', 'K']
        components_invalid = ['A', 'I', 'F', 'D']
        self.assertTrue(MobileFactory.validate_order(components_valid))
        self.assertFalse(MobileFactory.validate_order(components_invalid))

    def test_calculate_total(self):
        components = ['A', 'I', 'F', 'D', 'K']
        expected_total = 10.28 + 42.31 + 18.77 + 25.94 + 45.00
        self.assertEqual(MobileFactory.calculate_total(components), expected_total)

    def test_create_order(self):
        components = ['A', 'I', 'F', 'D', 'K']
        expected_order = {
            "order_id": 'some-id',
            "total": 142.3,
            "parts": ['LED Screen', 'Android OS', 'USB-C Port', 'Wide-Angle Camera', 'Metallic Body']
        }
        self.assertEqual(MobileFactory.create_order(components), expected_order)

if __name__ == '__main__':
    unittest.main()
