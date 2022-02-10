from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
 
@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/Go")
def Go():
    GPIO.output(14, GPIO.HIGH)
    return "LED on"

@app.route("/Left")
def Left():
    GPIO.output(15, GPIO.HIGH)
    return "LED on"

@app.route("/Right")
def Right():
    GPIO.output(18, GPIO.HIGH)
    return "LED on"

@app.route("/Back")
def Back():
    GPIO.output(26, GPIO.HIGH)
    return "LED on"

@app.route("/Stop")
def Stop():
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    return "LED off"



if __name__ == "__main__":  
   app.run(host="192.168.0.9", port = "8080")
