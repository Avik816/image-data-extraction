# Code authored by Avik Chakraborty

# Importing the necessary libraries.
from pytesseract import pytesseract
from PIL import Image

# Defining the paths to tesseract executable.
tesseractPATH = 'C:/Program Files (x86)/Tesseract/tesseract.exe'

# Starting a tesseract instance.
pytesseract.tesseract_cmd = tesseractPATH

# Opening the image from the directory.
# In this case the directory is the working directory.
image = Image.open('image.png')

# Extracting text from the image.
# The image is passed to the function and then the texts in the image are extracted.
extractedText = pytesseract.image_to_string(image = image)
print(extractedText)

# Saving the texts in the file.
with open(file = 'extracted texts.txt', mode = 'w', encoding = 'UTF-8') as file:
    file.write(extractedText)
    file.close()

print('Extracted text are written into the file.')
print('File saved to working directory !')