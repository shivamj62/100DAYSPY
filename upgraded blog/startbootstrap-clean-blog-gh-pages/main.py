from flask import Flask, render_template, request
import requests
import smtplib
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()
OWN_EMAIL = "shivam.jaiswal6204@gmail.com"
OWN_PASSWORD = "urzf jovp rgdt jhxb"
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        email_message = f"Subject:New Form\n\nName : {name}\neMail : {email}\nTelephone Number : {phone}\nMessage : \n{message}\n"
        try:
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
                connection.starttls()
                connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
                connection.sendmail(from_addr=OWN_EMAIL, to_addrs="shivamthecyborg@gmail.com",
                                    msg=email_message)
            logging.info("Email sent successfully.")
            return render_template("contact.html", msg_sent=True)
        except (smtplib.SMTPException, ConnectionError, TimeoutError) as e:
            logging.error(f"Failed to send email: {e}")
            print(f"error yeh hai: {e}")
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
