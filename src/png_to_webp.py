import os
import sys
from PIL import Image

if getattr(sys, 'frozen', False):
    BASE_FOLDER = os.path.dirname(sys.executable)
else:
    BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_FOLDER, "input")
OUTPUT_FOLDER = os.path.join(BASE_FOLDER, "output")

def convert_png_to_webp(input_folder, output_folder, quality):
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            with Image.open(input_path) as img:
                img.save(output_path, 'WEBP', quality=quality)
                print(f"Converted: {filename} -> {output_path} (Quality: {quality})")

if __name__ == "__main__":
    print(f"Input Folder: {INPUT_FOLDER}")
    print(f"Output Folder: {OUTPUT_FOLDER}")
    
    while True:
        try:
            quality = int(input("Enter WebP quality (0-100, higher is better): ").strip())
            if 0 <= quality <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    convert_png_to_webp(INPUT_FOLDER, OUTPUT_FOLDER, quality)
    print("Conversion complete! Check the output folder.")
    input("Press Enter to exit...")
