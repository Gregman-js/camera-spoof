from Module import Module
import cv2

class Blur(Module):
    
    level = 9
    name = 'b'
    enable = True
    
    def tick(self, img):
        return cv2.GaussianBlur(img, (self.level, self.level), 0)