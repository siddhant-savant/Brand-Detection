from PIL import Image
import os
import random

def paste_images(class_folders, large_image_folder, output_folder, num_small_images_per_large=5, num_output_images=500):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of large images
    large_images = [f for f in os.listdir(large_image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # Make sure we don't exceed the number of available large images
    num_output_images = min(num_output_images, len(large_images))

    for i in range(num_output_images):
        # Randomly select a large image
        large_image_name = large_images[i % len(large_images)]
        large_image_path = os.path.join(large_image_folder, large_image_name)
        large_image = Image.open(large_image_path)

        # Iterate over class folders and randomly select small images
        for class_folder in class_folders:
            small_images = [f for f in os.listdir(class_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
            selected_small_images = random.sample(small_images, min(num_small_images_per_large, len(small_images)))

            for small_image_name in selected_small_images:
                # Open the small image
                small_image_path = os.path.join(class_folder, small_image_name)
                small_image = Image.open(small_image_path)

                # Generate random position to paste the smaller image
                paste_position = (random.randint(0, large_image.width - small_image.width),
                                  random.randint(0, large_image.height - small_image.height))

                # Paste the smaller image onto the larger image
                large_image.paste(small_image, paste_position, small_image)

        # Save the result
        output_path = os.path.join(output_folder, f"result_{i}_{large_image_name}")
        large_image.save(output_path)

    print("Image pasting completed.")

if __name__ == "__main__":
    class_folders = [
        r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem1\armani_my_way_floral",
        r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem1\dior_miss_dior",
        r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem1\lancome_la_vie_est_belle",
        r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem1\prada_paradoxe",
        r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem1\ysl_black_opium",
    ]

    large_image_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\1_fpd"
    output_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\output_folder"

    paste_images(class_folders, large_image_folder, output_folder, num_output_images=500)
