from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World, Welcome to the world of Python's Flask!"
	
if __name__ == "__main__":
	app.run()