from ultralytics import YOLO
from math import ceil
import time
import cv2

cv2.VideoCapture()

class Segmentation:
    def __init__(self, model):
        self.model = YOLO(model)
        self.classes = list(self.model.names.values())

        self.isActive = False

        self.curr = None
        self.prev = None

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.fontScale = 1
        self.color = (255, 0, 0)
        self.thickness = 2
    

    def parse(self):
        time.sleep(2)
        self.isActive = True
        while True:
            if self.curr == self.prev:
                continue

            try:
                #_, frame = self.curr.read()
                frame = self.curr
                results = self.model(frame, stream=True)

                for r in results:
                    for box in r.boxes:
                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        org = [x1, y1]
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
                        cls = int(box.cls[0])
                        cv2.putText(frame, self.classes[cls], org, self.font, self.fontScale, self.color, self.thickness)

                _, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                  
            except:
                print('error processing frame.')

            if not self.isActive: # while loop doesnt run when isActive used as condition.
                break


    def segmentation(self, feed): #deprecated? 
        self.cap = cv2.VideoCapture(feed)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.isActive = True
        while True:
            _, frame = self.cap.read()
            results = self.model(frame, stream=True)

            for r in results:
                for box in r.boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    org = [x1, y1]
             
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # confidence = ceil((box.conf[0]*100))/100
                    # print("Confidence --->",confidence)

                    cls = int(box.cls[0])
                    # print("Class name -->", self.classes[cls])

                    cv2.putText(frame, self.classes[cls], org, self.font, self.fontScale, self.color, self.thickness)

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            if not self.isActive: # while loop doesnt run when isActive used as condition.
                break


    def end(self):
        try:
            self.cap.release()
        except:
            print('no cap to close.')
        self.isActive = False
    

    def update(self, data):
        self.prev = self.curr
        self.curr = data