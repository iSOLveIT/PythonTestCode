# Local modules
import unittest

# User-defined modules
from project.payment_providers import ProcessPayment

# Third-party modules


class TestPaymentGateWay(unittest.TestCase):
    def test_premium_payment_gateway(self):
        """
        Test case for premium payment gateway
        Payment can either be processed or not after the retry hence expectation can be True or False
        """
        testcase_amount = 89945
        expected = bool
        response = ProcessPayment(testcase_amount).select_payment_provider()
        self.assertEqual(type(response[0]), expected)
        self.assertIn('Premium Payment', response[1])

    def test_expensive_payment_gateway(self):
        """
        Test case for expensive payment gateway
        The payment process can bbe available or not hence we could get Expensive Payment or Cheap payment
        """
        testcase_amount = 234
        expected = True
        response = ProcessPayment(testcase_amount).select_payment_provider()
        self.assertEqual(response[0], expected)

    def test_cheap_payment_gateway(self):
        """
        Test case for cheap payment gateway
        """
        testcase_amount = 15
        expected = True
        response = ProcessPayment(testcase_amount).select_payment_provider()
        self.assertEqual(response[0], expected)
        self.assertIn('Cheap Payment', response[1])


if __name__ == '__main__':
    unittest.main()
