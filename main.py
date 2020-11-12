import time

from Camera import Camera
from Commander import Commander
from ModuleHandler import ModuleHandler


camera = Camera()
handler = ModuleHandler(camera)
commander = Commander(handler)
while commander.run:
    fps = handler.getMode('f')

    # start_time = time.time()

    if not handler.getMode('p'):
        img = camera.readCamera()
        img = handler.tick(img)
        camera.printFrame(img)

    # print("%.3f - %.3f" % ((time.time() - start_time), fps))

    time.sleep(fps)