"""create_task_model

Revision ID: be2c56dbfe85
Revises: 800d4c0cf00d
Create Date: 2022-01-10 11:51:05.174345

"""
from alembic import op
import sqlalchemy as sa
from app.db.base import CustomID


# revision identifiers, used by Alembic.
revision = 'be2c56dbfe85'
down_revision = '800d4c0cf00d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'task',
        sa.Column('id', CustomID(), server_default=sa.text("concat(CAST(EXTRACT(EPOCH FROM now()) AS BIGINT),text('-'),gen_random_uuid())"), nullable=False),
        sa.Column('status', sa.Enum('created', 'in_progress', 'completed', name='taskstatus'), nullable=False),
        sa.Column('result', sa.String(length=200), nullable=True),
        sa.Column('data', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
