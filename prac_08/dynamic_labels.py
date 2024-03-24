"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Dawei Zhu, first version: 24/03/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: English syllables
        self.syllables = {
            "Level 1": "Physical",
            "Level 2": "Datalink",
            "Level 3": "Network",
            "Level 4": "Transport",
            "Level 5": "Session",
            "Level 6": "Presentation",
            "Level 7": "Application"
        }

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Network Layers"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for i in self.syllables:
            # add the items to the "entries_box" layout widget
            temp_label = Label(text=f'{i}: {self.syllables[i]}')
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
