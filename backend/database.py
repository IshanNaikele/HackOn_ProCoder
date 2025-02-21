import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="geography_game",
            user="your_username",   # Replace with your PostgreSQL username
            password="your_password",  # Replace with your PostgreSQL password
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

def create_table():
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS quiz (
                id SERIAL PRIMARY KEY,
                question TEXT NOT NULL,
                option1 TEXT NOT NULL,
                option2 TEXT NOT NULL,
                option3 TEXT NOT NULL,
                option4 TEXT NOT NULL,
                answer TEXT NOT NULL,
                difficulty INT DEFAULT 1
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("Table created successfully!")

# Run this function to create the table when the script is executed
if __name__ == "__main__":
    create_table()
