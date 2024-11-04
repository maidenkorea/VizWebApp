from flask import Blueprint, render_template, Response, redirect, url_for
from segmentation import Segmentation

pages = Blueprint(__name__, 'views')
do = Segmentation()

@pages.route('/')
def home():
    return render_template('homepage.html')

@pages.route('/feed', methods=["POST", "GET"])
def feed():
    return Response(do.segmentation(), mimetype='multipart/x-mixed-replace; boundary=frame')

@pages.route('/stop', methods=["POST"])
def stop():
    do.end()
    return redirect(url_for('pages.home'))

@pages.route('videostream', methods=["POST"])
def videostream():
    return render_template('videostream.html')