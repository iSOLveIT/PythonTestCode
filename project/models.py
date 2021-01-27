# Local modules
from datetime import date

# User-defined modules

# Third-party modules
from pydantic import BaseModel, constr, PositiveFloat, validator
from credit_card_checker import CreditCardChecker


class BodyModel(BaseModel):
    """
    CreditCardNumber: The length is between 13 and 16 and is mandatory.
    CardHolder: The string has to be an alphabetic string and is mandatory
    ExpirationDate: Is a datetime object and is mandatory
    SecurityCode: Is a string with exactly 3 digits but optional
    Amount: Is a positive float number and is mandatory
    """
    CreditCardNumber: constr(min_length=13, max_length=16, strict=True)
    CardHolder: constr(regex=r"^[A-Za-z\-]+ ??[A-Za-z\-]+$")
    ExpirationDate: date
    SecurityCode: constr(regex=r"^\d{3}?$") = None
    Amount: PositiveFloat

    @validator('CreditCardNumber')
    def check_credit_card_validity(cls, v):
        """
        Checks the validity of the credit card number
        :param v: The field value to validate
        :return: Field value or Raise Value Error
        """
        card_number = v.replace(" ", "")
        credit_card_validity = CreditCardChecker(card_number).valid()
        if credit_card_validity is False:
            raise ValueError('Number should be a valid credit card number.')
        return v

    @validator('ExpirationDate')
    def expire_date_cannot_be_past(cls, v):
        """
        Checks if expiration date is past
        :param v: The field value to validate
        :return: Field value or Raise Value Error
        """
        expire_date = date.fromisoformat(str(v))
        if date.today() > expire_date:
            raise ValueError('Expiration date cannot be in the past.')
        return v
