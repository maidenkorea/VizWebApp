from flask import Flask, render_template, Response, redirect, url_for
from flask_socketio import SocketIO
from segmentation import Segmentation


app = Flask(__name__)
socketio = SocketIO(app)
model = Segmentation('yolov8m-seg.pt')
source = 0 # source for video feed. 


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/feed', methods=["POST", "GET"])
def feed():
    return Response(model.segmentation(source), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop', methods=["POST"])
def stop():
    model.end()
    return redirect(url_for('home'))

@app.route('/session', methods=["POST"])
def session():
    return render_template('session.html')


@socketio.on('connect')
def connect():
    print('connected')

@socketio.on('disconnect')
def disconnect():
    print('disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000)