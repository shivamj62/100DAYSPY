from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Guess a number between 0 and 9</h1> 
    <br> 
    <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWF1Z3l0YXZxaHo0ODZueXRhb29hOWJwdGh3Z2RqdWpqcnpkeGZsbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiIzHVN2qgNO7onJe/giphy.gif'/>
    """

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return """
        <h1 style='color:purple'>Too Low, Try Again</h1>
        <iframe src='https://giphy.com/embed/TgmiJ4AZ3HSiIqpOj6' width='480' height='271' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>
        <p><a href='https://giphy.com/gifs/gsimedia-bruh-thats-low-bro-TgmiJ4AZ3HSiIqpOj6'>via GIPHY</a></p>
        """
    elif guess > random_number:
        return """
        <h1 style='color:red'>Highest in the room, Try Again</h1>
        <iframe src='https://giphy.com/embed/wHB67Zkr63UP7RWJsj' width='480' height='336' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>
        <p><a href='https://giphy.com/gifs/wHB67Zkr63UP7RWJsj'>via GIPHY</a></p>
        """
    else:
        return """
        <h1 style='color:green'>Perfect</h1>
        <iframe src='https://giphy.com/embed/eYbM7glc0EWEnv0cFA' width='480' height='271' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>
        <p><a href='https://giphy.com/gifs/RelentlessRecords-bbcc-bad-boy-chiller-crew-gk-eYbM7glc0EWEnv0cFA'>via GIPHY</a></p>
        """

if __name__ == "__main__":
    app.run(debug=True)
