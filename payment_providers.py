import random


class ProcessPayment:
    def __init__(self, amount):
        self.amt = amount

    def select_payment_provider(self):
        # A random boolean value to mimic the availability of the payment gateway
        expensive_payment_available = random.sample([True, False], 1)[0]

        if self.amt > 500:
            processed = [self.premium_payment_gateway()]
            # retry up to 3 times in case payment does not get processed.
            if processed[0] is False:
                counter = 0
                while counter < 3:
                    processed[0] = self.premium_payment_gateway()
                    counter += 1

            return processed[0]

        # Checks availability of expensive_payment gateway
        # Otherwise, retry only once with CheapPaymentGateway.
        if (self.amt >= 21 or self.amt <= 500) and expensive_payment_available:
            return self.expensive_payment_gateway()

        # Using cheap_payment gateway
        return self.cheap_payment_gateway()

    @staticmethod
    def cheap_payment_gateway():
        return True

    @staticmethod
    def expensive_payment_gateway():
        return True

    @staticmethod
    def premium_payment_gateway():
        return random.sample([True, False], 1)[0]


if __name__ == '__main__':
    amt = ProcessPayment(amount=45).select_payment_provider()
    print(amt)
