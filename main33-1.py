import cv2

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,640)
    camera.set(4,480)
    
    xml = '/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(xml)
        
    while( camera.isOpened() ):
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.05, 5)
        print("faces detected Number: " + str(len(faces)))

        if len(faces):
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            
        cv2.imshow('result', image)
        
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


