from flask import Flask
from art import aprint, art
import face_recognition
from util.eye_locator import get_eye_poly

app = Flask(__name__)


@app.route('/')
def home():
    message = art('butterfly') + " " + art("woman") \
          + " Butterfly may the boogie be with you " \
          + art('butterfly') \
          + " " + art("woman")
    return message


@app.route('/features')
def features():
    image = face_recognition.load_image_file('./assets/danny.jpg')
    return get_eye_poly(image)


if __name__ == '__main__':
    app.run(debug=True)
