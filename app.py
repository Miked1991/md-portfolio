from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def display_home():
  return render_template('index.html')

@app.route("/work.html")
def display_work():
  return render_template('work.html')

@app.route("/services.html")
def display_service():
  return render_template('services.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)