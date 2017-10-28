from flask import Flask
from AlphaBot2 import AlphaBot2
app = Flask(__name__)

@app.route("/forward/")
def forward():
	return "forward!"
	Ab.forward()

@app.route("/backward/")
def backward():
	return "backward!"
	Ab.backward()

@app.route("/stop/")
def stop():
	return "stop!"
	Ab.stop()

@app.route("/left/")
def left():
    return "left!"
    Ab.left()

@app.route("/right/")
def right():
    return "right!"
    Ab.right()

@app.route("/camera/")
def camera():
    return send_file("/dev/video0", mimetype='image/png')
