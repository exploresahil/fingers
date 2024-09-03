import fingerprint_enhancer
import cv2
import os

# Define input and output paths
input_path = r"C:\Users\Sahil\Downloads\Aditya Training Center Ali Madam\PARLOUR BW21\tisha lingayat 17122165\input_image.dib"
output_folder = r"C:\Users\Sahil\Downloads\Aditya Training Center Ali Madam\PARLOUR BW21\tisha lingayat 17122165\output_folder"
output_path = os.path.join(output_folder, "enhanced_image.jpeg")

# Read input image
img = cv2.imread(input_path, -1)  # Use -1 to read image as is, which includes .dib format

# Check if image is read correctly
if img is None:
    print("Error: The input image could not be read.")
else:
    # Enhance the fingerprint image
    out = fingerprint_enhancer.enhance_Fingerprint(img)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the result as JPEG
    cv2.imwrite(output_path, out)

    print(f"Enhanced image saved at: {output_path}")
