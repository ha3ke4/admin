from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<font color="green"><h1>Hello, World!</h1></font>"
  
if __name__ == "__main__":
  app.run()
