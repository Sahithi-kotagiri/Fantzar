import unittest
from mobile_factory import MobileFactory

class TestMobileFactory(unittest.TestCase):
    
    def test_validate_order(self):
        # Test when an order contains one and only one component of each type
        components_valid = ['A', 'I', 'F', 'D', 'K']
        components_invalid = ['A', 'I', 'F', 'D']
        self.assertTrue(MobileFactory.validate_order(components_valid))
        self.assertFalse(MobileFactory.validate_order(components_invalid))

    def test_calculate_total(self):
        # Test calculating the total price of an order
        components = ['A', 'I', 'F', 'D', 'K']
        expected_total = 10.28 + 42.31 + 18.77 + 25.94 + 45.00
        self.assertEqual(MobileFactory.calculate_total(components), expected_total)

    def test_create_order(self):
        # Test creating an order with the given components
        components = ['A', 'I', 'F', 'D', 'K']
        expected_order = {
            "order_id": 'some-id',
            "total": 142.3,
            "parts": ['LED Screen', 'Android OS', 'USB-C Port', 'Wide-Angle Camera', 'Metallic Body']
        }
        self.assertEqual(MobileFactory.create_order(components), expected_order)

    def test_validate_order_invalid_component(self):
        # Test when an invalid component code is included in the order
        components_invalid = ['A', 'I', 'F', 'D', 'X']  # 'X' is an invalid component code
        self.assertFalse(MobileFactory.validate_order(components_invalid))

    def test_validate_order_multiple_components_same_type(self):
        # Test when multiple components of the same type are included in the order
        components_multiple = ['A', 'I', 'F', 'D', 'D']  # Two components of type 'D'
        self.assertFalse(MobileFactory.validate_order(components_multiple))

    def test_create_order_empty_components(self):
        # Test with an empty list of components
        components_empty = []
        self.assertIsNone(MobileFactory.create_order(components_empty))

    def test_create_order_single_component(self):
        # Test with a single valid component
        components_single = ["I"]  # Only Android OS
        expected_order_single = {
            "order_id": 'some-id',
            "total": 42.31,
            "parts": ['Android OS']
        }
        self.assertEqual(MobileFactory.create_order(components_single), expected_order_single)


if __name__ == '__main__':
    unittest.main()
