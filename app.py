from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(10))  # admin/user

# TICKET MODEL
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    issue = db.Column(db.String(200))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_ticket():
    ticket = Ticket(name=request.form['name'], issue=request.form['issue'])
    db.session.add(ticket)
    db.session.commit()
    return redirect('/tickets')

@app.route('/tickets')
def tickets():
    data = Ticket.query.all()
    return str([(t.name, t.issue) for t in data])

# LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            session['user'] = user.username
            session['role'] = user.role
            return redirect('/')
    return '''
    <form method="post">
        <input name="username" placeholder="Username">
        <input name="password" placeholder="Password">
        <button>Login</button>
    </form>
    '''

# SIGNUP (ADMIN CAN CREATE USERS)
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            password=request.form['password'],
            role="user"
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return '''
    <form method="post">
        <input name="username">
        <input name="password">
        <button>Create User</button>
    </form>
    '''

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
