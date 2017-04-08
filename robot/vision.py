import time
from pykoki import *
import cv2
import picamera
import picamera.array

def width_from_code(code):
        if code <= 27:
            return 0.25 * (10.0/12.0) #0.25 is printed width, inc. white border for wall marker?
        else:
            return 0.093 * (10.0/12.0) #for 10cm cubes?

class Vision:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1280,1024)
        self.camera.vflip = False
        self.k = PyKoki()
        self.stream = picamera.array.PiRGBArray(self.camera)
                
    def vision_see(self,(x,y),preview, preview_time):
        if self.camera.resolution != (x,y):
            self.camera.resolution = (x,y)
        self.params = CameraParams(Point2Df(x/2, y/2), Point2Df(x, y),Point2Di(x, y))         
        if preview:
            self.camera.start_preview()
            time.sleep(preview_time)
            self.camera.stop_preview()
        self.stream.seek(0)
        self.stream.truncate()    
        self.camera.capture(self.stream, format='bgr', use_video_port = True)
        self.image = self.stream.array
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.iplimage = cv2.cv.CreateImage((self.image.shape[1], self.image.shape[0]), cv2.cv.IPL_DEPTH_8U, 1)
        cv2.cv.SetData(self.iplimage, self.image.tostring(),self.image.shape[1])
        self.ipl2 = cv2.cv.CloneImage(self.iplimage)
        #find markers in image and return a list of marker objects
        self.m = self.k.find_markers_fp(self.ipl2, width_from_code, self.params) #from basic_example.py
        for element in self.m:
            if 0<=element.code<=27:
                element.marker_type = "MARKER_ARENA"
            elif 28<=element.code<=31:
                element.marker_type = "MARKER_ROBOT"
            elif 32<=element.code<=40:
                element.marker_type = "MARKER_PEDESTAL"
            elif 41<=element.code<=71:
                element.marker_type = "MARKER_TOKEN"
        return self.m

