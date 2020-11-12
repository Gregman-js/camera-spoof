from Module import Module
import dlib
import cv2
import imutils
import math

class Lens(Module):
    name = 'len'
    lenses = {}
    enable = True
    priority = 2
    printDots = False

    def setup(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("data/shape_predictor_68_face_landmarks.dat")
        self.lenses['mustache'] = cv2.imread("img/mustache.png", -1)
        self.lenses['glasses'] = cv2.imread("img/glasses.png", -1)

    def tick(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = self.detector(gray)
        for face in faces:
            img = self.fetchFaces(face, gray, img)
        return img

    def lensMustache(self, landmarks, img):
        degree = math.degrees(math.atan2(landmarks.part(35).y-landmarks.part(31).y, landmarks.part(35).x-landmarks.part(31).x))
        mustache = imutils.rotate_bound(self.lenses['mustache'], degree)
        orig_mask = mustache[:,:,3]
        orig_mask_inv = cv2.bitwise_not(orig_mask)
        mustache = mustache[:,:,0:3]
        origMustacheHeight, origMustacheWidth = mustache.shape[:2]
        mustacheWidth = abs(3 * (landmarks.part(31).x - landmarks.part(35).x))
        mustacheHeight = int(mustacheWidth * origMustacheHeight / origMustacheWidth) - 10
        mustache = cv2.resize(mustache, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
        mask = cv2.resize(orig_mask, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
        mask_inv = cv2.resize(orig_mask_inv, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
        y1 = int(landmarks.part(33).y - (mustacheHeight/2)) + 10
        y2 = int(y1 + mustacheHeight)
        x1 = int(landmarks.part(51).x - (mustacheWidth/2))
        x2 = int(x1 + mustacheWidth)
        roi = img[y1:y2, x1:x2]
        roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        roi_fg = cv2.bitwise_and(mustache,mustache,mask = mask)
        img[y1:y2, x1:x2] = cv2.add(roi_bg, roi_fg)
        return img
    
    def lensGlasses(self, landmarks, img):
        degree = math.degrees(math.atan2(landmarks.part(16).y-landmarks.part(0).y, landmarks.part(16).x-landmarks.part(0).x))
        glass = imutils.rotate_bound(self.lenses['glasses'], degree)
        orig_mask_g = glass[:,:,3]
        orig_mask_inv_g = cv2.bitwise_not(orig_mask_g)
        glass = glass[:,:,0:3]
        origGlassHeight, origGlassWidth = glass.shape[:2]
        glassWidth = abs(landmarks.part(16).x - landmarks.part(0).x)
        glassHeight = int(glassWidth * origGlassHeight / origGlassWidth)
        glass = cv2.resize(glass, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
        mask = cv2.resize(orig_mask_g, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
        mask_inv = cv2.resize(orig_mask_inv_g, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
        y1 = int(landmarks.part(24).y)
        y2 = int(y1 + glassHeight)
        x1 = int(landmarks.part(27).x - (glassWidth/2))
        x2 = int(x1 + glassWidth)
        roi1 = img[y1:y2, x1:x2]
        roi_bg = cv2.bitwise_and(roi1,roi1,mask = mask_inv)
        roi_fg = cv2.bitwise_and(glass,glass,mask = mask)
        img[y1:y2, x1:x2] = cv2.add(roi_bg, roi_fg)
        return img
    
    def fetchFaces(self, face, gray, img):
        x1 = face.left() # left point
        y1 = face.top() # top point
        x2 = face.right() # right point
        y2 = face.bottom() # bottom point
        landmarks = self.predictor(image=gray, box=face)

        if self.printDots:
            for n in range(0, 68): #[0, 16, 31, 35, 24, 27]
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(img=img, center=(x, y), radius=2, color=(0, 255, 0), thickness=-1)

        img = self.lensMustache(landmarks, img)

        img = self.lensGlasses(landmarks, img)

        return img