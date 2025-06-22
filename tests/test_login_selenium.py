from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector

def test_login_form_submission():
    # Setup Chrome options for headless execution (no GUI)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start Chrome
    driver = webdriver.Chrome(options=options)

    try:
        # Open your Flask app in browser
        driver.get("http://localhost:5000")

        # Fill in the form
        username = "selenium_user"
        password = "selenium_pass"
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)

        # Submit the form
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Give it a moment to process
        time.sleep(2)

        # Connect to DB to verify the user exists
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Secret5555",
            database="usersdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        assert result is not None, "❌ User not found in DB after Selenium submission."
        print("✅ Selenium test passed: User found in database.")

        cursor.fetchall()
        cursor.close()
        conn.close()

    finally:
        driver.quit()

