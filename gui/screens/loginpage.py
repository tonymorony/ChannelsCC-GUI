from lib import rpclib
from kivy.app import App
from kivy.uix.screenmanager import Screen


class LoginPage(Screen):

    def verify_credentials(self):
        while True:
            try:
                server_input = self.ids["rpcserver"].text
                user_input = self.ids["rpcuser"].text
                password_input = self.ids["rpcpassword"].text
                port_input = int(self.ids["port"].text)
                connection = rpclib.rpc_connect(user_input, password_input, server_input, port_input)
            except Exception as e:
                print(e)
                print("Not connected. Please check credentials")
                # TODO: have to throw popup and in this case not clean text fields
                self.ids["rpcserver"].text = ''
                self.ids["rpcuser"].text = ''
                self.ids["rpcpassword"].text = ''
                self.ids["port"].text = ''
                break
            else:
                App.get_running_app().rpc_connection = connection
                App.get_running_app().is_connected = True
                self.manager.current = "user"
                break
