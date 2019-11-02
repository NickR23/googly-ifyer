import numpy as np
import face_recognition
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import path


def get_eye_poly(img):
    img = face_recognition.load_image_file(img)
    landmarks = face_recognition.face_landmarks(img)
    landmarks = landmarks[0]
    return landmarks


if __name__ == '__main__':
    danny = face_recognition.load_image_file("./assets/danny.jpg")
    landmarks = face_recognition.face_landmarks(danny)
    # print(landmarks[0]['left_eye'], landmarks[0]['right_eye'])

    landmarks = get_eye_poly("./assets/danny.jpg")

    pil_image = Image.fromarray(danny)

    d = ImageDraw.Draw(pil_image, 'RGBA')

    d.polygon(landmarks['left_eye'], fill=(150, 0, 0, 128))
    d.polygon(landmarks['right_eye'], fill=(0, 0, 150, 128))

    pil_image.save('output/danny.jpg')

# dan_image = Image.open('assets/danny.jpg')
# googly = Image.open('assets/clear_eye.png')
# googly.thumbnail((50,50), Image.ANTIALIAS)

# background = dan_image.copy()
# coords = (landmarks['left_eye'][0][0] - 25, landmarks['left_eye'][0][1] - 25)
# background.paste(googly, coords, googly)
# background.save('output/danny.jpg')
