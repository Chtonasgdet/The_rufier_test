from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
from runner import Runner
from sits import Sits

age = 0
name_in = ''
p1, p2, p3 = 0, 0, 0

def check_int(num):
    try:
        return int(num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        greeting = Label(text = txt_instruction)

        hline1_scr1 = BoxLayout(size_hint = (.8, None), height = '30sp')
        name = Label(text = 'Введите имя:')
        self.user_name = TextInput(text = 'Имя', multiline = False)
        hline1_scr1.add_widget(name)
        hline1_scr1.add_widget(self.user_name)

        hline2_scr1 = BoxLayout(size_hint = (.8, None), height = '30sp')
        age = Label(text = 'Введите вораст:')
        self.user_age = TextInput()
        hline2_scr1.add_widget(age)
        hline2_scr1.add_widget(self.user_age)

        self.transition = Button(text = 'Начать', size_hint = (.3, .2), pos_hint = {'center_x': 0.5})
        self.transition.on_press = self.next

        vline1_scr1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vline1_scr1.add_widget(greeting)
        vline1_scr1.add_widget(hline1_scr1)
        vline1_scr1.add_widget(hline2_scr1)
        vline1_scr1.add_widget(self.transition)

        self.add_widget(vline1_scr1)

    def next(self):
        global name_in, age
        name_in = self.user_name.text
        age = check_int(self.user_age.text)
        if age == False or age < 7:
            age = 7
            self.user_age.text = str(age)
        else:
            self.manager.current = 'scr_2'

class PulseScr_1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.timer_1 = Seconds(15)
        self.timer_1.bind(done = self.sec_finish)
        measurement_1 = Label(text = txt_test1)

        hline1_scr2 = BoxLayout(size_hint = (.8, None), height = '30sp')
        result_1 = Label(text = 'Введите реультат:')
        self.user_result_1 = TextInput(text = '0', multiline = False)
        self.user_result_1.set_disabled(True)
        hline1_scr2.add_widget(result_1)
        hline1_scr2.add_widget(self.user_result_1)

        self.transition_1 = Button(text = 'Начать измерение', size_hint = (.3, .2), pos_hint = {'center_x': 0.5})
        self.transition_1.on_press = self.next

        vline1_scr2 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vline1_scr2.add_widget(measurement_1)
        vline1_scr2.add_widget(self.timer_1)
        vline1_scr2.add_widget(hline1_scr2)
        vline1_scr2.add_widget(self.transition_1)

        self.add_widget(vline1_scr2)

    def sec_finish(self, *args):
        self.next_screen = True
        self.user_result_1.set_disabled(False)
        self.transition_1.set_disabled(False)
        self.transition_1.text = 'Продолжить'

    def next(self):
        if not self.next_screen:
            self.transition_1.set_disabled(True)
            self.timer_1.start()
        else:
            global p1
            p1 = check_int(self.user_result_1.text)
            if p1 == False or p1 < 0:
                p1 = 0
                self.user_result_1.text = str(p1)
            else:
                self.manager.current = 'scr_3'

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen4 = False

        sits = Label(text = txt_test2)

        self.label_count = Sits(30)
        self.count_sits = Runner(30, 1.5, True, size_hint = (0.4, 1))
        self.count_sits.bind(finished = self.sits_finised)
        h3_1 = BoxLayout()
        vline0_scr3 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vline0_scr3.add_widget(sits)
        vline0_scr3.add_widget(self.label_count)
        vline0_scr3.add_widget(self.count_sits)
        h3_1.add_widget(vline0_scr3)

        self.transition_2 = Button(text = 'Начать', size_hint = (.3, .2), pos_hint = {'center_x': 0.5})
        self.transition_2.on_press = self.next

        vline1_scr3 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vline1_scr3.add_widget(h3_1)
        vline1_scr3.add_widget(self.transition_2)

        self.add_widget(vline1_scr3)

    def sits_finised(self, instance, value):
        self.transition_2.set_disabled(False)
        self.transition_2.text = 'Продолжить'
        self.next_screen4 = True

    def next(self):
        if not self.next_screen4:
            self.transition_2.set_disabled(True)
            self.count_sits.start()
            self.count_sits.bind(value = self.label_count.next)
        else:
            self.manager.current = 'scr_4'

class PulseScr_2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen2 = False
        self.timer_2 = Seconds(15)
        self.timer_2.bind(done = self.sec_finish2)

        measurements_2 = Label(text = txt_test3)
        self.hint = Label(text='Замерьте пульс')

        hline1_scr4 = BoxLayout(size_hint = (.8, None), height = '30sp')
        result_4 = Label(text = 'Результат:')
        self.user_result_4 = TextInput(text = '0', multiline = False)
        self.user_result_4.set_disabled(True)
        hline1_scr4.add_widget(result_4)
        hline1_scr4.add_widget(self.user_result_4)

        hline2_scr4 = BoxLayout(size_hint = (.8, None), height = '30sp')
        result4_after_rest = Label(text = 'Результат после отдыха:')
        self.user_result4_after_rest = TextInput(text = '0', multiline = False)
        self.user_result4_after_rest.set_disabled(True)
        hline2_scr4.add_widget(result4_after_rest)
        hline2_scr4.add_widget(self.user_result4_after_rest)

        self.ending = Button(text = 'Финальное измерение', size_hint = (.3, .2), pos_hint = {'center_x': 0.5})
        self.ending.on_press = self.next

        vline1_scr4 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vline1_scr4.add_widget(measurements_2)
        vline1_scr4.add_widget(self.hint)
        vline1_scr4.add_widget(self.timer_2)
        vline1_scr4.add_widget(hline1_scr4)
        vline1_scr4.add_widget(hline2_scr4)
        vline1_scr4.add_widget(self.ending)

        self.add_widget(vline1_scr4)

        self.stage = 0
        
    def sec_finish2(self, *args):
        if self.timer_2.done:
            if self.stage == 0:
                self.stage = 1
                self.hint.text = 'Отдых 30 сек'
                self.timer_2.restart(30)
                self.user_result_4.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.hint.text = 'Замерьте пульс'
                self.timer_2.restart(15)
            elif self.stage == 2:
                self.next_screen2 = True
                self.user_result4_after_rest.set_disabled(False)
                self.ending.set_disabled(False)
                self.ending.text = 'Завершить'


    def next(self):
        if not self.next_screen2:
            self.ending.set_disabled(True)
            self.timer_2.start()
        else:
            global p2, p3
            perehod = 0
            p2 = check_int(self.user_result_4.text)
            p3 = check_int(self.user_result4_after_rest.text)
            if p2 == False or p2 < 0:
                self.user_result_4.text = str(p2)
                perehod += 1
            if p3 == False or p3 < 0:
                self.user_result4_after_rest.text = str(p3)
                perehod += 1
            if perehod == 0:
                self.manager.current = 'scr_5'

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.final_result = Label(text = '')
        vline1_scr5 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vline1_scr5.add_widget(self.final_result)
        self.add_widget(vline1_scr5)

        self.on_enter = self.before

    def before(self):
        global name_in
        self.final_result.text = name_in + '\n' + test(p1, p2, p3, age)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name = 'scr_1'))
        sm.add_widget(PulseScr_1(name = 'scr_2'))
        sm.add_widget(CheckSits(name = 'scr_3'))
        sm.add_widget(PulseScr_2(name = 'scr_4'))
        sm.add_widget(Result(name = 'scr_5'))
        return sm


app = HeartCheck()
app.run()