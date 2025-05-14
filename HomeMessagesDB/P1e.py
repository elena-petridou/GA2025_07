import sys
import click
import argparse
import glob
import home_messages_db as db


@click.command()
@click.option('-d' , default = 1, help = 'DBURL insert into the project database (DBURL is a SQLAlchemy database URL)')
@click.argument('P1e-2022-12-01-2023-01-10.csv.gz[...]')
def insert_file(url,filename):
    database = db.HomeMessagesDB(f"{url}")
    try:
        database.create_db()
    except Exception as e:
        print(f"Error: {e}")
    try:
        database.insert_table_P1e(filename)
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dburl', required=True, help="Database URL")
    parser.add_argument('files', nargs='+', help="Input file(s)")
    args = parser.parse_args()

    expanded_files = []
    if not args.dburl:
        raise Exception("Database URL not provided")
        sys.exit(1)
    if not args.files:
        raise Exception("Input file(s) not provided")
        sys.exit(1)
    for pattern in args.files:
        expanded_files.extend(glob.glob(pattern))

    for file in expanded_files:
        insert_file(args.dburl, file)