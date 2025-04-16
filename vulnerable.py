# credit score loan approval
import sqlite3
from flask import Flask, request, render_template_string
 
app = Flask(__name__)
 
# Database setup
def setup_database():
    conn = sqlite3.connect("loans.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, credit_score INTEGER, loan_status TEXT)")
    c.execute("INSERT INTO users (name, credit_score, loan_status) VALUES ('Alice', 750, 'Approved'), ('Bob', 600, 'Rejected')")
    conn.commit()
    conn.close()
 
# Vulnerable: Credit scoring based on user-provided ID
@app.route('/credit_score', methods=['GET'])
def credit_score():
    user_id = request.args.get('id')  # User input directly included in the query
    conn = sqlite3.connect("loans.db")
    c = conn.cursor()
 
    # Vulnerable to SQL Injection
    query = f"SELECT name, credit_score FROM users WHERE id = {user_id}"
    c.execute(query)
    result = c.fetchone()
 
    conn.close()
 
    if result:
        return f"User: {result[0]}, Credit Score: {result[1]}"
    else:
        return "User not found."
 
# Vulnerable: Loan approval based on credit score
@app.route('/loan_approval', methods=['POST'])
def loan_approval():
    name = request.form.get('name')  # User input directly included in the query
    credit_score = request.form.get('credit_score')
 
    conn = sqlite3.connect("loans.db")
    c = conn.cursor()
 
    # Vulnerable to SQL Injection
    query = f"INSERT INTO users (name, credit_score, loan_status) VALUES ('{name}', {credit_score}, 'Pending')"
    c.execute(query)
    conn.commit()
 
    conn.close()
    return f"Loan application submitted for {name} with a credit score of {credit_score}."
 
# Vulnerable: Display loan approval feedback with XSS
@app.route('/loan_feedback', methods=['POST'])
def loan_feedback():
    feedback = request.form.get('feedback')  # User input directly rendered in HTML
 
    # Vulnerable to XSS
    html = f"<h1>Loan Feedback:</h1><p>{feedback}</p>"
    return render_template_string(html)
 
if __name__ == '__main__':
    setup_database()
    app.run(debug=True)