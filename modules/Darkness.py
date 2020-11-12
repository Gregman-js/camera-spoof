from Module import Module
import cv2

class Darkness(Module):
    
    level = -50
    name = 'd'
    enable = False
    
    def tick(self, img):
        return cv2.convertScaleAbs(img, beta=self.level)