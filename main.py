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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


from kivy.properties import ObjectProperty, NumericProperty, StringProperty

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

# These empty classes are defined so that they can be used in the .kv file,
# otherwise the base class could be styled but that would also style all
# future instances wich is very impratical.
class ScrollBox(ScrollView):
    pass
class ScrollLayout(GridLayout):
    pass


class RightPane(BoxLayout):
    def __init__(self, **kwargs):
        super(RightPane, self).__init__(**kwargs)
        self.layer_list = []

        # Create and add the Add Layer button
        self.addLayerBtn = Button(text = 'Add Layer', size_hint_y = .1)
        self.addLayerBtn.bind(on_press = self.add_layer)
        self.add_widget(self.addLayerBtn)

        # Add buttons of another class
        self.add_widget(Btn_add(size_hint_y = .1))
        self.add_widget(Btn_sub(size_hint_y = .1))

        # Make the layer scroll list
        self.scroller = ScrollBox()
        self.scroll_layout = ScrollLayout()
        # Automatically set the layout size to fit all its children,
        # I think this works by minimum_height automatically being updated
        # when contents change, which in turn activates the setter() method
        # which does a similar calculation on its own...?
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.scroller.add_widget(self.scroll_layout)
        self.add_widget(self.scroller)

    def add_layer(self, *args):
        print('add layer')
        self.layer_list.append(Layer())
        self.scroll_layout.add_widget(self.layer_list[-1])
        pass


class Layer(BoxLayout):
    content = NumericProperty(10)
    id = NumericProperty(1)

    def __init__(self, **kwargs):
        super(Layer, self).__init__(**kwargs)
        # self.id = id
        pass

    def spinner_press(self, *args):
        print('spinner pressed')
        pass

class Display(BoxLayout):
    num_prop = NumericProperty(100)

class LayersApp(App):
    def build(self):
        return MainFrame()


if __name__ == '__main__':
    LayersApp().run()
