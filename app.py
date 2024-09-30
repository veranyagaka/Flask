from flask import Flask, render_template
# wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sk'
class MyForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	submit = SubmitField('Submit')

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
