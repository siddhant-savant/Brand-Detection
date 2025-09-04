from PIL import Image
import os

def augment_images(input_folder, output_folder, rotation_angles=[0, 45, 90, 135, 180, 225, 270, 315], target_size=(60, 60)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = [file for file in os.listdir(input_folder) if file.lower().endswith('.png')]

    for image_file in images:
        input_path = os.path.join(input_folder, image_file)

        # Load the original image
        with Image.open(input_path) as original_img:
            # Save the original image
            original_img.save(os.path.join(output_folder, f"original_{image_file}"), "PNG")

            # Rotate and resize the image
            for angle in rotation_angles:
                rotated_img = original_img.rotate(angle, expand=True)

                # Resize the rotated image to the target size with antialiasing
                resized_img = rotated_img.resize(target_size, resample=Image.ANTIALIAS)

                # Save the rotated and resized image
                output_path = os.path.join(output_folder, f"augmented_{angle}_{image_file}")
                resized_img.save(output_path, "PNG")

                print(f"Processed: {output_path}")

# Input and output folders
input_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\img"
output_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\img_aug"

# Rotation angles and target size
rotation_angles = [0, 45, 90, 135, 180, 225, 270, 315]
target_size = (60, 60)

# Perform image augmentation
augment_images(input_folder, output_folder, rotation_angles, target_size)
