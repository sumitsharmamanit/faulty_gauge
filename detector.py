import cv2
import numpy as np
import statsmodels.api as sm
from config import *
from utils import tsplot


class detector:
    def __init__(self, video_file, flag, cropX1, cropY1, cropX2, cropY2):
        self.video = video_file
        self.filename = video_file.split("/")[-1].split(".")[0]
        self.cropX1 = cropX1
        self.cropY1 = cropY1
        self.cropX2 = cropX2
        self.cropY2 = cropY2
        self.flag = flag

    def pixel_count(self):
        # Establish capture
        cap = cv2.VideoCapture(self.video)

        # Loop through each frame
        white_pixel_count = []
        for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
            try:
                ret, frame = cap.read()
                frame = frame[self.cropX1:self.cropY1, self.cropX2:self.cropY2]
                # Gray transform
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                canny = cv2.Canny(gray, threshold1=CANNY_MIN_THRESH, threshold2=CANNY_MAX_THRESH)
                white_pixel_count.append(np.sum(canny == 255))  # checking white pixels only
            except:
                break
        return white_pixel_count

    def detect(self, ):
        series = self.pixel_count()
        tsplot(series, self.flag, self.filename)
        p_value = sm.tsa.stattools.adfuller(series)[1]
        print("p_value: ", round(p_value, 6))
        if p_value > P_THRESH:  # threshold can be set to an appropriate number based on the samples
            print('Result: Gauge is Working Fine')
            return 1
        else:
            print('Result: Faulty Gauge, needle vibration has been detected')
            return 0
