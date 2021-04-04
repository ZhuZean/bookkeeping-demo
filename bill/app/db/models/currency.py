""" Declarative model for Currency
"""

from enum import Enum
import datetime
import uuid

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from app.db.models import base_model


class Currency(base_model.BASE):
    """ Model Currency
    """
    __tablename__ = 'currency'
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
