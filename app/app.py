from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            # Connect to MySQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Secret5555",
                database="usersdb"
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return "User added successfully!"
        except Exception as e:
            return f"Error: {e}"

    return render_template("login.html")


if __name__ == "__main__":
    # Run on 0.0.0.0 so it's accessible in Codespaces
    app.run(debug=True, host="0.0.0.0", port=5000)
