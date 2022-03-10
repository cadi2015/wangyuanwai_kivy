from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

spinner = Spinner(
    # default value shown
    text='Home',
    # available values
    values=('Home', 'Work', 'Other', 'Custom'),
    # just for positioning in our example
    size_hint=(None, None),
    size=(100, 44),
    pos_hint={'center_x': .5, 'center_y': .5})


def show_selected_value(spinner, text):
    print('The spinner', spinner, 'has text', text)


if __name__ == "__main__":
    spinner.bind(text=show_selected_value)

    runTouchApp(spinner)
