import requests
from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 20)
    year = date.today().year
    return render_template("index.html", num=random_number, currentyear=year)

@app.route('/guess/<name>')
def guess(name):
    url = f'https://api.genderize.io?name={name}'
    reponse = requests.get(url)
    if reponse.status_code == 200:
        data = reponse.json()
        gender = data.get('gender')
        return render_template("guess.html", sex = gender, username = name)
    else:
        return render_template("guess.html", sex = "not found", username = "not found")

@app.route('/blog/<number>')
def blog(number):
    print(number)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug= True)
