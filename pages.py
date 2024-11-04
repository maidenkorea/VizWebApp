from flask import Blueprint, render_template, Response
from segmentation import segmentation

pages = Blueprint(__name__, 'views')

@pages.route('/')
def home():
    return render_template('homepage.html')

@pages.route('/feed', methods=["POST"])
def feed():
    return Response(segmentation(), mimetype='multipart/x-mixed-replace; boundary=frame')

@pages.route('/stop', methods=["POST"])
def stop():
    
    return render_template('homepage.html')