from PIL import Image
import os
import random

def paste_small_images_on_large(large_folder, small_folder, output_folder, num_pastes=6):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    large_images = [os.path.join(large_folder, filename) for filename in os.listdir(large_folder)]
    small_images = [os.path.join(small_folder, filename) for filename in os.listdir(small_folder)]

    for large_path in large_images:
        # Open the large image
        large_image = Image.open(large_path)

        for _ in range(num_pastes):
            # Randomly select a small image
            small_path = random.choice(small_images)
            small_image = Image.open(small_path)

            # Randomly choose a position to paste the small image on the large image
            x_position = random.randint(0, large_image.width - small_image.width)
            y_position = random.randint(0, large_image.height - small_image.height)

            # Paste the small image on the large image
            large_image.paste(small_image, (x_position, y_position), small_image)

        # Save the resulting image
        output_path = os.path.join(output_folder, os.path.basename(large_path))
        large_image.save(output_path)

if __name__ == "__main__":
    large_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\full_page_snaps"
    small_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\augmented_images"
    output_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\output_images"

    paste_small_images_on_large(large_folder, small_folder, output_folder, num_pastes=6)
