from PIL import Image
import sys

THUMB_SIZE = (320, 180)  # thumbnail size (16:9)

def crop_to_16_9(img):
    w, h = img.size
    target_ratio = 16 / 9
    current_ratio = w / h

    if current_ratio > target_ratio:
        # image too wide -> crop width
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        right = left + new_w
        top = 0
        bottom = h
    else:
        # image too tall -> crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        bottom = top + new_h
        left = 0
        right = w

    return img.crop((left, top, right, bottom))


def create_thumbnail(input_path, output_path):
    img = Image.open(input_path)

    img = crop_to_16_9(img)

    img = img.resize(THUMB_SIZE, Image.LANCZOS)

    img.save(output_path, "PNG")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_thumbnail.py input.png output.png")
        sys.exit(1)

    create_thumbnail(sys.argv[1], sys.argv[2])