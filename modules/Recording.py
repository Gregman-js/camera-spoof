from time import time
from Module import Module

class Recording(Module):

    lvl = 5
    priority = 1
    name = 'rec'
    enable = False
    record = []
    recStep = 0
    bckwrd = False
    recording = False

    def onEnable(self, lvl):
        self.recording = True
        self.record = []
        self.recStep = 0
        self.lvl = lvl
        self.bckwrd = False
        self.countTime = time()

    def tick(self, img):
        if self.recording:
            self.record.append(img)
            if time() - self.countTime >= self.lvl:
                self.recording = False
                self.recStep = len(self.record) - 1
                self.bckwrd = True
                print("Playing record")
            return img
        else:
            img = self.record[self.recStep]
            if not self.bckwrd:
                self.recStep += 1
                if self.recStep >= len(self.record):
                    self.recStep -= 1
                    self.bckwrd = not self.bckwrd
            else:
                self.recStep -= 1
                if self.recStep < 0:
                    self.recStep += 1
                    self.bckwrd = not self.bckwrd
            return img