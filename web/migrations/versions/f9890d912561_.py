"""empty message

Revision ID: f9890d912561
Revises: 
Create Date: 2018-06-01 03:08:08.754054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9890d912561'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=12), nullable=True),
    sa.Column('update_dttm', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('create_dttm', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('status', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_token', sa.String(length=100), nullable=True),
    sa.Column('session_id', sa.String(length=100), nullable=True),
    sa.Column('expiration_ttm', sa.DateTime(timezone=True), nullable=True),
    sa.Column('update_dttm', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('create_dttm', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('status', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=10), nullable=True),
    sa.Column('password', sa.String(length=500), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(length=50), nullable=True),
    sa.Column('update_dttm', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('create_dttm', sa.DateTime(timezone=True), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('status', sa.String(length=1), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('user_login')
    op.drop_table('role')
    # ### end Alembic commands ###
