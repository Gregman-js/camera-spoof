from Module import Module
import cv2

class Resizer(Module):
    
    level = 4
    name = 's'
    enable = True
    
    def tick(self, img):
        return cv2.resize(img, tuple(map(lambda a: a//self.level, self.camera.cameraSize)))