from ultralytics import YOLO
from math import ceil
import cv2

class Segmentation:
    def __init__(self):
        self.isActive = False

        self.model = YOLO("yolov8m-seg.pt")
        self.classes = list(self.model.names.values())
        #self.classes_ids = [self.yolo_classes.index(clas) for clas in self.yolo_classes]


    def segmentation(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.isActive = True
        while True:
            _, frame = self.cap.read()
            results = self.model(frame, stream=True)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    # bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                    # put box in cam
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # confidence
                    confidence = ceil((box.conf[0]*100))/100
                    print("Confidence --->",confidence)

                    # class name
                    cls = int(box.cls[0])
                    print("Class name -->", self.classes[cls])

                    # object details
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2

                    cv2.putText(frame, self.classes[cls], org, font, fontScale, color, thickness)

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            if not self.isActive:
                break


    def end(self):
        self.cap.release()
        self.isActive = False