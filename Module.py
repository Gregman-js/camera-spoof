class Module:
    enable = False
    priority = 50
    def __init__(self, camera=False, handler=False):
        self.camera = camera
        self.handler = handler
        self.setup()
    
    def setup(self):
        pass

    def toggle(self, lvl):
        self.enable = not self.enable
        if self.enable:
            self.onEnable(lvl)
        else:
            self.onDisable(lvl)
    
    def process(self, img):
        if self.enable:
            return self.tick(img)
        return img

    def tick(self, img):
        return img
    
    def onEnable(self, lvl):
        pass

    def onDisable(self, lvl):
        pass