from PIL import Image
import os

def resize_and_rotate_images(input_folder, output_folder, size=(150, 150)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        image = Image.open(input_path)

        # Resize the image
        resized_image = image.resize(size)

        # Save the resized image
        resized_image.save(output_path)

        # Horizontal flip
        horizontal_flip = resized_image.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal_flip.save(os.path.join(output_folder, f"horizontal_flip_{filename}"))


if __name__ == "__main__":
    input_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\original_product_images"
    output_folder = r"C:\Users\siddh\OneDrive\Desktop\Dissertation\brand_classification_img_dem2\test\augmented_images"

    resize_and_rotate_images(input_folder, output_folder)
