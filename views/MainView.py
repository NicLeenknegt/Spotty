import itertools, threading, time, sys

class MainView:

    def __init__(self):
        self.done = False
        self.animation_frames = [ '|', '/', '-', '\\' ]

    def run_animation(self):
        for c in itertools.cycle(self.animation_frames):
            if self.done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!')

    def start_loading_animation(self):
        t = threading.Thread(target=self.run_animation)
        t.start()

    def stop_loading_animation(self):
        self.done = True
