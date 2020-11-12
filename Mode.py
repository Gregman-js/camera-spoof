class Mode:
    idx = 0

    def __init__(self, camera=False, handler=False):
        self.camera = camera
        self.handler = handler
        self.setup()
    
    def setup(self):
        pass

    def getValue(self):
        return self.value[self.idx]
    
    def updateValue(self, lvl=0):
        self.idx += 1
        if self.idx >= len(self.value):
            self.idx = 0
        self.onUpdate()
    
    def onUpdate(self):
        pass