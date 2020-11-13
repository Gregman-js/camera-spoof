import threading
import sys
import signal

class Commander:
    run = True
    def __init__(self, moduleHandler):
        self.moduleHandler = moduleHandler
        self.thread = threading.Thread(target=self.read_input)
        self.thread.daemon = True
        self.thread.start()

        signal.signal(signal.SIGINT, self.signal_handler)
    
    def read_input(self):
        while True:
            inp = input()
            if inp == "e":
                self.run = False
                break
            else:
                self.moduleHandler.updateConfig(inp)

    def signal_handler(self, signal, frame):
        print("\nClosing")
        sys.exit(0)