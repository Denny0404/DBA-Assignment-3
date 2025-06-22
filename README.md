
# 📘 Assignment 3 – Web App with MySQL & Selenium Automation

## 👨‍🎓 Student Info
- **Name:** Denish Akbari
- **Course:** PROG8850 – Database Automation
- **Instructor:** [Your Instructor Name]
- **Date:** June 21, 2025

---

## 🚀 Project Overview

This project demonstrates a complete web application with:
- A user-friendly login form built using **Flask**
- Integration with a **MySQL database** to store credentials
- Automated testing using **Selenium**
- GitHub Actions for CI/CD to deploy and test the database setup

---

## 🧰 Tech Stack

| Component        | Technology          |
|------------------|---------------------|
| Frontend         | HTML + CSS (login.html, success.html) |
| Backend          | Python Flask        |
| Database         | MySQL               |
| Testing          | Selenium + Pytest   |
| CI/CD            | GitHub Actions      |
| Infrastructure   | Ansible, Devcontainer (Codespaces) |

---

## 🗂 Project Structure

```
DBA-Assignment-3/
├── app/
│   ├── app.py                  # Flask app logic
│   └── templates/
│       ├── login.html          # Login form UI
│       └── success.html        # Success screen after login
├── tests/
│   ├── test_login.py           # Direct DB insert test
│   └── test_login_selenium.py  # Selenium end-to-end test
├── db/
│   └── init.sql                # MySQL schema for 'users' table
├── .github/workflows/
│   └── mysql_action.yml        # GitHub Actions workflow
├── up.yml / down.yml           # Optional Ansible playbooks
├── devcontainer.json           # Codespaces development environment
├── requirements.txt            # All Python dependencies
└── README.md                   # Run instructions and documentation
```

---

## 🛠 Setup & Run Instructions

### ✅ Step 1: Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ Step 2: Install Chrome & Chromedriver

```bash
sudo apt update
sudo apt install -y wget unzip xvfb libxi6 libgconf-2-4 libnss3 libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

# Install compatible Chromedriver
CHROME_VERSION=$(google-chrome --version | grep -oP '[0-9.]+' | head -1 | cut -d '.' -f 1)
wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION -O chromedriver_version
CHROMEDRIVER_VERSION=$(cat chromedriver_version)
wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv chromedriver /usr/local/bin/
```

---

### ✅ Step 3: Start MySQL (Ansible method)

```bash
ansible-playbook up.yml
```

---

### ✅ Step 4: Initialize the database

```bash
mysql -u root -h 127.0.0.1 -p < db/init.sql
```

---

### ✅ Step 5: Run the Flask web app

```bash
python app/app.py
```

Visit the app at `http://localhost:5000`  
Enter username/password and click Submit.

---

### ✅ Step 6: Run Selenium test

```bash
pytest tests/test_login_selenium.py
```

Expected:
```
✅ Selenium test passed: User found in database.
```

---

## 🤖 GitHub Actions

The CI workflow automatically:
- Starts a MySQL container
- Installs MySQL client
- Applies schema from `schema_changes.sql`
- Runs on every `push`

Check logs in: **GitHub → Actions tab → mysql_action.yml**

---

## ✅ Features Summary

- [x] Flask app with styled login UI
- [x] User data stored in MySQL
- [x] Direct DB test (insert + verify)
- [x] Selenium automation for login
- [x] GitHub Actions CI/CD
- [x] Success screen with username
- [x] Fully working in Codespaces

---

## 📸 Screenshots (see Word report)
- Login Form
- Success Page
- DB Table Output
- Selenium Passed Output
- GitHub Actions Green Run

---

## 📦 Submission Includes

- ✅ `README.md` (this file)
- ✅ `Assignment_3_Report_Denish_Akbari.docx`
- ✅ All source code and tests
- ✅ GitHub CI/CD integration

---

## 📚 References

- Flask Docs: https://flask.palletsprojects.com/
- MySQL Docs: https://dev.mysql.com/doc/
- Selenium Docs: https://www.selenium.dev/documentation/
- GitHub Actions: https://docs.github.com/actions

---








# PROG8850Week1Installation
install mysql, python

```bash
ansible-playbook up.yml
```

To use mysql:

```bash
mysql -u root -h 127.0.0.1 -p
```

To run github actions like (notice that the environment variables default for the local case):

```yaml
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Install MySQL client
        run: sudo apt-get update && sudo apt-get install -y mysql-client

      - name: Deploy to Database
        env:
          DB_HOST: ${{ secrets.DB_HOST || '127.0.0.1' }} 
          DB_USER: ${{ secrets.DB_ADMIN_USER || 'root' }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD  || 'Secret5555'}}
          DB_NAME: ${{ secrets.DB_NAME || 'mysql' }}
        run: mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME < schema_changes.sql
```

locally:

first try

```bash
bin/act
```

then if that doesn't work 

```bash
bin/act -P ubuntu-latest=-self-hosted
```

to run in the codespace.

To shut down:

```bash
ansible-playbook down.yml
```

This is a reproducible mysql setup
