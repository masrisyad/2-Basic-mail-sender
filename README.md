# Flask Simple Mailer 📧

A lightweight web service built with Python and Flask that demonstrates how to send automated emails using the `Flask-Mail` extension and Gmail's SMTP server.

## 📌 Overview

This project sets up a local Flask server. When a user navigates to the root route (`/`), the application automatically triggers an email to a specified recipient using a pre-configured Gmail account.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed and configured:

* **Python 3.7+**
* **pip** (Python package installer)
* A **Gmail account** (You will need to generate an **App Password** since standard passwords are no longer supported for SMTP by Google).

## 🚀 Quick Setup

Follow these steps to get the application running on your local machine:

**1. Clone the repository (or create the project folder):**

```bash
mkdir flask-mailer
cd flask-mailer

```

**2. Create and activate a virtual environment (Recommended):**
Using a virtual environment isolates your project dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```

**3. Install dependencies:**
You will need both Flask and Flask-Mail to run this application.

```bash
pip install Flask Flask-Mail

```

## ⚙️ Configuration

Before running the application, you must update the script with your specific email credentials. Open the main Python file and replace the placeholder values:

```python
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
# IMPORTANT: Use a 16-character Google App Password here, NOT your actual account password.
app.config['MAIL_PASSWORD'] = 'your-16-char-app-password' 

# Update the sender and recipient inside the route
msg = Message('Halo', 
              sender='your-email@gmail.com', 
              recipients=['recipient-email@gmail.com'])

```

## 💻 Running the Application

Once configured, start the Flask development server:

```bash
python app.py

```

*(Assuming your script is named `app.py`)*

The server will start on `http://127.0.0.1:5000/`.
To trigger the email, simply open your web browser and navigate to that URL. If successful, you will see the word **"Sent"** in your browser, and the email will be delivered to the recipient's inbox.

---
