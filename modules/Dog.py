from Module import Module
import cv2
import numpy as np
from PIL import Image
import os

class Dog(Module):
    
    name = 'dog'
    enable = False

    def setup(self):
        image = np.array( Image.open(os.path.join(os.path.dirname(__file__), "../img/doge1.jpg")) )
        self.img = cv2.resize(image, self.camera.cameraSize)
    
    def tick(self, img):
        return self.img