import csv

import psycopg2
from decouple import config


def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=config('DB_HOST'),
            database=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            port=5432
        )
        # print(f"Connected to database {config('DB_NAME')}")
        return conn
    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to the database: {error}")
        return None


def read_csv_generator(file_path):
    """
    Generator function to read a CSV file line by line.

    Yields:
        dict: Each row as a dictionary (header -> value).
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Reading data................")
                yield row
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading CSV: {e}")


def insert_into_books(connection, query, data):
    """
    Inserts a row into the database.
    :param data:
    :param query:
    :param connection:
    :param row:
    :return:
    """

    try:
        with connection.cursor() as cur:
            cur.execute(query, data)

    except Exception as e:
        print(f"Insert error for row {data}: {e}")
        connection.rollback()
    else:
        connection.commit()
