from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window


class RootView(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootView, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World,My Button",
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5}))


class MainApp(App):

    def build(self):
        Window.fullscreen = False
        Window.size = (800, 400)
        self.root = root_view = RootView()
        root_view.bind(size=self._update_rect, pos=self._update_rect)

        with root_view.canvas.before:
            Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root_view.size, pos=root_view.pos)  # 长方形的绿色ViewGroup跟随父控件的大小
        return root_view

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MainApp().run()
