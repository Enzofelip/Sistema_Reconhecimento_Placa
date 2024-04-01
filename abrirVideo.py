import cv2

# Puxar o video

# video = cv2.VideoCapture("video.mp4")
# puxar a camera
video = cv2.VideoCapture("video.mp4")

# loop para capturar o video 

while True:
    # leitura do video inserido na variavel
    sucesso, frame = video.read()
    cv2.imshow("janela", frame)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

video.release()
cv2.destroyAllWindows()
