from alembic import op
import sqlalchemy as sa


"""
This file defines the initial database schema for the AI Powered Request Handler System MVP. 

The database is based on the PostgreSQL database, and this migration creates the necessary tables for storing user data, requests, and responses. 

Important Notes:
- This file is intended to be used with Alembic for managing database migrations.
- It adheres to the MVP's coding standards and best practices.
- Ensure this migration file integrates seamlessly with the existing MVP codebase.
- This migration only creates the initial schema. Future migrations will be needed to add or modify tables as the MVP evolves.
"""

# Define the tables
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

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
    op.drop_table('requests')
    op.drop_table('users')