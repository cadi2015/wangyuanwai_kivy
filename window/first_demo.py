from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.config import Config


class CameraApp(App):
    def build(self):
        self.title = "camera tool"
        Window.fullscreen = False
        Window.size = (800, 400)
        Config.set('graphics', 'resizable', False)
        my_label = Label(text="hello world")
        return my_label


if __name__ == "__main__":
    CameraApp().run()
