import  cv2
import pytesseract

def reconhecerImagem(imagem):
    pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Professor\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    # Inserir uma imagem em um avariavel compativel
    placaCarro = cv2.imread(imagem, 0)
    
    # imagemPreto = cv2.cvtColor(placaCarro, cv2.COLOR_BGR2GRAY)
    
    # BUscar os caracteres contidos na imagem, inserindo em uma variavel
    img = pytesseract.image_to_string(placaCarro, config="-l eng --oem 3 --psm 12")   
    return img


 

