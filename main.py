from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "🔮 Opataz AI (offline)"

        MDLabel:
            text: "⏱️ समय"
            halign: "center"
            font_style: "H5"

        MDCard:
            size_hint_y: None
            height: "100dp"

            MDLabel:
                text: "समय यहाँ दिखाई देगा"
                halign: "center"

        MDLabel:
            text: "📊 रंग बॉक्स एवं आवृत्ति"
            halign: "center"
            font_style: "H5"

        ScrollView:

            MDList:
                id: rang_box_list

        MDLabel:
            text: "🔢 ओपटाज़' (O')"
            halign: "center"

        MDLabel:
            id: opataz_prime
            text: "0"

        MDLabel:
            text: "🎯 अंतिम ओपटाज़"
            halign: "center"

        MDLabel:
            id: opataz_final
            text: "0"
'''

class OpatazApp(MDApp):
    def build(self):
        self.title = "ओपटाज़ एआई"
        return Builder.load_string(KV)

OpatazApp().run()
