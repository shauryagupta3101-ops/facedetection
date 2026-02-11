import cv2
import cv2.data
import random
training="haarcascade_frontalface_default.xml"
file_path= cv2.data.haarcascades +"/"+training
model =cv2.CascadeClassifier(file_path)

cam= cv2. VideoCapture(0) # for external camera jitne camera  unta count increase karoge
while True:
    status, image=cam.read()
    if status == False:
        print("camers is not working ")
        break
    faces=model.detectMultiScale(image, 1.5,8)# (scale factor )1.3 for the reduction and the(minimum check  ) 5 is for the ki itni baar aagar vahi chizz aaraha h to vo sahi h 
        
    for face in faces :
        x1=face[0]
        y1=face[1]
        x2=x1+face[2]
        y2=y1+face[3]
        # b=random.randint(0,255)
        # g=random.randint(0,255)   # this line of codes are used for the  showing diffrent colours  of the box 
        # r=random.randint(0,255)
        cv2.rectangle(image,(x1,y1),(x2,y2),[0,0,255],5)
        cv2.putText(image,"face detected", (x1,y1-20), cv2.FONT_ITALIC,1,[255,255,255],2)
    cv2.imshow("camera",image)
    key = cv2.waitKey(1)
    value=ord("q")         # yaha se aapan uski assci value chack karte h 

    if key ==value:
        cv2.destroyAllWindows()
        cam.release
        break
 


