
class Observable:

    def __init__(self,value):
        self.value = value
        self.listener = None

    def observe(self, func):
        self.listener = func

    def set(self,value):
        self.value = value
        self.listener(value)
