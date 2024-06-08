import mysql.connector
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class MyApp(App):
    def build(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="puntajes"
        )
        self.cursor = self.conn.cursor()

        layout = BoxLayout(orientation='vertical')

        self.counter = 0
        self.label = Label(text=str(self.counter), font_size='50sp')
        layout.add_widget(self.label)

        button = Button(text='Suma para ganar', background_color=(1, 0, 0, 1))
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)

        email_input = TextInput(hint_text='Ingresa tu correo electrónico')
        layout.add_widget(email_input)

        send_button = Button(text='Enviar puntaje', size_hint_y=None, height=50)
        send_button.bind(on_press=lambda instance: self.send_score(instance, email_input.text))
        layout.add_widget(send_button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = str(self.counter)

    def send_score(self, instance, email):
        if not email:
            self.show_popup("Por favor, ingresa tu correo electrónico.")
            return

        max_value = self.counter

        try:
            self.cursor.execute("INSERT INTO usuarios (email, puntaje) VALUES (%s, %s)", (email, max_value))
            self.conn.commit()
            self.show_popup("Puntaje enviado correctamente.")
        except mysql.connector.Error as error:
            self.show_popup(f"Error al enviar el puntaje: {error}")

    def show_popup(self, message):
        popup = Popup(title='Mensaje', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MyApp().run()