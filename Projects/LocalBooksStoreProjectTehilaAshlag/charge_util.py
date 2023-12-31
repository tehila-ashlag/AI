import stripe


# "testPublishableKey":"pk_test_51ORE0EHN2LabDtUKllfrS5uq1On0urT9sUvzmUnCtmi7kDhEMcDJ4ypMI1OSvHHtOp871jskFVSrGrlxqmudoWtN009vza6zRL",
testSecretKey="sk_test_51ORE0EHN2LabDtUKen1G9KKBJzm57P12FmQNtOBc1LfaUMbPvJZ6T5AJBQn6fFiylAEx07piAWXK4B39SeJvSQfh00sM1LX4TO"


# Set your test API keys
stripe.api_key = testSecretKey

def chargeCustomer(dollarAmount):
# Create a test charge
    chargeDone=False
    try:
        charge = stripe.Charge.create(
            amount=int(dollarAmount*100),  # Amount in cents (e.g., $20.00)
            currency="usd",
            source="tok_visa",  # Use a test card token (e.g., tok_visa)
            description="Test charge",
        )

        # charge object contains the response from stripe saved above in obj for future uses--
        chargeDone=True
    except stripe.error.StripeError as e:
        # If there's an error, print the error message
        print("Error:", str(e))
    return chargeDone