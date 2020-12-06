from Module import Module
import cv2

class Blur(Module):
    
    level = 3
    name = 'b'
    enable = True
    priority = 99
    
    def tick(self, img):
        return cv2.GaussianBlur(img, (self.level, self.level), 0)