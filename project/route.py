# Local modules

# User-defined modules
from project import app
from .models import BodyModel
from .payment_providers import ProcessPayment

# Third-party modules
from flask import request
from pydantic import ValidationError


@app.route("/", methods=["POST"])
def home():
    """
    The “ProcessPayment” method that receives a request consisting of:
        CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, and Amount
    :return: Payment is processed: 200 OK or
    The request is invalid: 400 bad request or
    Any error: 500 internal server error
    """
    try:
        user_data = request.json
        validate_user_data = BodyModel(
            CreditCardNumber=user_data['CreditCardNumber'],
            CardHolder=user_data['CardHolder'],
            ExpirationDate=user_data['ExpirationDate'],
            SecurityCode=user_data['SecurityCode'],
            Amount=user_data['Amount']
        )

        # Process payment
        payment_processing = ProcessPayment(validate_user_data.Amount).select_payment_provider()
        if payment_processing[0] is False:
            return {"response": "Payment is not processed: 200 OK."}, 200
        return {"response": "Payment is processed: 200 OK."}, 200
    except ValidationError:
        return {"response": "The request is invalid: 400 bad request."}, 400
    except:
        return {"response": "Any error: 500 internal server error"}, 500
