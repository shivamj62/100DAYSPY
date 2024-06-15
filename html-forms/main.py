from flask import Flask,  render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def recieve_data():
    error = None
    if request.method == 'POST':
        return render_template("login.html", user_username=request.form['username'], user_password=request.form['password'])
    else:
        error = "pata nahi kya hua"
        render_template("login.html", user_error = error)

if __name__ == "__main__":
    app.run(debug=True)