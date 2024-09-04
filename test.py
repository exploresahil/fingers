import cv2
import fingerprint_enhancer
from glob import glob

# Example usage:
# img = cv2.imread(
#     '/home/parag/fingers/uploads/WhatsApp Image 2024-09-03 at 16.14.29_2e8fe93c (1) (1).jpg', cv2.IMREAD_GRAYSCALE)
# enhanced_img = fingerprint_enhancer.enhance_Fingerprint(img)


# Use list comprehension to match multiple extensions
files = glob('./**/*.jpg', recursive=True) + \
    glob('./**/*.png', recursive=True) + \
    glob('./**/*.jpeg', recursive=True)

# Print the list of files
print(files)

# cv2.('Original', img)
# cv2.imshow('Enhanced', enhanced_img)
# cv2.imwrite("ss.jpg", enhanced_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
