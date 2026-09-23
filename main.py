from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import webbrowser

class PlataformaApp(App):
    def build(self):
        self.icon = 'Logo.png'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        try:
            logo = Image(source='Logo.png', size_hint=(1, 0.4))
            layout.add_widget(logo)
        except:
            erro_label = Label(text='[ Logo Aqui ]', color=(1, 0, 0, 1), size_hint=(1, 0.4))
            layout.add_widget(erro_label)

        texto_boas_vindas = Label(
            text="Bem Vindo!\nA Plataforma de Crescimento",
            font_size='20sp',
            bold=True,
            halign='center',
            color=(0, 0.39, 0.08, 1)
        )
        texto_boas_vindas.bind(size=texto_boas_vindas.setter('text_size'))
        layout.add_widget(texto_boas_vindas)

        botao_site = Button(
            text="Abrir App",
            font_size='18sp',
            background_color=(0, 0.39, 0.08, 1),
            color=(0.81, 0.99, 0.84, 1),
            size_hint=(1, None),
            height=50
        )
        botao_site.bind(on_press=self.abrir_site)
        layout.add_widget(botao_site)

        botao_sair = Button(
            text="Sair",
            font_size='18sp',
            background_color=(0, 0.39, 0.08, 1),
            color=(0.81, 0.99, 0.84, 1),
            size_hint=(1, None),
            height=50
        )
        botao_sair.bind(on_press=self.fechar_app)
        layout.add_widget(botao_sair)

        return layout

    def abrir_site(self, instance):
        webbrowser.open("https://serhumano.com.br/aldeias/")

    def fechar_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    PlataformaApp().run()
