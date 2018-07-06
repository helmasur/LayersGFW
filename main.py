'''
LAYERS

Kivy v1.10.0
Python v3.6.5

Användbara kivy examples:

    demo\
            kivycatalog
            showcase

    widgets\
            compound_selection
            Splitter
            spinner
            colorpicker
            colorusage
            effectwidget
            fbowidget - för att rita tusentals widgets
            focus_behavior
            label_sizing - anpassa text till yta
                textalign
                shorten text
            textinput
            popup with kv
            label with markup
                rstexample
            scatter
            scrollview - scrolla lagerlistan
            settings - !
            tabbedpanel
    misc\
            two panes - knappar uppdaterar ruta






Note
COMMON ERROR: The name of the kv file, e.g. pong.kv,
must match the name of the app, e.g. PongApp
(the part before the App ending).
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty, NumericProperty

class MainFrame(BoxLayout):
    pass

class Btn_add(Button):
    def __init__(self, **kwargs):
        super(Btn_add, self).__init__(**kwargs)
        self.text = "+"
    def on_press(self, *args):
        self.parent.parent.ids.disp_instance.num_prop += 1

class Btn_sub(Button):
    def __init__(self, **kwargs):
        super(Btn_sub, self).__init__(**kwargs)
        self.text = "-"
    def on_press(self, *args):
        self.parent.parent.ids.disp_instance.num_prop -= 1

class RightPane(BoxLayout):
    def __init__(self, **kwargs):
        super(RightPane, self).__init__(**kwargs)
        self.add_widget(Btn_add())
        self.add_widget(Btn_sub())
        self.add_widget(Layer())

class Layer(BoxLayout):
    content = NumericProperty(10)
    def stuff(self, *args):
        pass

class Display(BoxLayout):
    num_prop = NumericProperty(100)

class LayersApp(App):
    def build(self):
        return MainFrame()


if __name__ == '__main__':
    LayersApp().run()
