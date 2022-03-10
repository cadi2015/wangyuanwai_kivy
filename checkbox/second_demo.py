from random import uniform
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

if __name__ == "__main__":
    x = GridLayout(cols=4)
    for i in range(36):
        r, g, b = [uniform(0.2, 1.0) for j in range(3)]
        x.add_widget(CheckBox(group='1' if i % 2 else '', color=[r, g, b, 2]))
    Window.fullscreen = False
    Window.size = (800, 400)
    runTouchApp(x)
