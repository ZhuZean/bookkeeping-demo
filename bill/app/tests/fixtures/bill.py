import pytest
from typing import Callable
from datetime import datetime

from app.db.models.currency import Currency
from app.db.models.payment import Payment
from app.db.models.usage import Usage
from app.db.models.bill import (
    BillTypeEnum,
    Bill
)
from app.core.config import settings


@pytest.fixture
def currency_maker(db):
    def factory(args={}):
        params = {
            **{
                'name': 'JPY'
            },
            **args
        }
        currency = Currency(**params)
        db.add(currency)
        db.commit()
        return currency
    return factory


@pytest.fixture
def payment_maker(db):
    def factory(args={}):
        params = {
            **{
                'name': 'Cash'
            },
            **args
        }
        payment = Payment(**params)
        db.add(payment)
        db.commit()
        return payment
    return factory


@pytest.fixture
def usage_maker(db):
    def factory(args={}):
        params = {
            **{
                'name': 'Shopping'
            },
            **args
        }
        usage = Usage(**params)
        db.add(usage)
        db.commit()
        return usage
    return factory


@pytest.fixture
def bill_maker(db, payment_maker, currency_maker, usage_maker):
    def factory(args={}):
        payment = None
        if not args.get('payment_id'):
            payment = payment_maker()
        currency = None
        if not args.get('currency_id'):
            currency = currency_maker()
        usage = None
        if not args.get('usage_id'):
            usage = usage_maker()
        params = {
            **{
                'bill_type': BillTypeEnum.expense,
                'note': 'test bill',
                'price': 800,
                'payment_id': payment.id if payment else None,
                'currency_id': currency.id if currency else None,
                'usage_id': usage.id if usage else None
            },
            **args
        }
        bill = Bill(**params)
        db.add(bill)
        db.commit()
        return bill
    return factory
