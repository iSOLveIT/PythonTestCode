## ProcessPayment API
The API receives a request
like this
- CreditCardNumber (mandatory, string, it should be a valid credit card number)
- CardHolder: (mandatory, string)
- ExpirationDate (mandatory, DateTime, it cannot be in the past)
- SecurityCode (optional, string, 3 digits)
- Amount (mandatory decimal, positive amount)

The response of this method should be 1 of the following based on
- Payment is processed: 200 OK
- The request is invalid: 400 bad request
- Any error: 500 internal server error

The API uses Pydantic for data validation.
Test Cases can be found in `test` folder

### Author
* __Duodu Randy :octocat:__

### Date Created
* _Wednesday, 27th January 2021_
