import cv2

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,640)
    camera.set(4,480)
        
    while(1):
        _, frame = camera.read()
        
        qrDecoder = cv2.QRCodeDetector()
        data,bbox,recti = qrDecoder.detectAndDecode(frame)
        
        cv2.imshow('qrcode test',frame)
        print(data)
                 
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
