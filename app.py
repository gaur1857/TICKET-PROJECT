from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

# fake database
users = []
tickets = []

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = {
            "id": len(users) + 1,
            "username": request.form['username'],
            "password": request.form['password']
        }
        users.append(user)
        return redirect('/login')
    return render_template('signup.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        for user in users:
            if user['username'] == request.form['username'] and user['password'] == request.form['password']:
                session['user_id'] = user['id']
                return redirect('/')
    return render_template('login.html')

# Add Ticket
@app.route('/add', methods=['POST'])
def add_ticket():
    if 'user_id' not in session:
        return redirect('/login')

    ticket = {
        "name": request.form['name'],
        "issue": request.form['issue'],
        "user_id": session['user_id']
    }
    tickets.append(ticket)

    return redirect('/tickets')

# Show only user's tickets
@app.route('/tickets')
def view_tickets():
    if 'user_id' not in session:
        return redirect('/login')

    user_tickets = [t for t in tickets if t['user_id'] == session['user_id']]

    return render_template('tickets.html', tickets=user_tickets)

app.run(debug=True)
