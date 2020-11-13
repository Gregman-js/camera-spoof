from time import time, sleep

from Camera import Camera
from Commander import Commander
from ModuleHandler import ModuleHandler


camera = Camera()
handler = ModuleHandler(camera)
commander = Commander(handler)
while commander.run:
    start_time = time()
    fps = handler.getMode('f')

    if not handler.getMode('p'):
        img = camera.readCamera()
        img = handler.tick(img)
        camera.printFrame(img)

    running_time = (time() - start_time)
    break_time = fps - running_time
    if break_time < 0:
        break_time = 0
    sleep(break_time)
    # print("%.3f - %.3f" % ((time() - start_time), fps))
