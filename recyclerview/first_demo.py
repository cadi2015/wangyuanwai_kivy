from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window

Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str("wang yuan wai")} for x in range(100)]


class Application(App):
    def build(self):
        Window.fullscreen = False
        Window.size = (800, 400)
        return RV()


if __name__ == '__main__':
    Application().run()
