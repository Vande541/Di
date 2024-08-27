from PIL import Image
import os
import time

def convert_image_to_webp(input_folder):
    file_names = [file_name for file_name in os.listdir(input_folder) if file_name.endswith(('jpg', 'jpeg', 'png', 'gif','heic'))]
    total_files = len(file_names)

    if total_files == 0:
        print("No image files found to process.")
        return

    for index, file_name in enumerate(file_names):
        # Xóa tệp hình ảnh
        os.remove(os.path.join(input_folder, file_name))

        # Tính toán và hiển thị tiến độ
        progress = (index + 1) / total_files * 100
        print(f"Progress: {progress:.2f}%")

# Gọi hàm với thư mục chứa hình ảnh
convert_image_to_webp('Asset')
