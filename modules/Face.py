from Module import Module
import dlib
import cv2
import imutils
import math
import os
import numpy as np

class Face(Module):
    name = 'face'
    lenses = {}
    enable = False
    priority = 3
    breaks = [16, 21, 26, 30, 35, 41, 47, 59]
    alsoConnect = {
        48: [59],
        60: [67],
        36: [41],
        42: [47],
    }
    lastGood = False

    def setup(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(os.path.join(os.path.dirname(__file__), "../data/shape_predictor_68_face_landmarks.dat"))

    def tick(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = self.detector(gray)
        img = np.zeros((self.camera.cameraSize[1],self.camera.cameraSize[0],3), np.uint8)
        for face in faces:
            x1 = face.left() # left point
            y1 = face.top() # top point
            x2 = face.right() # right point
            y2 = face.bottom() # bottom point
            landmarks = self.predictor(image=gray, box=face)
            self.lastGood = landmarks

            img = self.printFace(landmarks, img)
        else:
            if self.lastGood:
                img = self.printFace(self.lastGood, img)
        return img

    def printFace(self, landmarks, img):
        for n in range(0, 67): #[0, 16, 31, 35, 24, 27]
            if n in self.breaks:
                continue
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            img = cv2.line(img, self.pointToTuple(landmarks.part(n)), self.pointToTuple(landmarks.part(n+1)), (0, 255, 0), 2)
            if n in self.alsoConnect:
                for an in self.alsoConnect[n]:
                    img = cv2.line(img, self.pointToTuple(landmarks.part(n)), self.pointToTuple(landmarks.part(an)), (0, 255, 0), 2)
        return img
    
    def pointToTuple(self, point):
        x = point.x
        y = point.y
        return (x, y)