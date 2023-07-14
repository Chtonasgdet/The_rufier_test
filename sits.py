from kivy.uix.label import Label

class Sits(Label):
    def __init__(self, total, **kwargs):
        super().__init__(**kwargs)
        self.current = 0
        self.total = total
        self.text = "Осталось приседаний: " + str(self.total)

    def next(self, *args):
        self.current += 1
        squats = max(0, self.total - self.current)
        self.text = "Осталось приседаний: " + str(squats)
        