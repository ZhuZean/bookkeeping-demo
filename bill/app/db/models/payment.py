""" Declarative model for Payment
"""

from enum import Enum
import datetime
import uuid

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from app.db.models import base_model


class Payment(base_model.BASE):
    """ Model Payment
    """
    __tablename__ = 'payment'
    id = sa.Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    name = sa.Column(sa.String, nullable=False, index=True)
    created_at = sa.Column(
        sa.DateTime(timezone=True), nullable=True, default=datetime.datetime.utcnow
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True), nullable=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
