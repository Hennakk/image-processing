import cv2
import RPi.GPIO as GPIO

greenLed = 16
blueLed = 20
redLed = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenLed,GPIO.OUT)
GPIO.setup(blueLed,GPIO.OUT)
GPIO.setup(redLed,GPIO.OUT)

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,320)
    camera.set(4,240)
        
    while(1):
        _, frame = camera.read()  

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = (100,100,120)
        upper_blue = (150,255,255)
        
        lower_green = (50, 150, 50)
        upper_green = (80, 255, 255)
        
        lower_red = (150, 50, 50)
        upper_red = (180, 255, 255)
                
        redMask = cv2.inRange(hsv, lower_red, upper_red)   
        greenMask = cv2.inRange(hsv, lower_green, upper_green)  
        blueMask = cv2.inRange(hsv, lower_blue, upper_blue)  

        redPixels = cv2.countNonZero(redMask)
        greenPixels = cv2.countNonZero(greenMask)
        bluePixels = cv2.countNonZero(blueMask)
        
        #print(redPixels,greenPixels,bluePixels)
        
        colorList = [redPixels,greenPixels,bluePixels]
        maxValue = max(colorList)
        maxPos = colorList.index(maxValue)
        print( maxValue, maxPos)
        
        if maxValue >= 500:
            if maxPos == 0: #red
                print("red on")
                GPIO.output(greenLed, 0)
                GPIO.output(blueLed, 0)
                GPIO.output(redLed, 1)
            elif maxPos == 1: #green
                print("green")
                GPIO.output(greenLed, 1)
                GPIO.output(blueLed, 0)
                GPIO.output(redLed, 0)
            elif maxPos == 2: #blue
                print("blue")
                GPIO.output(greenLed, 0)
                GPIO.output(blueLed, 1)
                GPIO.output(redLed, 0)
        else:
            GPIO.output(greenLed, 0)
            GPIO.output(blueLed, 0)
            GPIO.output(redLed, 0)
            
        cv2.imshow('frame',frame)
                 
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    GPIO.cleanup()

if __name__ == '__main__':
    main()


