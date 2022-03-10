from kivy.uix.checkbox import CheckBox
from kivy.app import App
from kivy.core.window import Window


def on_checkbox_active(checkbox, value):
    if value:
        print(value)
        print('The checkbox', checkbox, 'is active')
    else:
        print("操")
        print('The checkbox', checkbox, 'is inactive')


class MyApp(App):

    def build(self):
        Window.fullscreen = False
        Window.size = (800, 400)
        checkbox = CheckBox()
        checkbox.bind(active=on_checkbox_active)

        return checkbox


if __name__ == "__main__":
    MyApp().run()
