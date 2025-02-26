import os
import sys
from PIL import Image

if getattr(sys, 'frozen', False):
    BASE_FOLDER = os.path.dirname(sys.executable)
else:
    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_FOLDER, "input")
OUTPUT_FOLDER = os.path.join(BASE_FOLDER, "output")

def convert_png_to_webp(input_folder, output_folder):
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            with Image.open(input_path) as img:
                img.save(output_path, 'WEBP')
                print(f"Converted: {filename} -> {output_path}")

if __name__ == "__main__":
    print(f"Input Folder: {INPUT_FOLDER}")
    print(f"Output Folder: {OUTPUT_FOLDER}")
    convert_png_to_webp(INPUT_FOLDER, OUTPUT_FOLDER)
    print("Conversion complete! Check the output folder.")
    input("Press Enter to exit...")