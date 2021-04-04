from uuid import uuid4

import pytest

from app.core.config import settings
from app.db.models.bill import BillTypeEnum

class TestCreateBill:

    def test_create_bill(self, client, db, payment_maker, currency_maker, usage_maker):
        payment = payment_maker()
        currency = currency_maker()
        usage = usage_maker()
        request_data = {
            "bill_type": BillTypeEnum.expense,
            "note": "test shopping",
            "price": 1000,
            "payment_id": str(payment.id),
            "usage_id": str(usage.id),
            "currency_id": str(currency.id)
        }
        response = client.post(f'{settings.api_base_path}', json=request_data)
        assert response.status_code == 201

        content = response.json()
        assert content['bill_type'] == BillTypeEnum.expense
        assert content['note'] == request_data['note']
        assert content['price'] == request_data['price']
        assert content['payment']['id'] == str(payment.id)
        assert content['usage']['id'] == str(usage.id)
        assert content['currency']['id'] == str(currency.id)

    def test_invalid_usage_id(self, client, db, payment_maker, currency_maker):
        payment = payment_maker()
        currency = currency_maker()
        request_data = {
            "bill_type": BillTypeEnum.expense,
            "note": "test shopping",
            "price": 1000,
            "payment_id": str(payment.id),
            "usage_id": str(uuid4()),
            "currency_id": str(currency.id)
        }
        response = client.post(f'{settings.api_base_path}', json=request_data)
        assert response.status_code == 500

        content = response.json()
        assert content['detail']['reason'] == 'Server error'


class TestGetBill:

    def test_get_bill(self, client, db, bill_maker):
        bill_db_obj = bill_maker()
        response = client.get(f'{settings.api_base_path}')
        assert response.status_code == 200

        content = response.json()
        assert len(content['items']) == 1

        bill = content['items'][0]
        assert bill['note'] == bill_db_obj.note
        assert bill['price'] == bill_db_obj.price
        assert bill['payment']['id']  == str(bill_db_obj.payment.id)
        assert bill['usage']['id'] == str(bill_db_obj.usage.id)
        assert bill['currency']['id'] == str(bill_db_obj.currency.id)

        assert content['pagination'] is not None
        pagination = content['pagination']
        assert pagination['total_pages'] == 1


class TestGetBillFormInfo:

    def test_get_bill_form_info(self, client, db, payment_maker, currency_maker, usage_maker):
        payment = payment_maker()
        currency = currency_maker()
        usage = usage_maker()
        response = client.get(f'{settings.api_base_path}/form-info')
        assert response.status_code == 200

        content = response.json()
        assert len(content['payment']) == 1
        assert content['payment'][0] == 'Cash'
        assert len(content['usage']) == 1
        assert content['usage'][0] == 'Shopping'
        assert len(content['currency']) == 1
        assert content['currency'][0] == 'JPY'
        assert len(content['bill_type']) == 2
        assert 'income' in content['bill_type']
        assert 'expense' in content['bill_type']


class TestGetBillSummary:

    def test_get_bill_summary(self, client, db, bill_maker, payment_maker):
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
        response = client.get(f'{settings.api_base_path}/summary')
        assert response.status_code == 200

        content = response.json()
        summary = content['summary']
        assert summary['total_expense'] == 200
        assert summary['total_income'] == 1000
        payment_detail = content['payment_detail']
        assert payment_detail[0]['name'] == 'Cash'
        assert payment_detail[0]['amount'] == 800
