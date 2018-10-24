import cv2
import numpy as np
import os
import time

import settings


def get_cv2():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imwrite('gray.jpg', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    get_cv2()
