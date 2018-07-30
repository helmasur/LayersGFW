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

from random import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox


from kivy.properties import ObjectProperty, NumericProperty, StringProperty, ListProperty, DictProperty


class MainFrame(BoxLayout):
    layers_dict = {}
    # num_prop = NumericProperty(456)
    def input_to_layer(self, *args):
        # self.num_prop = int(self.ids.theLeftInput.text)
        # layers_dict[Layer.active_layer].ids.thumb.text = str(self.num_prop)
        pass
    def on_num_prop(self, *args):
        print('werga')

    def test(self, *args):
        print(MainFrame.layers_dict[Layer.active].content)
        MainFrame.layers_dict[Layer.active].content += 1
        print(MainFrame.layers_dict[Layer.active].content)

class LayersApp(App):
    def build(self):
        return MainFrame()

class Display(BoxLayout):
    def input(self, *args):
        print('ok')
        print(self.ids.txtin.text)
        # self.num_prop = int(self.ids.txtin.text)
        # print(self.num_prop)
        print('act layer: '+Layer.active_layer)
        # print(self.parent.ids.rpanel.)
        # print(layers_dict)
        pass
    def new_num(self, *args):
        print('dfg')

class LayerTools(BoxLayout):
    pass

class RightPane(BoxLayout):
    inc_layer_id = 0 # incremental id

    def __init__(self, **kwargs):
        super(RightPane, self).__init__(**kwargs)

    def add_layer(self, *args):
        MainFrame.layers_dict[self.inc_layer_id] = Layer(self.inc_layer_id)
        self.parent.ids.theScrollGrid.add_widget(MainFrame.layers_dict[self.inc_layer_id])
        self.inc_layer_id += 1

    def add_thumb(self, *args):
        MainFrame.layers_dict[self.inc_layer_id] = ThumbLayer(self.inc_layer_id)
        self.parent.ids.theScrollGrid.add_widget(MainFrame.layers_dict[self.inc_layer_id])
        self.inc_layer_id += 1

class ThumbLayer(BoxLayout):
    active = NumericProperty(0)


    def __init__(self, lid, **kwargs):
        super(ThumbLayer, self).__init__(**kwargs)
        self.layer_id = lid
        ThumbLayer.active = lid
        self.content = NumericProperty(1)


    def update(self, ob, *args):
        ob.text = str(self.content)



class Layer(BoxLayout):
    active = NumericProperty(0)

    def __init__(self, lid, **kwargs):
        super(Layer, self).__init__(**kwargs)
        self.layer_id = lid
        Layer.active = lid
        self.content = 22
        # self.ids.thumb.bind(text=self.parent.parent.content)
        # self.ids.thumb.text = '0'

    def get_content(self, *args):
        return self.content

    def set_active(self, *args):
        Layer.active = self.layer_id
        print('Active layer: '+str(Layer.active))

    def spinner_press(self, *args):
        print('spinner pressed')
        pass

    def print_id(self, *args):
        print(self.layer_id)

    def print_active(self, *args):
        print(Layer.active)

if __name__ == '__main__':
    LayersApp().run()
