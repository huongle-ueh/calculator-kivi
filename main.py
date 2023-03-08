from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class Calculator(FloatLayout):
    def __init__(self):
        super().__init__()
        self.input_box = self.ids.input_box
        self.result = 0
        self.operation = None

    def add_operation(self, operator):
        self.result = float(self.input_box.text)
        self.operation = operator
        self.input_box.text = ""

    def calculate(self):
        if self.operation == "+":
            self.result += float(self.input_box.text)
        elif self.operation == "-":
            self.result -= float(self.input_box.text)
        elif self.operation == "*":
            self.result *= float(self.input_box.text)
        elif self.operation == "/":
            self.result /= float(self.input_box.text)
        self.input_box.text = str(self.result)

    def clear_input(self):
        self.input_box.text = ""

    def delete_input(self):
        self.input_box.text = self.input_box.text[:-1]

class CalculatorApp(App):
    def build(self):
        Builder.load_file('main.kv')
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
