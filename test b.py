from kivy.lang import Builder

from kivymd.app import MDApp


class TestNavigationDrawer(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file("test.kv")


TestNavigationDrawer().run()