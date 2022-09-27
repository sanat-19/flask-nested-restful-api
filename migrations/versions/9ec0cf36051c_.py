"""empty message

Revision ID: 9ec0cf36051c
Revises: 
Create Date: 2022-09-25 12:47:25.866014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ec0cf36051c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('website', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=20), nullable=True),
    sa.Column('suite', sa.String(length=20), nullable=True),
    sa.Column('city', sa.String(length=20), nullable=True),
    sa.Column('zipcode', sa.String(length=20), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('catchPhrase', sa.String(length=20), nullable=True),
    sa.Column('bs', sa.String(length=20), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('geos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lat', sa.String(length=20), nullable=True),
    sa.Column('lng', sa.String(length=20), nullable=True),
    sa.Column('address', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('geos')
    op.drop_table('companies')
    op.drop_table('addresses')
    op.drop_table('users')
    # ### end Alembic commands ###
