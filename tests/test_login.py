import mysql.connector

def test_direct_database_insert():
    username = "selenium_user"
    password = "pass123"

    # Connect to database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Secret5555",
        database="usersdb"
    )
    cursor = conn.cursor()

    # Simulate form insert
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

    # Now verify user was added
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    assert result is not None, f"❌ User '{username}' not found!"
    print(f"✅ User '{username}' found in database.")

    # ✅ Fetch all to avoid "unread result" error
    cursor.fetchall()
    cursor.close()
    conn.close()
