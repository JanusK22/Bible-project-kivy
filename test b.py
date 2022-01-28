from kivy.lang import Builder

from kivymd.app import MDApp


class Bible(MDApp):
    data = {
        'Version': 'book-multiple',
        'Jump in': 'debug-step-over',
        'Search': 'text-search',
    }


    def build(self):
        self.theme_cls.primary_palette = "Indigo"

        return Builder.load_file("test.kv")


Bible().run()