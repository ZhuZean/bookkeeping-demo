"""generate tables

Revision ID: 29d0412899dd
Revises: 
Create Date: 2021-04-02 23:12:52.917825

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '29d0412899dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_currency_name'), 'currency', ['name'], unique=False)
    op.create_table('payment',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payment_name'), 'payment', ['name'], unique=False)
    op.create_table('usage',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usage_name'), 'usage', ['name'], unique=False)
    op.create_table('bill',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bill_type', sa.String(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('payment_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('usage_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('currency_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], ),
    sa.ForeignKeyConstraint(['usage_id'], ['usage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bill_currency_id'), 'bill', ['currency_id'], unique=False)
    op.create_index(op.f('ix_bill_payment_id'), 'bill', ['payment_id'], unique=False)
    op.create_index(op.f('ix_bill_usage_id'), 'bill', ['usage_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bill_usage_id'), table_name='bill')
    op.drop_index(op.f('ix_bill_payment_id'), table_name='bill')
    op.drop_index(op.f('ix_bill_currency_id'), table_name='bill')
    op.drop_table('bill')
    op.drop_index(op.f('ix_usage_name'), table_name='usage')
    op.drop_table('usage')
    op.drop_index(op.f('ix_payment_name'), table_name='payment')
    op.drop_table('payment')
    op.drop_index(op.f('ix_currency_name'), table_name='currency')
    op.drop_table('currency')
    # ### end Alembic commands ###
