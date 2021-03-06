"""empty message

Revision ID: 468d0564d1da
Revises: 92065c3757f1
Create Date: 2018-05-24 13:01:59.191963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '468d0564d1da'
down_revision = '92065c3757f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('nodes_parent_id_fkey', 'nodes', type_='foreignkey')
    op.drop_constraint('nodes_project_id_fkey', 'nodes', type_='foreignkey')
    op.create_foreign_key('nodes_parent_id_fkey', 'nodes', 'nodes', ['parent_id'], ['node_id'], ondelete='SET NULL')
    op.create_foreign_key('nodes_project_id_fkey', 'nodes', 'projects', ['project_id'], ['project_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("nodes_parent_id_fkey", 'nodes', type_='foreignkey')
    op.drop_constraint('nodes_project_id_fkey', 'nodes', type_='foreignkey')
    op.create_foreign_key('nodes_project_id_fkey', 'nodes', 'projects', ['project_id'], ['project_id'])
    op.create_foreign_key('nodes_parent_id_fkey', 'nodes', 'nodes', ['parent_id'], ['node_id'])
    # ### end Alembic commands ###
