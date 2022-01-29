from flask import Flask, redirect, url_for, render_template, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "your password"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False,unique = True)
    password = db.Column(db.String(80), nullable = False)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/iphone")
def iphone():
    return render_template("iphone.html")


@app.route("/additem", methods=['GET','POST'])
@login_required
def additem():
    return render_template('additem.html')

@app.route("/additem/phone", methods=['GET','POST'])
@login_required
def addphone():
    return render_template('addphone.html')

@app.route("/register",  methods=['GET','POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        session["user"] = form.username.data
        user = User(username = form.username.data, password = generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form = form)


@app.route("/login",  methods=['GET','POST'])
def login():
    login_form = LoginForm(csrf_enabled = False)
    if "user" in session:
        redirect(url_for("home"))
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username_login.data).first()
        if user:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user)
                return redirect(url_for('home'))
                flash('Logged in Succsesfully')
                session['user'] = login_form.username_login.data
            elif check_password_hash(user.password, login_form.password.data) == None:
                flash('Wrong password!')
    return render_template("login.html", login_form = login_form)


@app.route("/logout", methods=['GET', "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
