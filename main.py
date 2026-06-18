from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "🔮 Opataz AI Offline"

        MDLabel:
            text: "⏱️ Time"
            halign: "center"
            font_style: "H5"

        MDCard:
            size_hint_y: None
            height: "100dp"

            MDLabel:
                text: "Time Here"
                halign: "center"

        MDLabel:
            text: "📊 Rang Box"
            halign: "center"
            font_style: "H5"

        ScrollView:

            MDList:
                id: rang_box_list

        MDLabel:
            text: "🔢 O'"
            halign: "center"

        MDLabel:
            id: opataz_prime
            text: "0"

        MDLabel:
            text: "🎯 Final Opataz"
            halign: "center"

        MDLabel:
            id: opataz_final
            text: "0"
'''

class OpatazApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

OpatazApp().run()
