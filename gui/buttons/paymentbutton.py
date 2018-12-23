from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.popup import Popup


class PaymentButton(Button):

    application = App.get_running_app()

    def on_release(self):

        if self.application.active_channel_id == "":
            content = Button(text="Please select channel first!")
            popup = Popup(title='No channels selected', content=content, auto_dismiss=False)
            content.bind(on_press=popup.dismiss)
            popup.open()
        else:
            self.application.root.ids.userpage.manager.current = "paymentpage"
