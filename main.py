from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

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
class MainScreen(Screen):
    text = StringProperty('ask')
    def on_enter(self, *args):
        pass



class AskView(MDCard):
    login = StringProperty('login')
    question_content = StringProperty('ask')
    question_detail = StringProperty('ask')
    pass


class AnswerView(MDCard):
    login = StringProperty('login')
    answer_content = StringProperty('answer')
    answer_detail = StringProperty('answer')
    pass


class Tags(MDChip):
    text_tag = StringProperty('tag')
    pass


class TagsBlock(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Tags(text_tag="la la la"))
        self.add_widget(Tags(text_tag="llo lo lo"))
        self.add_widget(Tags(text_tag="llu lu lu"))
        self.add_widget(Tags(text_tag="la li la"))
        self.add_widget(Tags(text_tag="lyyy la la"))



class AllViewScroll(ScrollView):
    pass


class Content(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(AskView(login='My login', question_content="La alalla lsjdjd ufdhvdsl fgsdlkglkdsfj fdsgsdfg dsgfds gdf gdsf g sdf g sdf gd sfsdfgdsgsdfg ", question_detail='My Ask dfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fds nddfg fdмs nddc'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd ufdhvdsl fgsdlkglkdsfj fdsgsdfg dsgfds gdf gdsf g sdf g sdf gd sfsdfgdsgsdfg ", answer_detail='My Ask dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg fAsk dfg f'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd ufdhvdsl fgsdlkglkdsfj fdsgsdfg dsgfds gdf gdsf g sdf g sdf gd sfsdfgdsgsdfg ", answer_detail='My Askjhnljknhkjhljk lkj jlk lkh lkhlk j;l kjl jlkjj; f'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd ufdhvdsl fgsdlkglkdsfj fdsgsdfg dsgfds gdf gdsf g sdf g sdf gd sfsdfgdsgsdfg ", answer_detail='My Ashhloihihi juhlk hlkhl khk hkjf'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd ufdhvdsl fgsdlkglkdsfj", answer_detail='My A hjh lhjlohjlhlkjhlkj hkj hklh jklhklj hlkh khl khkh kljh lk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))
        self.add_widget(AnswerView(login='My login', answer_content="La alalla lsjdjd u", answer_detail='Myddfsddf bgjhgj khj jgjh gjk gkjh gkjh gkj gjk gjk gkj kj hgjh gkj gk khjjhhk'))



class Example(MDApp):
    path_to_kv_file = "main.kv"

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)


Example().run()
