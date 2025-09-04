import os
import shutil
import random

def create_image_copies(input_folder, output_folder, total_copies):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all images in the input folder
    images = [file for file in os.listdir(input_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Ensure that the output folder is initially empty
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    # Randomly select images and create copies until the desired total_copies is reached
    while total_copies > 0:
        random_image = random.choice(images)
        source_path = os.path.join(input_folder, random_image)
        copy_path = os.path.join(output_folder, f"copy_{total_copies}_{random_image}")
        shutil.copyfile(source_path, copy_path)
        print(f"Created copy: {copy_path}")
        total_copies -= 1

# Input and output folders
input_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\fpd_resized_output"
output_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\fpd_copies_output"

# Total number of copies needed
total_copies = 200

# Create image copies
create_image_copies(input_folder, output_folder, total_copies)
