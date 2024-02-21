import argparse
import os
import datetime
from alembic.config import Config
from alembic import command

alembic_cfg_path = 'alembic.ini'

alembic_cfg = Config(alembic_cfg_path)

def make_revision(text):
    revision_message = text
    command.revision(alembic_cfg, message=revision_message, autogenerate=True)


def migrate():
    command.upgrade(alembic_cfg, 'head')

def main():
    parser = argparse.ArgumentParser(description='Database migration script.')
    subparsers = parser.add_subparsers(dest='command')

    
    revision_parser = subparsers.add_parser('make_revision', help='Run database migrations.')
    revision_parser.add_argument('text', help='The revision to migrate to.')
    migrate_parser = subparsers.add_parser('migrate', help='migrate the pending revisions')


    args = parser.parse_args()

    if args.command == 'make_revision':
        make_revision(args.text)

    if args.command == 'migrate':
        migrate()


if __name__ == '__main__':
    main()