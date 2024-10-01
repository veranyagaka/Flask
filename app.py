from flask import Flask, render_template
# wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# sqlalchemy
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	def __repr__(self):
		return f"User('{self.name}')"
class MyForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	submit = SubmitField('Submit')
@app.route('/add_user/<name>')
def add_user(name):
	user = User(name=name)
	db.session.add(user)
	db.session.commit()
	return f"User {name} added"
@app.route('/users')
def users():
    users = User.query.all()
    return str(users)

@app.route('/form', methods=['GET', 'POST'])
def form():
	form = MyForm()
	if form.validate_on_submit():
		name = form.name.data
		return f"Hello {name}"
	return render_template('form.html', form=form)
@app.route('/')
def home():
	return "Hello Flask"

@app.route('/about')
def about():
	return 'About Page'

@app.route('/contact')
def contact():
	return render_template('contact.html') # needs to be in templates folder

if __name__ == '__main__':
	app.run(debug=True)

'''
from app import db, app

# Use parentheses to call app_context()
with app.app_context():  
    db.create_all()  # Create all tables

python

sqlite3 mydatabase.db
.tables
'''
