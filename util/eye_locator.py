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


def get_poly_center(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    center = (sum(x) / len(points), sum(y) / len(points))
    center = [round(x) for x in center]
    return center


def get_pasted_eyes(img_path):
    image = face_recognition.load_image_file(img_path)
    lm = get_eye_poly(image)

    face_img = Image.fromarray(image)

    left_eye_position = get_poly_center(lm['left_eye'])
    left_eye_img = Image.open('./assets/clear_eye.png', 'r')
    left_eye_img.thumbnail((50, 50), Image.ANTIALIAS)
    left_eye_position = (left_eye_position[0] - 25, left_eye_position[1] - 25)
    face_img.paste(left_eye_img, left_eye_position, left_eye_img)

    right_eye_position = get_poly_center(lm['right_eye'])
    right_eye_img = Image.open('./assets/clear_eye.png', 'r')
    right_eye_img.thumbnail((50, 50), Image.ANTIALIAS)
    right_eye_position = (right_eye_position[0] - 25, right_eye_position[1] - 25)
    face_img.paste(right_eye_img, right_eye_position, right_eye_img)

    return face_img


if __name__ == '__main__':
    # scary_danny = get_highlighted_eyes('./assets/frank.jpg')
    # scary_danny.save('./output/frank.jpg')
    pasted_eye_img = get_pasted_eyes('./assets/frank.jpg')
    pasted_eye_img.save('output/pasted.png')
