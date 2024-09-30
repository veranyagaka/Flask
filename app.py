from flask import Flask, render_template
app = Flask(__name__)

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
