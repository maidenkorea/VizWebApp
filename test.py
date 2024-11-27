import cv2

async def display_incoming_video(src):
    cap = cv2.VideoCapture(src)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        _, frame = cap.read()
        cv2.imshow('Stream', frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    cap.release()
    return