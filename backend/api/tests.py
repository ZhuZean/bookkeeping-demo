from django.test import TestCase
from api.models import Payment, Usage, Currency, Bill



class ApiModelTestCase(TestCase):
    def setUp(self):
        payment_obj = Payment.objects.create(name="payment_1")
        usage_obj = Usage.objects.create(name="usage_1")
        currency_obj = Currency.objects.create(name="currency_1")
        payment_obj_1 = Bill.objects.create(
            usage=usage_obj,
            payment=payment_obj,
            currency=currency_obj,
            bill_type="IN",
            price=1000,
            note="test note"
        )
        payment_obj_2 = Bill.objects.create(
            usage=usage_obj,
            payment=payment_obj,
            currency=currency_obj,
            bill_type="EX",
            price=500,
            note="shopping"
        )
