# Web UI Automation Framework — PyTest + Selenium (POM)

A UI test automation framework built with **Python, Selenium, PyTest, and Page Object Model (POM)** design pattern.  
This project automates multiple practice web pages including forms, autocomplete, scrolling, and input validation.
Web Page: https://practice.expandtesting.com/
---

## 🚀 Tech Stack

- Python 3.x
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- PyTest HTML Report
- ChromeDriver

---

## 📂 Project Structure

project-root/
│

├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ ├── autocomplete_page.py
│ ├── radio_buttons_page.py
│ └── infinite_scroll_page.py
│

├── tests/
│ ├── test_login.py
│ ├── test_autocomplete.py
│ ├── test_radio_buttons.py
│ └── test_infinite_scroll.py
│
├── conftest.py
├── requirements.txt
└── README.md
✅Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
✅Install dependencies
pip install -r requirements.txt
✅Install ChromeDriver

Download ChromeDriver matching your Chrome version and add it to PATH.

▶️ Run Tests

Run all tests:
pytest -v

Run specific test file:

pytest tests/test_dropdowns.py -v

📊 Generate HTML Report
pytest -v --html=report.html --self-contained-html
Open report.html in browser after execution.

/screenshots/

🧠 Design Pattern Used
Page Object Model (POM)

Benefits:
Reusable page methods
Clean separation of test logic
Easier maintenance
Scalable test structure

✅ Example Test Flow
Open page
Fill form fields
Select dropdown values
Submit form
Validate result

👩‍💻 Author

Simi Chakma
QA & Automation Learner
Python • Selenium • PyTest


