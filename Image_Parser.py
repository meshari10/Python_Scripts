import sys
import pytesseract
from PIL import Image

# Check that two arguments were provided
if len(sys.argv) != 3:
    print('Usage: python Image_Parser.py <input_image> <output_file>')
    sys.exit(1)

# Open image and convert to grayscale
image = Image.open(sys.argv[1])
image = image.convert('L')

# Extract text from image
text = pytesseract.image_to_string(image)

# Save text to file
with open(sys.argv[2], 'w') as f:
    f.write(text)
