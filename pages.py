from flask import Blueprint, render_template, Response

pages = Blueprint(__name__, 'views')

@pages.route('/')
def home():
    return render_template('homepage.html')

@pages.route('/feed')
def feed():
    return Response()