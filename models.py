from datetime import datetime
from pydantic import BaseModel, constr, PositiveFloat, StrictStr, validator
from credit_card_checker import CreditCardChecker


class BodyModel(BaseModel):
    CreditCardNumber: constr(min_length=13, max_length=16, strict=True)
    CardHolder: StrictStr
    ExpirationDate: datetime
    SecurityCode: constr(regex=r"^\d{3}?$") = None
    Amount: PositiveFloat

    @validator('CreditCardNumber')
    def check_credit_card_validity(cls, v):
        card_number = v.replace(" ", "")
        credit_card_validity = CreditCardChecker(card_number).valid()
        if credit_card_validity is False:
            raise ValueError('Number should be a valid credit card number.')
        return v

    @validator('ExpirationDate')
    def expire_date_cannot_be_past(cls, v):
        expire_date = datetime.fromisoformat(str(v))
        if datetime.now() > expire_date:
            raise ValueError('Expiration date cannot be in the past.')
        return v
