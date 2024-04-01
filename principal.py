# import reconhecimento

# print(reconhecimento.reconhecerImagem("placa.png"))
import sys # Importando ferramentas do sistema
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QLineEdit
from PyQt6.QtGui import *
import cv2
import pytesseract
import dados
import reconhecimento
app = QApplication(sys.argv)

dadosPessoas = dados.informacoes()

# def pegandoDados():
    
#     placaRecconhecida =  reconhecimento.reconhecerImagem("placa.png")
#     # print(placaRecconhecida)
    
    
#     # print(dadosPessoas)
    
#     for p in dadosPessoas.keys():
#         if p in placaRecconhecida:
#             name = dadosPessoas[p][0]
#             model = dadosPessoas[p][1]
#             anoo = dadosPessoas[p][2]
#             placaa = placaRecconhecida
    
        
#     txtUsuario.setText(str(name))
#     txtUsuario1.setText(str(model))
#     txtUsuario2.setText(str(anoo))
#     txtUsuario3.setText(str(placaa))


def abrirCamera():
    
    video = cv2.VideoCapture(0)
    while True:
    # leitura do video inserido na variavel
        sucesso, frame = video.read()
        cv2.imshow("janela", frame)

        cv2.imwrite("imagemSalva.png", frame)
        placaReconhcer = reconhecimento.reconhecerImagem("imagemSalva.png")
        
        for p in dadosPessoas.keys():
            if p in placaReconhcer:
                txtUsuario.setText(str(dadosPessoas[p][0]))
                txtUsuario1.setText(str(dadosPessoas[p][1]))
                txtUsuario2.setText(str(dadosPessoas[p][2]))
                txtUsuario3.setText(str(placaReconhcer))
        
        print(placaReconhcer)
        
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

    video.release()
    cv2.destroyAllWindows()
    
janela = QWidget()

janela.resize(800, 800) # width, heigth
janela.setWindowTitle("Login")


txtTitulo = QLabel('Reconhecimento de placa - imagem', janela)
txtTitulo.setGeometry(330, 20, 400, 100)
txtTitulo.setStyleSheet("text-align: center; text-transform: uppercase;")

image = QLabel('',janela)
image.setPixmap(QPixmap('placa.png'))
image.setGeometry(50, 90,950, 300)

nome = QLabel('Nome: ', janela)
nome.setGeometry(60, 350, 50, 100)
nome.setStyleSheet("font-size:12px")

txtUsuario = QLineEdit('', janela)
txtUsuario.setGeometry(200, 376,550, 50)
txtUsuario.setStyleSheet('border-radius:7px; background-color:#e5e5e5')
txtUsuario.setPlaceholderText("Digite seu nome")

modelo = QLabel('modelo: ', janela)
modelo.setGeometry(60, 417, 50, 100)
modelo.setStyleSheet("font-size:12px")

txtUsuario1 = QLineEdit('', janela)
txtUsuario1.setGeometry(200, 439,550, 50)
txtUsuario1.setStyleSheet('border-radius:7px; background-color:#e5e5e5')
txtUsuario1.setPlaceholderText("Digite seu nome")

ano = QLabel('ano: ', janela)
ano.setGeometry(60, 480, 50, 100)
ano.setStyleSheet("font-size:12px")

txtUsuario2 = QLineEdit('', janela)
txtUsuario2.setGeometry(200, 502,550, 50)
txtUsuario2.setStyleSheet('border-radius:7px; background-color:#e5e5e5')
txtUsuario2.setPlaceholderText("Digite seu nome")

placa = QLabel('placa: ', janela)
placa.setGeometry(60, 550, 50, 100)
placa.setStyleSheet("font-size:12px")

txtUsuario3 = QLineEdit('', janela)
txtUsuario3.setGeometry(200, 570,550, 50)
txtUsuario3.setStyleSheet('border-radius:7px; background-color:#e5e5e5')
txtUsuario3.setPlaceholderText("Digite seu nome")

btn = QPushButton('Verificar', janela)
btn.setGeometry(200, 650, 550, 50)
btn.setStyleSheet('background-color: #14213d; color: #fff; border-radius:10px; transition:0.5s; cursor: pointer;')
btn.clicked.connect(abrirCamera)


janela.show()
app.exec()