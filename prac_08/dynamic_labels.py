
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    main_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Lachlan", "Jordan", "Ben", "Regan"]

    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file("dynamic_labels.kv")
        return self.root

    def print_names(self):
        for name in self.names:
            self.root.main.text = str(name)


DynamicLabelsApp().run()
