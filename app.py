from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

tickets = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_ticket():
    name = request.form['name']
    issue = request.form['issue']

    tickets.append({'name': name, 'issue': issue})
    return redirect('/tickets')

@app.route('/tickets')
def view_tickets():
    return render_template('tickets.html', tickets=tickets)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
