from PIL import Image
import os

def convert_png_to_jpg(input_folder, output_folder, target_resolution=(800, 600), quality=85):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            # Open the PNG image
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Resize to the target resolution
            img = img.resize(target_resolution, Image.LANCZOS)

            # Convert to RGB (if necessary)
            img = img.convert('RGB')

            # Save as JPEG with the same filename
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
            try:
                img.save(output_path, format='JPEG', quality=quality)
                print(f"Converted {filename} to {os.path.basename(output_path)}")
            except Exception as e:
                print(f"Error saving {filename}: {e}")





# Usage example
input_folder = 'C:/uelordi01.github.io/AIimagenes'
output_folder = 'C:/uelordi01.github.io/out_images'
target_resolution = (600, 650)  # Change to your desired resolution
convert_png_to_jpg(input_folder, output_folder, target_resolution)
