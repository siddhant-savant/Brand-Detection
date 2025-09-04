import os
from PIL import Image

def resize_images(input_directory, output_directory, target_size):
    """
    Resize all images in the input directory and save them to the output directory.

    Parameters:
    - input_directory (str): Path to the directory containing input images.
    - output_directory (str): Path to the directory to save resized images.
    - target_size (tuple): Target size in the format (width, height).
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over each file in the input directory
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)
        
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(target_size, 3)  # Use integer value for Image.ANTIALIAS

            # Save the resized image to the output directory
            output_path = os.path.join(output_directory, filename)
            resized_img.save(output_path)

# Example usage
input_directory = r'C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_exposure_validation_dataset\img_resize'
output_directory = r'C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_exposure_validation_dataset\img_resized'
target_size = (768, 768)

resize_images(input_directory, output_directory, target_size)
