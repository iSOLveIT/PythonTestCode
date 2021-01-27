from flask import Flask, request
from pydantic import ValidationError

from models import BodyModel


app = Flask("__name__")


@app.route("/", methods=["POST"])
def home():
    try:
        user_data = request.json
        validate_user_data = BodyModel(
            CreditCardNumber=user_data['CreditCardNumber'],
            CardHolder=user_data['CardHolder'],
            ExpirationDate=user_data['ExpirationDate'],
            SecurityCode=user_data['SecurityCode'],
            Amount=user_data['Amount']
        )

        print(validate_user_data)

        return {"response": "Payment is processed: 200 OK."}, 200
    except ValidationError:
        return {"response": "The request is invalid: 400 bad request."}, 400
    except:
        return {"response": "Any error: 500 internal server error"}, 500


if __name__ == '__main__':
    app.run(port=8000)
