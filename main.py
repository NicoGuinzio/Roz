import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta de la carpeta con las imágenes
ruta_carpeta = r"C:\Users\NicolasG\Desktop\PYTHON IA\photos"

# Obtener la lista de archivos en la carpeta
lista_archivos = os.listdir(ruta_carpeta)



# Iterar en todos los archivos de la carpeta
for archivo in lista_archivos:
    # Comprobar si el archivo es una imagen
    if archivo.endswith('.png') or archivo.endswith('.jpg') or archivo.endswith('.jpeg') or archivo.endswith('.bmp'):
        # Cargar la imagen
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        image = Image.open(ruta_archivo)

        # Reconocer el texto
        text = pytesseract.image_to_string(image, lang='eng')

        # Imprimir el texto reconocido
        print(f'Texto en {archivo}:')
        print(text)
