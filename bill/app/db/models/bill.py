""" Declarative model for Bill
"""

from enum import Enum
import datetime
import uuid

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from app.db.models import base_model
from app.db.models.payment import Payment
from app.db.models.usage import Usage
from app.db.models.currency import Currency


class BillTypeEnum(str, Enum):
    income = 'income'
    expense = 'expense'


class Bill(base_model.BASE):
    """ Model Bill
    """
    __tablename__ = 'bill'
    id = sa.Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    bill_type = sa.Column(sa.String, nullable=False)
    note = sa.Column(sa.Text, nullable=True)
    price = sa.Column(sa.Numeric(asdecimal=True), nullable=False)

    payment_id = sa.Column(postgresql.UUID(as_uuid=True), sa.ForeignKey('payment.id'), nullable=False, index=True)
    payment = relationship('Payment')

    usage_id = sa.Column(postgresql.UUID(as_uuid=True), sa.ForeignKey('usage.id'), nullable=False, index=True)
    usage = relationship('Usage')

    currency_id = sa.Column(postgresql.UUID(as_uuid=True), sa.ForeignKey('currency.id'), nullable=False, index=True)
    currency = relationship('Currency')

    created_at = sa.Column(
        sa.DateTime(timezone=True), nullable=True, default=datetime.datetime.utcnow
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True), nullable=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
