# Local modules
import json
import unittest

# User-defined modules
from project import app

# Third-party modules


class TestInvalidRequest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        self.app = app.test_client()
        # Test if debug is off
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    # Helper method
    def process_payment_api(self, json_data: dict):
        data = json.dumps(
            dict(CreditCardNumber=json_data["credit_card_number"], CardHolder=json_data["card_holder"],
                 ExpirationDate=json_data["expire_date"], SecurityCode=json_data["security_code"],
                 Amount=json_data["amount"]
                 )
        )
        return self.app.post('/', data=data, content_type='application/json',
                             follow_redirects=True)

    def test_invalid_credit_card_number(self):
        """
        Test case for checking invalid credit card number
        """
        testcase = {
            "credit_card_number": "4121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_credit_card_number_length(self):
        """
        Test case for checking length of the credit card number
        """
        testcase = {
            "credit_card_number": "412107184815", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_credit_card_number_isString(self):
        """
        Test case for checking credit card number is string
        """
        testcase = {
            "credit_card_number": 5121071848156976, "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_credit_card_number_isProvided(self):
        """
        Test case for checking credit card number is not provided
        """
        testcase = {
            "credit_card_number": None, "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_card_holder_isString(self):
        """
        Test case for checking card holder is string
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": 897322,
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_card_holder_containsAlphabeticString(self):
        """
        Test case for checking cardholder is an alphabetic string
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy6743",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_card_holder_isProvided(self):
        """
        Test case for checking card holder is provided
        """
        testcase = {
            "credit_card_number": 5121071848156976, "card_holder": None,
            "expire_date": "2022-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_expire_date_isDatetime(self):
        """
        Test case for checking expiration date is a datetime obj
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": 989213281, "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_expire_date_isProvided(self):
        """
        Test case for checking expiration date is provided
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": None, "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_expire_date_isPast(self):
        """
        Test case for checking expiration date is in the past
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2020-05-01", "security_code": "345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_security_code_isString(self):
        """
        Test case for checking security code is string
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": 345, "amount": 7882.983
        }
        expected = 200
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)

    def test_security_code_isProvided(self):
        """
        Test case for checking security code is optional
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": None, "amount": 7882.983
        }
        expected = 200
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)

    def test_security_code_length(self):
        """
        Test case for checking security code length is 3 digits
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345345", "amount": 7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_amount_isPositive(self):
        """
        Test case for checking amount is a positive
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": -7882.983
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_amount_isProvided(self):
        """
        Test case for checking amount is provided
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": None
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)
        self.assertIn('The request is invalid: 400 bad request.', response.json['response'])

    def test_amount_isZero(self):
        """
        Test case for checking amount is zero
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 0
        }
        expected = 400
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)


class TestValidRequest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        self.app = app.test_client()
        # Test if debug is off
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    # Helper method
    def process_payment_api(self, json_data: dict):
        data = json.dumps(
            dict(CreditCardNumber=json_data["credit_card_number"], CardHolder=json_data["card_holder"],
                 ExpirationDate=json_data["expire_date"], SecurityCode=json_data["security_code"],
                 Amount=json_data["amount"]
                 )
        )
        return self.app.post('/', data=data, content_type='application/json',
                             follow_redirects=True)

    def test_valid_request(self):
        """
        Test case for checking a valid request
        """
        testcase = {
            "credit_card_number": "5121071848156976", "card_holder": "Randy Duodu",
            "expire_date": "2022-05-01", "security_code": "345", "amount": 76.89
        }
        expected = 200
        response = self.process_payment_api(json_data=testcase)
        self.assertEqual(response.status_code, expected)


if __name__ == '__main__':
    unittest.main()
