import os
from PIL import Image

def is_image_valid(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()  # Kiểm tra ảnh có bị lỗi không
        return True
    except (IOError, SyntaxError) as e:
        return False

def remove_invalid_images(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            if not is_image_valid(file_path):
                print(f"Xóa ảnh lỗi: {file_path}")
                os.remove(file_path)

remove_invalid_images('Asset')
