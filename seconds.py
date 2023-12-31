from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.uix.label import Label

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.current = 0
        self.text = 'Прошло секунд: ' + str(self.current)

    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = 'Прошло секунд: ' + str(self.current)
        self.start()

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = 'Прошло секунд: ' + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False