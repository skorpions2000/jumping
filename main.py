from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import ThreeLineAvatarListItem
from kivymd.uix.tab import MDTabsBase

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer


BoxLayout:

    HotReloadViewer:
        size_hint_x: .3
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 1, 0, 1
        errors_background_color: app.theme_cls.bg_dark
'''

class Tab(MDFloatLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class GL(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem(text="Three-line item with avatar", secondary_text="Secondary text here", tertiary_text="fit more text than usual"))
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())

        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())

        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())
        self.add_widget(ThreeLineAvatarListItem())

class ContentNavigationDrawer(BoxLayout):
    """
    Этот класс переключает скрины которые в меню которое реализовано
    в файле main.kv
    """
    test_value = 'In name'
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Example(MDApp):
    path_to_kv_file = "main.kv"

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)


Example().run()