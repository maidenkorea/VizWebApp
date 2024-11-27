from flask import Flask, render_template, Response, redirect, url_for
from flask_socketio import SocketIO
from segmentation import Segmentation
import test as t


app = Flask(__name__)
socketio = SocketIO(app)
model = Segmentation('yolov8m-seg.pt')
source = 0 # source for video feed. 
user_connected = False


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/feed', methods=["POST", "GET"])
def feed():
    return Response(model.parse(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop', methods=["POST"])
def stop():
    model.end()
    return redirect(url_for('home'))

@app.route('/session', methods=["POST"])
def session():
    return render_template('session.html')

@app.route('/test', methods=["POST", "GET"])
def test():
    #t.display_incoming_video()
    return render_template('test.html')


@socketio.on('connect')
def connect():
    if user_connected:
        pass
    print('connected')

@socketio.on('disconnect')
def disconnect():
    print('disconnected')

@socketio.on('frame')
def frame(data):
    print('frame rec.')
    model.update(data)

@socketio.on_error_default
def default_error_handler(e):
    print("Error: {}".format(e))
    socketio.stop()


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000)