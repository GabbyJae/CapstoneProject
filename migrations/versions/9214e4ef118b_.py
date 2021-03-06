"""empty message

Revision ID: 9214e4ef118b
Revises: 50f3efafc212
Create Date: 2020-07-06 15:25:45.860168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9214e4ef118b'
down_revision = '50f3efafc212'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Parking Lots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reservations_id', sa.Integer(), nullable=True),
    sa.Column('parkinglots', sa.String(length=255), nullable=True),
    sa.Column('numberofspaces', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.String(length=255), nullable=True),
    sa.Column('start_time', sa.String(length=255), nullable=True),
    sa.Column('end_date', sa.String(length=255), nullable=True),
    sa.Column('end_time', sa.String(length=255), nullable=True),
    sa.Column('licenseplateno', sa.String(length=255), nullable=True),
    sa.Column('typeofparking', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Reservations')
    op.drop_table('Parking Lots')
    # ### end Alembic commands ###
