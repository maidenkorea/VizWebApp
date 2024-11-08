from flask import Flask, render_template, Response, redirect, url_for
from flask_socketio import SocketIO
from segmentation import Segmentation


app = Flask(__name__)
socketio = SocketIO(app)
do = Segmentation('yolov8m-seg.pt')
source = 0 # source for video feed. 


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/feed', methods=["POST", "GET"])
def feed():
    return Response(do.segmentation(source), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop', methods=["POST"])
def stop():
    do.end()
    return redirect(url_for('home'))

@app.route('/videostream', methods=["POST"])
def videostream():
    return render_template('videostream.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000)