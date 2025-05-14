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
        print(f"Connected to database {config('DB_NAME')}")
        return conn
    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to the database: {error}")
        return None
