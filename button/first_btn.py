from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class TestApp(App):
    def build(self):
        Window.fullscreen = False
        Window.size = (800, 400)
        return Button(text='Hello World')


if __name__ == "__main__":
    TestApp().run()
