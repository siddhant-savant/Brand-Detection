import os
from PIL import Image

def resize_images_in_directory(input_dir, output_dir, new_size=(720, 720)):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Iterate through each file in the input directory
        for filename in os.listdir(input_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)

                # Open the image file
                with Image.open(input_path) as img:
                    # Resize the image
                    resized_img = img.resize(new_size)

                    # Save the resized image
                    resized_img.save(output_path)

                    print(f"Image '{filename}' resized and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_directory = r'C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_test\images to be resized'
output_directory = r'C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_test\resized_boots'
resize_images_in_directory(input_directory, output_directory)
