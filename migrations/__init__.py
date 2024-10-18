from alembic import op
import sqlalchemy as sa


"""
This file initializes the Alembic migration system for the AI Powered Request Handler System MVP. 

It sets up the migration environment and enables the management of database schema changes. 

Important Notes:
- This file is intended to be used with Alembic for managing database migrations.
- It adheres to the MVP's coding standards and best practices.
- Ensure this migration file integrates seamlessly with the existing MVP codebase.
- This migration only creates the initial schema. Future migrations will be needed to add or modify tables as the MVP evolves.
"""

# Define the tables
def upgrade():
    # Create the `users` table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

    # Create the `requests` table
    op.create_table(
        'requests',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('response', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    # Drop the `requests` table
    op.drop_table('requests')
    # Drop the `users` table
    op.drop_table('users')