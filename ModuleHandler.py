from modules.Blur import Blur
from modules.Darkness import Darkness
from modules.Resizer import Resizer
from modules.Dog import Dog
from modules.Zw import Zw
from modules.Glitch import Glitch
from modules.Recording import Recording
from modules.Lens import Lens

from modes.Fps import Fps
from modes.Pause import Pause

class ModuleHandler:
    modules = []
    modes = {}
    def __init__(self, camera):
        self.camera = camera
        self.modules = [
            Blur(),
            Darkness(),
            Resizer(camera=camera),
            Dog(camera=camera),
            Zw(camera=camera),
            Glitch(),
            Recording(camera=camera, handler=self),
            Lens()
        ]
        self.modes = {
            'f': Fps(),
            'p': Pause(),
        }
    
    def tick(self, img):
        sortedModules = sorted(self.modules, key=lambda el: el.priority)
        for module in sortedModules:
            img = module.process(img)
        return img
    
    def updateConfig(self, key):
        keys = key.split()
        if len(keys):
            key = keys[0]
            lvl = int(keys[1]) if len(keys) > 1 else 0
            for module in self.modules:
                if module.name == key:
                    module.toggle(lvl)
            if key in self.modes:
                self.modes[key].updateValue(lvl)
        
    def getMode(self, key):
        if key in self.modes:
            return self.modes[key].getValue()
        return False