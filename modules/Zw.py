from Module import Module
import cv2
import numpy as np
from PIL import Image

class Zw(Module):
    
    name = 'zw'
    enable = False

    def setup(self):
        image = np.array( Image.open("img/zw.jpg") )
        self.img = cv2.resize(image, self.camera.cameraSize)
    
    def tick(self, img):
        return self.img