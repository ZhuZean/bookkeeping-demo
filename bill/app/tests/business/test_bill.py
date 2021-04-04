from unittest.mock import Mock
from datetime import datetime
import uuid
import json

import pytest

from app.api.endpoints import bad_request, business_error
from app.helper.paginator import Paginator
from app.business.bill import BillBusiness
from app.db.models.bill import BillTypeEnum
from app.schemas.bill import CreateBillRequest


class TestCreateBill():

    def test_normal_flow(self, db, payment_maker, currency_maker, usage_maker):
        payment = payment_maker()
        currency = currency_maker()
        usage = usage_maker()

        bill_business = BillBusiness()
        params = CreateBillRequest(**{
            "bill_type": BillTypeEnum.expense,
            "note": "test shopping",
            "price": 1000,
            "payment_id": str(payment.id),
            "usage_id": str(usage.id),
            "currency_id": str(currency.id)
        })
        result = bill_business.create(db=db,  params=params)

        assert result is not None
        assert result.id is not None
        assert result.bill_type == BillTypeEnum.expense
        assert result.note == "test shopping"
        assert result.price == 1000
        assert result.payment.id == payment.id
        assert result.usage.id == usage.id
        assert result.currency.id == currency.id


class TestGetBill():

    def test_normal_flow(self, db, bill_maker):
        bill_db_obj = bill_maker()

        bill_business = BillBusiness()
        paginator = Paginator(5, 1)
        items = bill_business.get_bills(db=db, paginator=paginator)

        assert len(items) == 1
        bill = items[0]
        assert bill.bill_type == bill_db_obj.bill_type


class TestGetBillFormInfo():

    def test_normal_flow(self, db, payment_maker, currency_maker, usage_maker):
        payment = payment_maker()
        currency = currency_maker()
        usage = usage_maker()

        bill_business = BillBusiness()
        result = bill_business.get_form_info(db=db)

        assert result['currency'][0] == currency.name
        assert result['payment'][0] == payment.name
        assert result['usage'][0] == usage.name
        assert BillTypeEnum.income in result['bill_type']
        assert BillTypeEnum.expense in result['bill_type']


class TestGetBillFormInfo():

    def test_normal_flow(self, db, payment_maker, currency_maker, usage_maker):
        payment = payment_maker()
        currency = currency_maker()
        usage = usage_maker()

        bill_business = BillBusiness()
        result = bill_business.get_form_info(db=db)

        assert result['currency'][0] == currency.name
        assert result['payment'][0] == payment.name
        assert result['usage'][0] == usage.name
        assert BillTypeEnum.income in result['bill_type']
        assert BillTypeEnum.expense in result['bill_type']


class TestGetBillSummary():

    def test_normal_flow(self, db, bill_maker, payment_maker):
        payment = payment_maker()
        bill_expense = bill_maker({
            'bill_type' : BillTypeEnum.expense,
            'price': 200,
            'payment_id': payment.id
        })
        bill_income = bill_maker({
            'bill_type' : BillTypeEnum.income,
            'price': 1000,
            'payment_id': payment.id
        })

        bill_business = BillBusiness()
        result = bill_business.get_summary(db=db)

        summary = result['summary']
        assert summary['total_expense'] == 200
        assert summary['total_income'] == 1000
        payment_detail = result['payment_detail']
        assert payment_detail[0]['name'] == 'Cash'
        assert payment_detail[0]['amount'] == 800
