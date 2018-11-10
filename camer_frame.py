import cv2
import numpy as np
import os

import settings


def get_cv2():
    os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
    cap = cv2.VideoCapture(settings.IP_CAMERA, cv2.CAP_FFMPEG)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        cv2.imwrite('gray.jpg', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    get_cv2()
