"""empty message

Revision ID: e4e692e4558d
Revises: 
Create Date: 2020-02-22 10:35:41.798765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4e692e4558d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=True),
    sa.Column('last_name', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('monthly_income', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expenses',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('user_id', 'category_id')
    )
    op.create_table('todos',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('is_done', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('user_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_table('expenses')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
