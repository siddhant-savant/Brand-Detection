from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(1920, 7040)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size)
                resized_img.save(output_path)
                print(f"Resized: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Input and output folders
input_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\fpd"
output_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\fpd_resized_output"

# Resize images
resize_images(input_folder, output_folder)