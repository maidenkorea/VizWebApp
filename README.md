# Viz - Sidewalk Image Segmentation
## YOLOv8 Image Segmentation Deployed with Flask
Viz is a simple implementation of a custom tuned YOLOv8 instance segmentation model, trained on our own annotated datasets. The goal of this project is to assist visually impaired pedestrians with navigating campus sidewalks. This project:
* implements customed trained model weights.
* integrates an AI image segmentation model to a front-end web app.
* is hosted via a Flask web-server.

Viz was primarily developed as a learning opportunity.
## Upcoming Features
This app is still in development, and some of the features we are still working on implementing are:
 1. text-to-speech alerts.
 2. clearer video feedback and annotation.
 3. instanced user sessions.
## Quick-Start Guide
Here are some brief instructions to get you started on running this project locally. If you encounter any issues during this process, please feel free to reach out so I can improve these instructions!
#### 1. Make sure Python is installed
Open your terminal or command prompt and enter `python`. It should return something like `Python 3.12.7`, if it does not, you can check out the guides here for [Windows](https://docs.python.org/3/using/windows.html) and [Mac](https://docs.python.org/3/using/mac.html).
Press `ctrl+c` to exit Python if it is already installed.
#### 2. Clone the repo locally
To clone the repo, navigate to your desired directory in your terminal using:
```
cd C:\Your\Project\Directory\Path
``` 
and then entering:
```
git clone https://github.com/maidenkorea/VizWebApp.git
```
If you do not have git installed, go ahead and follow [this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) guide.
#### 3. Create a Python virtual environment
Ensure you are still in the project directory, and enter:
```
python -m venv .venv
```
If this fails, you can try:
```
python3 -m venv .venv
```
Now activate your virtual environment:

Windows:
```
.venv\Scripts\activate
```
Mac/Linux:
```
source .venv/bin/activate
```
#### 4. Install project requirements
To install the requirements within your virtual environment, enter:
```
pip install -r requirements.txt
```
#### 5. Run the web server locally
After ensuring you are still within your virtual environment, run the following command:
```
python app.py
```
#### 6. Access the web server
Navigate to `http://127.0.0.1:8000` in your browser, and enjoy!
If this address does not work, make sure it matches the address output by the Python script.
## Usage Guidelines
As this project was primarily developed as a learning opportunity, I encourage you to clone and rename this project to suit your needs! 

Our model is a tuned version of Ultralytics' YOLOv8 image segmentation model. The documentation for YOLO can be found [here](https://docs.ultralytics.com/reference/cfg/__init__/).

When training the model, we used [RoboFlow](https://roboflow.com) to manage the datasets, and [Google Colab](https://colab.research.google.com) to train.

We use OpenCV for the camera. Here's the [documentation](https://docs.opencv.org/4.x/index.html).

For front-end styling, we use Bootstrap, and you can find that documentation [here](https://getbootstrap.com/docs/5.3/getting-started/introduction/).

And we use Flask for the back-end, for which you can find the documentation [here](https://flask.palletsprojects.com/en/stable/).

With these tools, you can use our app as a guideline for your very own, or make something entirely new! Happy building!
