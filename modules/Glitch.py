from Module import Module
import cv2
from glitch_this import ImageGlitcher
from PIL import Image
import numpy as np

class Glitch(Module):
    
    level = 4
    changeColor = False
    name = 'g'
    enable = False

    def setup(self):
        self.glitcher = ImageGlitcher()
    
    def tick(self, img):
        img = Image.fromarray(img)
        img = self.glitcher.glitch_image(img, self.level, color_offset=self.changeColor)
        img = np.asarray(img)
        return img