from utils import connect_to_db, insert_into_books, read_csv_generator


def main():
    pass
    # connect_to_db()


def fetch_data():
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM  LIMIT 10;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except Exception as e:
        print(f"Error fetching data: {e}")
    finally:
        conn.close()


def load_book_data(file_path):
    query = """
            INSERT INTO books (title, language, price, genre)
            VALUES (%s, %s, %s, %s) \
            """

    conn = connect_to_db()
    if conn is None:
        return
    try:
        for row in read_csv_generator(file_path):
            data = (row['Title'], row['Language'], row['Price'], row['Genre'])
            insert_into_books(conn, query, data)
        conn.commit()
        print("Books data inserted successfully.")
    except Exception as e:
        print(f"Error during data load: {e}")
        conn.rollback()
    finally:
        conn.close()

def load_customers_data(file_path):
    query = """
            INSERT INTO customers(
	 customername, email, preferredlanguage, loyaltypoints, membershiplevel)
	VALUES ( %s, %s, %s, %s, %s)\
            """

    conn = connect_to_db()
    if conn is None:
        return
    try:
        for row in read_csv_generator(file_path):
            data = (row['CustomerName'], row['Email'], row['PreferredLanguage'], row['LoyaltyPoints'], row['MembershipLevel'])
            insert_into_books(conn, query, data)
        conn.commit()
        print("Customers data inserted successfully.")
    except Exception as e:
        print(f"Error during data load: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    # books_data = './data/books.csv'
    # load_book_data(books_data)

    customers_data = './data/customers.csv'
    load_customers_data(customers_data)
