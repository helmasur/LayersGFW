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


class MainFrame(BoxLayout):
    pass

class RightPane(BoxLayout):
    def __init__(self, **kwargs):
        super(RightPane, self).__init__(**kwargs)
        self.add_widget(Button(text='+'))
        self.add_widget(Button(text='-'))
    pass

class Display(BoxLayout):
    pass


class LayersApp(App):
    def build(self):
        return MainFrame()


if __name__ == '__main__':
    LayersApp().run()
