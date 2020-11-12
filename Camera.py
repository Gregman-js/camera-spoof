import cv2
import pyfakewebcam

class Camera:
    cameraSize = (640, 480)
    def __init__(self):
        self.spoof_device = pyfakewebcam.FakeWebcam('/dev/video2', self.cameraSize[0], self.cameraSize[1])
        self.camera = cv2.VideoCapture(0)
    
    def readCamera(self):
        _, img = self.camera.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
    
    def printFrame(self, img):
        img = cv2.resize(img, self.cameraSize)

        self.spoof_device.schedule_frame(img)
    