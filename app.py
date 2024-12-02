from flask import Flask, render_template, Response, redirect, url_for
from flask_socketio import SocketIO
from segmentation import Segmentation


app = Flask(__name__)
socketio = SocketIO(app)
model = Segmentation('best.pt')


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/stop', methods=["POST"])
def stop():
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

@socketio.on('frame')
def frame(data):
    print('frame recieved.')
    result = model.parse(data)
    socketio.emit('result', result)

@socketio.on_error_default
def default_error_handler(e):
    print("Error: {}".format(e))
    socketio.stop()


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000)