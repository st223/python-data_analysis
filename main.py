# Индекс Руфье

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
global p1,p2,p3,age
age = 7
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

def test(p1, p2, p3):
    index = (4*(p1+p2+p3) -200)/10
    return index

def result_index(index, age):
    s = 'Неизвестный результат'
    i = 0
    if age <= 8:
        i = 0
    elif age <=10:
        i = 1
    elif age <= 12:
        i = 2
    elif age <=14:
        i = 3
    else:
        i = 4
    index += 1.5*i
    if index < 6:
        s = "Отличный результат! Ваше сердце работает как часы!"
    elif index < 12:
        s = "Хороший результат! Сердце работает хорошо, но не стоит злоупотреблять."
    elif index < 17:
        s = "Результат удовлетворительный. Но следует тщательнее следить за здоровьем"
    elif index < 21:
        s = "Результат слабый. Рекомендовано обращение к доктору."
    else:
        s = 'Результат ужасный. Обследуйтесь у врача как можно скорее!!!'
    
    return s

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainLab = Label(text = "Heart Check")
        btnTest = Button(text = "Пройти тест")
        btnTest.on_press = self.nextTest
        btnInstruction = Button(text = "Инструкция")
        btnInstruction.on_press = self.nextInstruction
        btnExit = Button(text = "Выход")
        btnExit.on_press = self.exit_app
        h1 = BoxLayout(orientation = "horizontal", padding = 20, spacing = 10)
        h2 = BoxLayout(orientation = "vertical", padding = 20, spacing = 10)

        v1 = BoxLayout(orientation = "vertical", padding = 20, spacing = 10)
        h1.add_widget(mainLab)
        h2.add_widget(btnTest)
        h2.add_widget(btnInstruction)
        h2.add_widget(btnExit)

        v1.add_widget(h1)
        v1.add_widget(h2)
        self.add_widget(v1)    
    def nextTest(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'test'
    def nextInstruction(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'instruction'
    def exit_app(self):
        app.stop()

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vmain = BoxLayout(orientation = "vertical", padding = 20, spacing = 10)
        lab1= Label(text = "Введите имя:")
        input1 = TextInput(text = "0", multiline = False)
        lab2 = Label(text = "Введите возраст:")
        self.input2 = TextInput(text = "0", multiline = False)
        lab3 = Label(text = "Замерьте пульс за 15 секунд. \nРезультат запишите в соответствующее поле.")
        self.input3 = TextInput(text = "0", multiline = False)
        lab4= Label(text = "Выполните 30 приседаний за 45 секунд. \nВ течение минуты замерьте пульс два раза: за первые 15 секунд минуты, затем за последние 15 секунд. \nРезультаты запишите в соответствующие поля.")
        self.input4 = TextInput(text = "0", multiline = False)
        self.input5 = TextInput(text = "0", multiline = False)
        btnNext = Button(text = "Рассчитать результаты:")
        btnNext.on_press = self.nextRes
        btnBack = Button(text = "В меню")
        btnBack.on_press = self.backMain
        vmain.add_widget(lab1)
        vmain.add_widget(input1)
        vmain.add_widget(lab2)
        vmain.add_widget(self.input2)
        vmain.add_widget(lab3)
        vmain.add_widget(self.input3)
        vmain.add_widget(lab4)
        vmain.add_widget(self.input4)
        vmain.add_widget(self.input5)
        vmain.add_widget(btnNext)
        vmain.add_widget(btnBack)
        self.add_widget(vmain)
    def nextRes(self):
        global p1,p2,p3,age
        age = check_int(self.input2.text)
        p1 = check_int(self.input3.text)
        p2 = check_int(self.input4.text)
        p3 = check_int(self.input5.text)
        
        normaldata = (age != False and age > 0) and (p1 != False and p1 > 0) and (p2 != False and p2 > 0) and (p3 != False and p3 > 0)
        if normaldata:
            self.manager.transition.direction = 'left'
            self.manager.current = 'result'
    def backMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vmain = BoxLayout(orientation = "vertical", padding = 20, spacing = 10)
        lab1 = Label(text = "Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего \nздоровья.", halign = 'left')
        lab2 = Label(text = "Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности \nсердца при физической нагрузке.", halign = 'left')
        lab3 = Label(text = "У испытуемого определяют частоту пульса за 15 секунд.", halign = 'left')
        lab4 = Label(text = "Затем в течение 45 секунд испытуемый выполняет 30 приседаний.", halign = 'left')
        lab5 = Label(text = "После окончания нагрузки пульс подсчитывается вновь: число пульсаций за первые 15 секунд, 30 секунд \nотдыха, число пульсаций за последние 15 секунд.", halign = 'left')
        btnBack = Button(text = "В меню")
        btnBack.on_press = self.backMain
        vmain.add_widget(lab1)
        vmain.add_widget(lab2)
        vmain.add_widget(lab3)
        vmain.add_widget(lab4)
        vmain.add_widget(lab5)
        vmain.add_widget(btnBack)
        self.add_widget(vmain)
    def backMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global p1,p2,p3,age
        index = test(p1,p2,p3)
        advice = result_index(age, index)
        self.indexLab = Label(text = "Ваш индекс Руфье:")
        self.levelLab = Label(text = str(index))
        self.adviceLab = Label(text = advice)
        btnBack = Button(text = "В меню")
        btnBack.on_press = self.backMain
        vmain = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        vmain.add_widget(self.indexLab)
        vmain.add_widget(self.levelLab)
        vmain.add_widget(self.adviceLab)
        vmain.add_widget(btnBack)
        self.add_widget(vmain)
        self.on_enter = self.res
    def backMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
    global p1,p2,p3,age
    age = 0
    p1 = 0
    p2 = 0
    p3 = 0
    def res(self):
        global p1,p2,p3,age
        index = test(p1,p2,p3)
        self.levelLab.text = str(index)
        self.adviceLab.text = result_index(index,age)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        main = MainScreen(name = 'main')
        test = TestScreen(name = 'test')
        result = ResultScreen(name = 'result')
        instruction = InstructionScreen(name = 'instruction')
        sm.add_widget(main)
        sm.add_widget(test)
        sm.add_widget(result)
        sm.add_widget(instruction)
        return sm

app = MyApp()
app.run()
