import cv2
import cv2.data# traning file ko lane ke liye
import os 
#this line only help us for the finding of files 
# print(os .listdir(cv2.data. haarcascades))
img= cv2.imread("WhatsApp Image 2025-03-30 at 14.23.56_9409d061.jpg")# image read ho  rahi h isme 
# img= cv2.resize(img(500,600))                                       # isme size maintain kar raha h 
training="haarcascade_frontalface_default.xml"
file_path= cv2.data.haarcascades +"/"+training
model =cv2.CascadeClassifier(file_path)
faces=model. detectMultiScale(img, 1.3,5)# (scale factor )1.3 for the reduction and the(minimum check  ) 5 is for the ki itni baar aagar vahi chizz aaraha h to vo sahi h 
print(faces)

for face in faces :
    x1=face[0]
    y1=face[1]
    x2=x1+face[2]
    y2=y1+face[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),[45,125,5],5)# phele imge ka naam , coordinates,( bgr) colour ,thickness 
cv2.imshow("dont'know", img)
cv2.waitKey(0)
cv2.destrotyAllwindows()