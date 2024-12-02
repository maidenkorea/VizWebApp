from ultralytics import YOLO
import numpy as np
import base64
import cv2

cv2.VideoCapture()

class Segmentation:
    def __init__(self, model):
        self.model = YOLO(model)
        self.classes = list(self.model.names.values())

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.fontScale = 1
        self.color = (255, 0, 0)
        self.thickness = 2
    

    def parse(self, data):
        print('calling parse...')
        frame = self.readb64(data)

        try:
            #_, frame = self.curr.read()
            print('processing frame...')
            results = self.model(frame, stream=True, verbose=False)

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

            return (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                  
        except:
            print('error processing frame.')


    def end(self):
        try:
            self.cap.release()
        except:
            print('no cap to close.')
        self.isActive = False

    
    def readb64(self, uri):
        encoded_data = uri.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img