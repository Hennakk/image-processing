import cv2
import time

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,640)
    camera.set(4,480)
        
    while(1):
        _, frame = camera.read()
        
        qrDecoder = cv2.QRCodeDetector()
        data,bbox,recti = qrDecoder.detectAndDecode(frame)
        
        cv2.imshow('qrcode test',frame)
        #print(data)
        lastline =""
        if recti is not None:
            try:
                with open('qrcode.txt', 'r') as f:
                    lastline = f.readlines()[-1]
            except:
                print("no file")
            
            print(data,lastline)
                
            if data in lastline:
                print("same data")
                
            else:
                print("save data")
                f = open('qrcode.txt','a')
                f.write(data + '\r\n')
                f.close()
                time.sleep(3.0)
                
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


