# Local modules
import random
from typing import List, Tuple

# User-defined modules

# Third-party modules


class ProcessPayment:
    def __init__(self, amount: float) -> None:
        self.amt: float = amount

    def select_payment_provider(self) -> Tuple[bool, str]:
        # A random boolean value to mimic the availability of the payment gateway
        expensive_payment_available: bool = random.sample([True, False], 1)[0]

        if self.amt > 500:
            # Using Premium Payment
            processed: List[Tuple[bool, str]] = [self.premium_payment_gateway()]
            is_processed, _ = processed[0]
            # retry up to 3 times in case payment does not get processed.
            if is_processed is False:
                counter: int = 0
                while counter < 3 and is_processed is False:
                    processed[0] = self.premium_payment_gateway()
                    counter += 1

            return processed[0]

        # Checks availability of expensive_payment gateway
        # Otherwise, retry only once with CheapPaymentGateway.
        if (21 <= self.amt <= 500) and expensive_payment_available:
            # Using Expensive Payment
            return self.expensive_payment_gateway()

        # Using Cheap Payment
        return self.cheap_payment_gateway()

    @staticmethod
    def cheap_payment_gateway() -> Tuple[bool, str]:
        return True, "Cheap Payment"

    @staticmethod
    def expensive_payment_gateway() -> Tuple[bool, str]:
        return True, "Expensive Payment"

    @staticmethod
    def premium_payment_gateway() -> Tuple[bool, str]:
        return random.sample([True, False], 1)[0], "Premium Payment"
