import face_recognition
from PIL import Image, ImageDraw


def get_eye_poly(img):
    lm = face_recognition.face_landmarks(img)
    lm = lm[0]
    return lm


def get_highlighted_eyes(img_path):
    image = face_recognition.load_image_file(img_path)
    lm = get_eye_poly(image)
    pil_img = Image.fromarray(image)
    d = ImageDraw.Draw(pil_img, 'RGBA')
    d.polygon(lm['left_eye'], fill=(150, 0, 0, 128))
    d.polygon(lm['right_eye'], fill=(0, 0, 150, 128))
    return pil_img


if __name__ == '__main__':
    scary_danny = get_highlighted_eyes('./assets/danny.jpg')
    scary_danny.save('./output/danny.jpg')
