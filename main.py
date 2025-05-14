from utils import connect_to_db

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

if __name__ == "__main__":
    main()