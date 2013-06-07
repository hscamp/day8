# imports
from flask import Flask, render_template
 
# run the app
app = Flask(__name__)
 
# route for domain
@app.route("/")
# route function (get)
def hello():
	return render_template('index.html')

# route for menu
@app.route("/menu/", methods=['GET', 'POST'])
def menu():
	print "here!"
	return render_template('menu.html')

# route for contact us
@app.route("/contact/", methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

# route for 404
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# main (runs python file)
if __name__ == "__main__":
    app.run()