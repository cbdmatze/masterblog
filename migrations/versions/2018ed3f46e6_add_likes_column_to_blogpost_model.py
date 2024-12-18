"""Add likes column to BlogPost model

Revision ID: 2018ed3f46e6
Revises: 
Create Date: 2024-12-05 19:00:16.499021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2018ed3f46e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog_post', schema=None) as batch_op:
        batch_op.drop_column('likes')

    # ### end Alembic commands ###
