import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window

kivy.require('1.0.5')


class Controller(FloatLayout):
    label_wid = ObjectProperty()
    btn_info = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.number = 1

    def do_action(self):
        self.label_wid.text = "show what?????????????????"


class ControllerApp(App):

    def build(self):
        Window.fullscreen = False
        Window.size = (800, 400)
        return Controller(btn_info='change camera')


if __name__ == '__main__':
    ControllerApp().run()
