from ultralytics import YOLO
import cv2

class Segmentation:
    def __init__(self):
        self.isActive = False

        self.model = YOLO("yolov8m-seg.pt")
        self.yolo_classes = list(self.model.names.values())
        self.classes_ids = [self.yolo_classes.index(clas) for clas in self.yolo_classes]


    def segmentation(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.isActive = True
        while True:
            _, frame = self.cap.read()
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            if not self.isActive:
                break


    def end(self):
        self.cap.release()
        self.isActive = False