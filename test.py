from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty, get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineListItem

from Tools import Creator
from Tools.Query import Query_sql


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    text = StringProperty()


class MyItem(TwoLineListItem):
    pass


class Bible(MDApp):
    overlay_color = get_color_from_hex("#6042e4")

    data = {
        'Version': 'book-multiple',
        'Jump in': 'debug-step-over',
        'Search': 'text-search',
    }

    que = Query_sql().random_verse()[0]
    verse_today = ".".join([str(i) for i in que])

    def remove_item(self, instance):
        self.root.ids.md_list.remove_widget(instance)

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.material_style = "M3"

        return Builder.load_file("test.kv")

    def on_start(self):
        que = Query_sql().random_verse()[0]
        for i in Creator.Read_book("kjv").read_book():
            self.root.ids.selection_list.add_widget(i)

        verse_today = ".".join([str(i) for i in que])
        self.root.ids.box.add_widget(
            MD3Card(
                line_color=(0.2, 0.2, 0.2, 0.8),
                style="filled",
                text=verse_today
            )
        )

    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.root.ids.selection_list.unselected_all(),
                ]
            ]
            right_action_items = [["share"], ["dots-vertical"]]
        else:
            md_bg_color = (0, 0, 0, 1)
            left_action_items = [["menu"]]
            right_action_items = []
            self.root.ids.toolbar.title = "KJV version to put"

        Animation(md_bg_color=md_bg_color, d=1).start(self.root.ids.toolbar)
        self.root.ids.toolbar.left_action_items = left_action_items
        self.root.ids.toolbar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.root.ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )


Bible().run()
