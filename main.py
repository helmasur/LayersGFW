#Kivy v1.10.0
#Python v3.6.5

'''
Note
COMMON ERROR: The name of the kv file, e.g. pong.kv,
must match the name of the app, e.g. PongApp
(the part before the App ending).
'''

from kivy.app import App
from kivy.uix.widget import Widget


class MainFrame(Widget):
    pass

class Layer(Widget):
    pass


class LayersApp(App):
    def build(self):
        return MainFrame()


if __name__ == '__main__':
    LayersApp().run()
