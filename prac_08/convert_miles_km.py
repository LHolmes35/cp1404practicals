
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATIO = 1.60933


class DistanceConverterApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def calculate_conversion(self):
        miles = self.get_valid_miles()
        kilometres = miles * CONVERSION_RATIO
        self.root.ids.output_label.text = str(kilometres)

    def handle_increment(self, change):
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.calculate_conversion()

    def get_valid_miles(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0


DistanceConverterApp().run()
