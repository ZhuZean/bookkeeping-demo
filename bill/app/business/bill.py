""" Bill business
"""
from uuid import UUID

from sqlalchemy.orm import Session

from app.crud.bill import bill as crud_bill
from app.db.models.bill import Bill as BillOrm, BillTypeEnum
from app.db.models.currency import Currency as CurrencyOrm
from app.db.models.payment import Payment as PaymentOrm
from app.db.models.usage import Usage as UsageOrm
from app.schemas.bill import CreateBillRequest
from app.helper.paginator import Paginator


class BillBusiness():

    def create(self, params: CreateBillRequest, db: Session=None):
        bill = crud_bill.create(db=db, obj_in=params)

        return bill

    def get_bills(self, paginator: Paginator, db: Session=None):
        bill_query = crud_bill.get_list(db=db)

        return paginator.get_page(bill_query)

    def get_form_info(self, db: Session=None):
        bill_query = crud_bill.get_list(db=db)
        result = {
            'currency': self._get_all_currency_name(db),
            'payment': self._get_all_payment_name(db),
            'usage': self._get_all_usage_name(db),
            'bill_type': self._get_all_bill_type(),
        }

        return result

    def _get_all_currency_name(self, db: Session) -> list:
        currency_query = db.query(CurrencyOrm)
        all_currency = currency_query.order_by(CurrencyOrm.updated_at).all()

        return [currency.name for currency in all_currency]

    def _get_all_payment_name(self, db: Session) -> list:
        payment_query = db.query(PaymentOrm)
        all_payment = payment_query.order_by(PaymentOrm.updated_at).all()

        return [payment.name for payment in all_payment]

    def _get_all_usage_name(self, db: Session) -> list:
        usage_query = db.query(UsageOrm)
        all_usage = usage_query.order_by(UsageOrm.updated_at).all()

        return [usage.name for usage in all_usage]

    def _get_all_bill_type(self) -> list:
        return [bill_type.value for bill_type in BillTypeEnum]

    def get_summary(self, db: Session=None):
        payment_detail = self._get_payment_details(db)
        result = {
            'summary': self._get_summary(db),
            'payment_detail': self._get_payment_details(db)
        }
        return result

    def _get_summary(self, db: Session=None) -> dict:
        result = {
            'total_expense': 0,
            'total_income': 0
        }
        bill_queryset = db.query(
            BillOrm
        ).order_by(
            'created_at'
        ).all()

        for bill_obj in bill_queryset:
            if (bill_obj.bill_type == BillTypeEnum.expense):
                result['total_expense'] += bill_obj.price
            if (bill_obj.bill_type == BillTypeEnum.income):
                result['total_income'] += bill_obj.price
        return result

    def _get_payment_details(self, db) -> list:
        payment_queryset = db.query(
            PaymentOrm
        ).order_by(
            'created_at'
        ).all()

        payment_detail = []
        for payment_obj in payment_queryset:
            detail = {
                'name': payment_obj.name,
                'amount': self._get_payment_summary(db, payment_obj)
            }
            payment_detail.append(detail)

        return payment_detail

    def _get_payment_summary(self, db, payment) -> int:
        amount = 0

        bill_queryset = db.query(
            BillOrm
        ).filter(
            BillOrm.payment_id==payment.id
        ).order_by(
            'created_at'
        ).all()

        for bill_obj in bill_queryset:
            if (bill_obj.bill_type == BillTypeEnum.expense):
                amount -= bill_obj.price
            if (bill_obj.bill_type == BillTypeEnum.income):
                amount += bill_obj.price

        return amount
