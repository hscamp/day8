# imports
from flask import Flask, render_template
 
# run the app
app = Flask(__name__)
 
# route for domain
@app.route("/")
# route function (get)
def hello():
	return render_template('index.html')
    # return "Hello World!"

# route for 404
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# main (runs python file)
if __name__ == "__main__":
    app.run()