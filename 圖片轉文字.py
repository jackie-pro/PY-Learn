import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('IMG_5028.jpg',mode = 'r')
print(Image)
code = pytesseract.image_to_string(img)
print(code)


